from typing import Callable, Awaitable
from abc import ABC, abstractmethod

from src.classes.helper import Helper
from src.classes.provider import Provider
from src.classes.packet import UnifiedPacket, EventType

import base64


class Communicator(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def set_is_async(self, is_async: bool):
        pass

    @abstractmethod
    async def connect(self):
        pass

    @abstractmethod
    def set_consumer(self, consumer: Callable[[UnifiedPacket], Awaitable[None]]):
        pass

    @abstractmethod
    async def produce(self, packet: UnifiedPacket):
        pass

    @abstractmethod
    async def consume(self, packet: UnifiedPacket):
        pass


class RealtimeCommunicator(Communicator):
    def __init__(self, entry, config, participant_instance, environment):
        self.is_async = False
        self.participant = participant_instance
        self.provider = Provider()
        self.agent = self.provider.get_agent(entry=entry, config=config, participant_instance=participant_instance, type='realtime', environment=environment, agent_instance=self)

    def set_is_async(self, is_async: bool):
        self.is_async = is_async

    async def connect(self):
        await self.agent.connect()
    
    async def produce(self, packet: UnifiedPacket):
        if packet.event in (EventType.RESPONSE_AUDIO_DONE, EventType.RESPONSE_AUDIO_DONE) and hasattr(self.participant, "noise_mixer"):
            audio_data = packet.audio if packet.event == EventType.RESPONSE_AUDIO_DONE else packet.audio_delta

            audio_data = base64.b64decode(audio_data)
            audio_data = self.participant.noise_mixer.apply(audio_data)
            audio_data = base64.b64encode(bytes(audio_data)).decode("utf-8")

            setattr(packet, "audio" if packet.event == EventType.RESPONSE_AUDIO_DONE else "audio_delta", audio_data)

        await self.participant.produce(packet)

    async def consume(self, packet: UnifiedPacket):
        await self.model_consumer(packet)

    def set_consumer(self, consumer):
        self.model_consumer = consumer


class MultimodalCommunicator(Communicator):
    def __init__(self, entry, config, participant_instance, environment):
        self.is_async = False
        self.participant = participant_instance
        self.modalities = Helper.get_modalities(type=participant_instance.type, client_mode=config.client_mode, agent_mode=config.agent_mode)

        self.provider = Provider()
        self.agent = self.provider.get_agent(entry=entry, config=config, participant_instance=participant_instance, type='text', environment=environment, agent_instance=self)
        self.tts_model = self.provider.get_tts(config, participant_instance.type)
        self.stt_model = self.provider.get_stt(config, participant_instance.type)

    async def connect(self):
        await self.agent.connect()

    def tts(self, query: str):
        audio_data = self.tts_model.process(query)

        if self.participant.type == "client" and self.participant.noise_mixer:
            audio_data = self.participant.noise_mixer.apply(audio_data)

        return base64.b64encode(bytes(audio_data)).decode("utf-8")

    def tts_stream(self, query: str):
        audio_chunks = self.tts_model.process_stream(query)

        for chunk in audio_chunks:
            if self.participant.type == "client" and self.participant.noise_mixer:
                chunk = self.participant.noise_mixer.apply(chunk)

            yield base64.b64encode(chunk)

    def stt(self, audio_data):
        transcript = self.stt_model.process_audio(base64.b64decode(audio_data))

        return transcript

    async def produce(self, packet: UnifiedPacket):
        if self.modalities == ["text"] or packet.event != EventType.RESPONSE_TEXT_DONE:
            await self.participant.produce(packet)
        else:
            if self.is_async:
                async for chunk in self.tts(packet.text):
                    voice_packet = UnifiedPacket(
                        event=EventType.RESPONSE_AUDIO_DELTA,
                        audio=base64.b64encode(chunk).decode("utf-8"),
                    )
                    await self.participant.produce(voice_packet)

                transcript_packet = UnifiedPacket(
                    event=EventType.RESPONSE_AUDIO_TRANSCRIPT_DONE,
                    text=packet.text,
                )

                log_tts_packet = UnifiedPacket(
                    event=EventType.RESPONSE_LOG_TTS,
                    text=packet.text,
                )

                await self.participant.produce(log_tts_packet)
                await self.participant.produce(transcript_packet)

                await self.participant.produce(UnifiedPacket(
                    event=EventType.RESPONSE_DONE
                ))
            else:
                voice_packet_payload = self.tts(packet.text)
                voice_packet = UnifiedPacket(
                    event=EventType.RESPONSE_AUDIO_DONE,
                    audio=voice_packet_payload,
                )

                transcript_packet = UnifiedPacket(
                    event=EventType.RESPONSE_AUDIO_TRANSCRIPT_DONE,
                    text=packet.text,
                )

                log_tts_packet = UnifiedPacket(
                    event=EventType.RESPONSE_LOG_TTS,
                    text=packet.text,
                )

                await self.participant.produce(log_tts_packet)
                await self.participant.produce(voice_packet)
                await self.participant.produce(transcript_packet)

    async def consume(self, packet: UnifiedPacket):
        if self.modalities == ["text"] or packet.event != EventType.RESPONSE_AUDIO_DONE:
            await self.model_consumer(packet)
        else:
            transcript = self.stt(packet.audio)

            log_stt_packet = UnifiedPacket(
                event=EventType.RESPONSE_LOG_STT,
                text=transcript,
            )

            text_packet = UnifiedPacket(
                event=EventType.RESPONSE_TEXT_DONE,
                text=transcript,
            )
            await self.participant.produce(log_stt_packet)

            await self.model_consumer(text_packet)

    def set_consumer(self, consumer):
        self.model_consumer = consumer

    def set_is_async(self, is_async: bool):
        pass


def build_communicator(entry, config, participant_instance, environment):
    current_mode = config.agent_mode if participant_instance.type == "agent" else config.client_mode

    realtime_modes = {"realtime-text", "realtime-voice", "realtime-multimodal"}
    multimodal_modes = {"text", "voice", "text-voice-multimodal"}

    if current_mode in realtime_modes:
        return RealtimeCommunicator(entry=entry, config=config, participant_instance=participant_instance, environment=environment)
    elif current_mode in multimodal_modes:
        return MultimodalCommunicator(entry=entry, config=config, participant_instance=participant_instance, environment=environment)
    else:
        raise ValueError(f"Unknown mode: {current_mode}")
