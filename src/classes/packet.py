import json
from dataclasses import dataclass
from typing import Optional, Dict, Any
from enum import Enum


class EventType(str, Enum):
    BENCHFORCE_HANDSHAKE = "benchforce.handshake"
    BENCHFORCE_TERMINATE = "benchforce.terminate"
    BENCHFORCE_LOG_ORIG_DB = "benchforce.log_original_db"
    BENCHFORCE_LOG_DRYRUN_DB = "benchforce.log_dryrun_db"
    BENCHFORCE_LOG_TOPIC = "benchforce.log_topic"
    RESPONSE_AUDIO_DELTA = "response.audio.delta"
    RESPONSE_AUDIO_DONE = "response.audio.done"
    RESPONSE_AUDIO_TRANSCRIPT_DONE = "response.audio_transcript.done"
    RESPONSE_TEXT_DONE = "response.text.done"
    RESPONSE_TEXT_DELTA = "response.text.delta"
    RESPONSE_DONE = "response.done"
    RESPONSE_LOG_TTS = "response.log_tts"
    RESPONSE_LOG_SPEECH_STARTED = "response.log_speech_started"
    RESPONSE_LOG_SPEECH_FINISHED = "response.log_speech_finished"
    RESPONSE_LOG_STT = "response.log_stt"
    RESPONSE_FUNCTION_CALL = "response.function_call"
    RESPONSE_FUNCTION_CALL_RESULT = "response.function_call_result"
    RESPONSE_ERROR = "response.error"
    RUNNER_FINAL_RESULT = "runner.final_results"
    RUNNER_ENTRY_STARTED = "runner.entry_started"
    BENCHFORCE_GET_PENDING_SESSIONS = "benchforce.get_pending_session"
    BENCHFORCE_CURRENT_SESSIONS = "benchforce.current_sessions"


@dataclass
class UnifiedPacket:
    event: EventType
    audio_delta: Optional[str] = None
    audio: Optional[str] = None
    text: Optional[str] = None
    text_delta: Optional[str] = None
    function_call: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    config: Optional[Any] = None
    hash: Optional[str] = None
    topic: Optional[str] = None
    tokens: Optional[int] = None

    def to_json(self) -> str:
        return json.dumps(self.__dict__)
