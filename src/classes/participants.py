import os
import json
import logging
from threading import Event
import websockets
import asyncio

from src.classes.proxy import ProxyClient
from src.classes.packet import UnifiedPacket, EventType
from src.classes.communicator import build_communicator
from src.classes.noise import NoiseMixer
from src.classes.helper import Helper


class BaseParticipant:
    def __init__(self, session_id: str, entry, config, participant_type, environment, with_agent = True, ws_host: str = "localhost", ws_port: int = 6789):
        self.environment = environment
        self.session_id = session_id
        self.with_agent = with_agent
        self.entry = entry
        self.config = config
        self.type = participant_type
        self.ws_client = ProxyClient(
            f"ws://{ws_host}:{ws_port}",
            session_id,
            participant_type,
        )
        self.communicator = build_communicator(
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
        await asyncio.sleep(int(self.config.termination_timer))
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
            UnifiedPacket(event=EventType.BENCHFORCE_HANDSHAKE, config=json.dumps(self.entry)).to_json()
        )

        self.tasks.append(asyncio.create_task(self.communicator.connect()))
        self.tasks.append(asyncio.create_task(self.consume()))

        await self.termination_event.wait()

    async def produce(self, packet: UnifiedPacket):
        await self.ws_client.send_message(packet.to_json())

    async def forward_packet(self, packet: UnifiedPacket):
        if packet.event == EventType.BENCHFORCE_TERMINATE:
            await self.terminate_session()
            await self.handle_session_termination()
        else:
            await self.communicator.consume(packet)

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
        self.communicator.set_is_async(is_async)


class ClientParticipant(BaseParticipant):
    def __init__(self, session_id: str, entry, config, environment, evaluator, with_agent = True, client_ready_event: Event = None, ws_host: str = "localhost", ws_port: int = 6789):
        self.delayed_greeting = []
        self.session_established = True if with_agent else False
        self.session_id = session_id
        self.with_agent = with_agent
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
        self.client_ready_event = client_ready_event
        super().__init__(
            session_id=session_id,
            entry=entry,
            config=config,
            participant_type="client",
            environment=environment,
            with_agent=with_agent,
            ws_host=ws_host,
            ws_port=ws_port,
        )

    async def forward_packet(self, packet: UnifiedPacket):
        if packet.event in [EventType.RESPONSE_TEXT_DONE, EventType.RESPONSE_AUDIO_TRANSCRIPT_DONE]:
            self.increase_turn()
        if self.current_turn == self.max_turns:
            await self.terminate_session()
            await self.handle_session_termination()

        await super().forward_packet(packet)

        if packet.event == EventType.BENCHFORCE_HANDSHAKE and not self.with_agent and not self.session_established and self.delayed_greeting:
            await super().produce(
                UnifiedPacket(event=EventType.BENCHFORCE_HANDSHAKE, config=self.entry)
            )
            for message in self.delayed_greeting:
                await super().produce(message)
            self.session_established = True
            self.delayed_greeting = []

    async def produce(self, packet: UnifiedPacket):
        if not self.with_agent and not self.session_established:
            self.delayed_greeting.append(packet)
            self.client_ready_event.set()  # Tell agent to connect, as an initial greeting is ready
        else:
            await super().produce(packet)

    async def handle_session_termination(self):
        await super().handle_session_termination()
        try:
            file_path = Helper.get_transcript_file_path(self.session_id)
            if os.path.exists(file_path):
                self.evaluator.check_entry(self.session_id, self.entry, self.environment)
            else:
                logging.warning(f"Transcript file not found for session {self.session_id}, skipping evaluation")
        except Exception as e:
            logging.error(f"Error during session termination for {self.session_id}: {str(e)}")


class AgentParticipant(BaseParticipant):
    def __init__(
        self,
        session_id: str,
        entry,
        config,
        environment,
        ws_host: str = "localhost",
        ws_port: int = 6789,
    ):
        super().__init__(
            session_id=session_id,
            entry=entry,
            config=config,
            participant_type="agent",
            environment=environment,
            ws_host=ws_host,
            ws_port=ws_port,
        )

    async def produce(self, packet: UnifiedPacket):
        if packet.event == EventType.RESPONSE_FUNCTION_CALL_RESULT:
            packet.hash = Helper.get_data_hash(Helper.apply_mask(self.communicator.provider.functions_data, self.environment.get("filter_schema")))

        await super().produce(packet)
