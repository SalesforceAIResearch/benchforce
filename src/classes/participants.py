import os
import copy
import json
import logging
import websockets
import asyncio

from src.classes.proxy import ProxyClient
from src.classes.packet import UnifiedPacket, EventType
from src.classes.agents import Agent
from src.classes.noise import NoiseMixer
from src.classes.helper import Helper


class BaseParticipant:
    def __init__(self, session_id: str, entry, config, participant_type, environment):
        self.environment = environment
        self.entry = entry
        self.config = config
        self.type = participant_type
        self.ws_client = ProxyClient(
            f"ws://localhost:{os.environ.get('WS_SERVER_PORT', 6789)}",
            session_id,
            participant_type,
        )
        self.agent = Agent().build(
            entry=entry,
            config=config,
            participant_instance=self,
            environment=environment,
        )
        self.tasks = []
        self.terminated = False
        self.max_turns = config.max_turns
        self.current_turn = 0

        self.termination_event = asyncio.Event()
        self.termination_task = asyncio.create_task(self._termination_timer())

    async def _termination_timer(self):
        await asyncio.sleep(1200)
        await self.handle_session_termination()


    def increase_turn(self):
        self.current_turn += 1

    async def terminate_session(self):
        await self.ws_client.send_message(
            UnifiedPacket(
                event=EventType.BENCHFORCE_TERMINATE,
                config=json.dumps(vars(self.config) if self.type == "agent" else self.entry),
            ).to_json()
        )

    async def handle_session_termination(self):
        for task in self.tasks:
            if not task.done():
                task.cancel()
        self.tasks.clear()
        self.terminated = True
        await self.ws_client.close()
        self.termination_event.set()

    async def create(self):
        await self.ws_client.connect()
        await self.ws_client.send_message(
            UnifiedPacket(event=EventType.BENCHFORCE_HANDSHAKE).to_json()
        )

        data = copy.deepcopy(self.environment.get("data"))

        original_db_hash = Helper.get_data_hash(Helper.apply_mask(data, self.environment.get("filter_schema")))
        dryrun_db_hash = Helper.get_data_hash(Helper.apply_mask(Helper.dry_run(data, self.entry, self.environment.get("functions")), self.environment.get("filter_schema")))

        original_db_packet = UnifiedPacket(
            event=EventType.BENCHFORCE_LOG_ORIG_DB,
            hash=original_db_hash,
        ).to_json()

        dryrun_db_hash_packet = UnifiedPacket(
            event=EventType.BENCHFORCE_LOG_DRYRUN_DB,
            hash=dryrun_db_hash,
        ).to_json()

        await self.ws_client.send_message(original_db_packet)
        await self.ws_client.send_message(dryrun_db_hash_packet)

        self.tasks.append(asyncio.create_task(self.agent.connect()))
        self.tasks.append(asyncio.create_task(self.consume()))

        await self.termination_event.wait()

    async def produce(self, packet: UnifiedPacket):
        await self.ws_client.send_message(packet.to_json())

    async def forward_packet(self, packet: UnifiedPacket):
        if packet.event == EventType.BENCHFORCE_TERMINATE:
            await self.terminate_session()
            await self.handle_session_termination()
        else:
            await self.agent.consume(packet)

    async def consume(self):
        while not self.terminated:
            try:
                msg = await self.ws_client.ws.recv()
                data = json.loads(msg)
                packet_str = data.get("message")
                if not packet_str:
                    logging.error("Received message without 'message' field")
                else:
                    packet_data = json.loads(packet_str)
                    packet = UnifiedPacket(**packet_data)
                    await self.forward_packet(packet)
            except websockets.exceptions.ConnectionClosed:
                logging.info("Websocket connection with client closed")
                break
            except Exception as e:
                logging.error(f"Error processing incoming message: {e}")

    def set_is_async(self, is_async: bool):
        self.agent.set_is_async(is_async)



class ClientParticipant(BaseParticipant):
    def __init__(self, session_id: str, entry, config, environment, evaluator):
        self.session_id = session_id
        self.evaluator = evaluator
        self.noise_mixer = NoiseMixer(
            config.noises,
            config.noise_volume,
            config.sample_rate,
            config.cutoff_freq,
            config.clipping_threshold,
            config.drop_probability,
            config.snr_db,
            config.chunk_size_ms,
        )

        super().__init__(session_id, entry, config, "client", environment)

    async def forward_packet(self, packet: UnifiedPacket):
        if packet.event in [EventType.RESPONSE_TEXT_DONE, EventType.RESPONSE_AUDIO_TRANSCRIPT_DONE]:
            self.increase_turn()
        if self.current_turn == self.max_turns:
            await self.terminate_session()
            await self.handle_session_termination()

        await super().forward_packet(packet)

    async def handle_session_termination(self):
        await super().handle_session_termination()
        self.evaluator.check_entry(self.session_id, self.entry, self.environment)


class AgentParticipant(BaseParticipant):
    def __init__(
        self,
        session_id: str,
        entry,
        config,
        environment,
    ):
        super().__init__(session_id, entry, config, "agent", environment)

    async def produce(self, packet: UnifiedPacket):
        if packet.event == EventType.RESPONSE_FUNCTION_CALL_RESULT:
            packet.hash = Helper.get_data_hash(Helper.apply_mask(self.agent.provider.functions_data, self.environment.get("filter_schema")))

        await super().produce(packet)
