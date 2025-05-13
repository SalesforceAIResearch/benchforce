import json
import os
import logging
import base64
import wave
import time

class ServerLogger:
    def __init__(self, sample_rate, transcript_root="history"):
        self.logger = logging
        self.sample_rate = sample_rate
        self.transcript_root = transcript_root
        os.makedirs(self.transcript_root, exist_ok=True)
        self.session_files = {}
        self.session_audio_buffer = {}

    def info(self, msg):
        self.logger.info(msg)
    
    def warning(self, msg):
        self.logger.warning(msg)
    
    def error(self, msg):
        self.logger.error(msg)
    
    def register_session(self, session_id):
        session_path = os.path.join(self.transcript_root, session_id)
        os.makedirs(session_path, exist_ok=True)
        file_path = os.path.join(session_path, "transcript.jsonl")
        self.session_files[session_id] = open(file_path, "a", encoding="utf-8")
        self.info(f"Session {session_id} registered. Transcript file created.")
    
    def save_packet(self, session_id, message):
        message["timestamp"] = time.time()
        packet_message = json.loads(message.get("message"))
        event = packet_message.get("event")
        if event in ["response.audio.delta", "response.audio.done"]:
            if event == "response.audio.delta":
                audio_data_b64 = packet_message.get("audio_delta")
            else:
                audio_data_b64 = packet_message.get("audio")
            if audio_data_b64:
                try:
                    decoded = base64.b64decode(audio_data_b64)
                except Exception as e:
                    self.error(f"Base64 decode error for session {session_id}: {str(e)}")
                    return
                if session_id not in self.session_audio_buffer:
                    self.session_audio_buffer[session_id] = bytearray()
                self.session_audio_buffer[session_id].extend(decoded)
            return
        file_obj = self.session_files.get(session_id)
        if file_obj:
            file_obj.write(json.dumps(message, ensure_ascii=False) + "\n")
            file_obj.flush()
        else:
            self.error(f"Transcript file for session {session_id} not found. Packet not saved.")
    
    def unregister_session(self, session_id):
        file_obj = self.session_files.get(session_id)
        if file_obj:
            file_obj.close()
            del self.session_files[session_id]
            self.info(f"Session {session_id} ended. Transcript file closed.")
        audio_buffer = self.session_audio_buffer.get(session_id)
        if audio_buffer and len(audio_buffer) > 0:
            output_path = os.path.join(self.transcript_root, session_id, "output.wav")
            with wave.open(output_path, 'wb') as wf:
                wf.setnchannels(1)
                wf.setsampwidth(2)
                wf.setframerate(self.sample_rate)
                wf.writeframes(audio_buffer)
            self.info(f"Audio file saved for session {session_id} at {output_path}")
            del self.session_audio_buffer[session_id]
        else:
            self.info(f"No audio data for session {session_id}")
