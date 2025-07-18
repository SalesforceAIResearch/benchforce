import json
import os
import base64
import time
import struct

from src.classes import utils

logger = utils.make_logger(name="ServerLogger")


class ServerLogger:

    def __init__(self, sample_rate, transcript_root="history"):
        self.sample_rate = sample_rate
        self.transcript_root = transcript_root
        os.makedirs(self.transcript_root, exist_ok=True)
        self.session_files = {}
        self.session_audio_buffer = {}
        self.session_audio_segments = {}  # Track audio segments with speaker info
        self.session_current_speaker = {}  # Track current speaker per session

    def register_session(self, session_id):
        session_path = os.path.join(self.transcript_root, session_id)
        os.makedirs(session_path, exist_ok=True)
        file_path = os.path.join(session_path, "transcript.jsonl")
        self.session_files[session_id] = open(file_path, "a", encoding="utf-8")
        self.session_audio_segments[session_id] = []
        self.session_current_speaker[session_id] = None
        logger.debug(f"Session {session_id} registered. Transcript file created.")
    
    def save_packet(self, session_id, message):
        message["timestamp"] = time.time()
        packet_message = json.loads(message.get("message"))
        event = packet_message.get("event")
        role = message.get("role", "unknown")
        
        # Handle audio events with speaker role tracking
        if event in ["response.audio.delta", "response.audio.done"]:
            if event == "response.audio.delta":
                audio_data_b64 = packet_message.get("audio_delta")
            else:
                audio_data_b64 = packet_message.get("audio")
                
            if audio_data_b64:
                try:
                    decoded = base64.b64decode(audio_data_b64)
                except Exception as e:
                    logger.error(f"Base64 decode error for session {session_id}: {str(e)}")
                    return
                    
                # Initialize audio buffer if needed
                if session_id not in self.session_audio_buffer:
                    self.session_audio_buffer[session_id] = bytearray()
                
                # Track speaker changes and audio segments
                current_audio_position = len(self.session_audio_buffer[session_id])
                
                # If speaker changed or this is the first audio
                if (self.session_current_speaker[session_id] != role or
                    not self.session_audio_segments[session_id]):
                    
                    # End previous segment if exists
                    if (self.session_audio_segments[session_id] and
                        self.session_current_speaker[session_id] is not None):
                        self.session_audio_segments[session_id][-1]["end_byte"] = current_audio_position
                        self.session_audio_segments[session_id][-1]["duration_seconds"] = (
                            current_audio_position - self.session_audio_segments[session_id][-1]["start_byte"]
                        ) / (self.sample_rate * 2)  # 2 bytes per sample for 16-bit audio
                    
                    # Start new segment
                    segment = {
                        "speaker_role": role,
                        "start_byte": current_audio_position,
                        "start_timestamp": message["timestamp"],
                        "end_byte": None,
                        "duration_seconds": None
                    }
                    self.session_audio_segments[session_id].append(segment)
                    self.session_current_speaker[session_id] = role
                
                # Add audio data to buffer
                self.session_audio_buffer[session_id].extend(decoded)
                
                # If this is audio.done, close the current segment
                if event == "response.audio.done" and self.session_audio_segments[session_id]:
                    final_position = len(self.session_audio_buffer[session_id])
                    self.session_audio_segments[session_id][-1]["end_byte"] = final_position
                    self.session_audio_segments[session_id][-1]["duration_seconds"] = (
                        final_position - self.session_audio_segments[session_id][-1]["start_byte"]
                    ) / (self.sample_rate * 2)
            return
            
        # Save regular transcript messages
        file_obj = self.session_files.get(session_id)
        if file_obj:
            file_obj.write(json.dumps(message, ensure_ascii=False) + "\n")
            file_obj.flush()
        else:
            logger.error(f"Transcript file for session {session_id} not found. Packet not saved.")
    
    def _create_wav_with_metadata(self, file_path, audio_data, segments):
        """Create WAV file with embedded speaker metadata in INFO chunk"""
        # Prepare metadata as JSON string
        metadata = {
            "session_segments": segments,
            "sample_rate": self.sample_rate,
            "total_bytes": len(audio_data)
        }
        metadata_json = json.dumps(metadata, separators=(',', ':'))
        metadata_bytes = metadata_json.encode('utf-8')
        
        # Calculate chunk sizes
        fmt_chunk_size = 16
        data_chunk_size = len(audio_data)
        info_chunk_size = len(metadata_bytes)
        
        # Add padding if info chunk size is odd
        if info_chunk_size % 2 == 1:
            metadata_bytes += b'\x00'
            info_chunk_size += 1
        
        # Calculate total file size
        riff_chunk_size = 4 + (8 + fmt_chunk_size) + (8 + data_chunk_size) + (8 + info_chunk_size)
        
        logger.debug(f"Saving audio file to {file_path}...")
        with open(file_path, 'wb') as f:
            # RIFF header
            f.write(b'RIFF')
            f.write(struct.pack('<L', riff_chunk_size))
            f.write(b'WAVE')
            
            # FORMAT chunk
            f.write(b'fmt ')
            f.write(struct.pack('<L', fmt_chunk_size))
            f.write(struct.pack('<H', 1))  # PCM format
            f.write(struct.pack('<H', 1))  # Mono
            f.write(struct.pack('<L', self.sample_rate))  # Sample rate
            f.write(struct.pack('<L', self.sample_rate * 2))  # Byte rate
            f.write(struct.pack('<H', 2))  # Block align
            f.write(struct.pack('<H', 16))  # Bits per sample
            
            # DATA chunk
            f.write(b'data')
            f.write(struct.pack('<L', data_chunk_size))
            f.write(audio_data)
            
            # INFO chunk with speaker metadata
            f.write(b'LIST')
            f.write(struct.pack('<L', info_chunk_size + 4))
            f.write(b'INFO')
            f.write(b'ISPK')  # Custom fourcc for speaker info
            f.write(struct.pack('<L', len(metadata_bytes)))
            f.write(metadata_bytes)

        logger.debug("Audio file saved.")
    
    def unregister_session(self, session_id):
        file_obj = self.session_files.get(session_id)
        if file_obj:
            file_obj.close()
            del self.session_files[session_id]
            logger.debug(f"Session {session_id} ended. Transcript file closed.")
            
        audio_buffer = self.session_audio_buffer.get(session_id)
        audio_segments = self.session_audio_segments.get(session_id, [])
        
        if audio_buffer and len(audio_buffer) > 0:
            session_path = os.path.join(self.transcript_root, session_id)
            
            # Save audio file with embedded metadata
            output_path = os.path.join(session_path, "output.wav")
            self._create_wav_with_metadata(output_path, audio_buffer, audio_segments)
            
            # Cleanup
            del self.session_audio_buffer[session_id]
            del self.session_audio_segments[session_id]
            del self.session_current_speaker[session_id]
        else:
            logger.warning("No audio data to save.")


def read_wav_metadata(file_path):
    """Utility function to read speaker metadata from WAV file"""
    try:
        with open(file_path, 'rb') as f:
            # Read RIFF header
            riff = f.read(4)
            if riff != b'RIFF':
                return None
            
            file_size = struct.unpack('<L', f.read(4))[0]
            wave_id = f.read(4)
            if wave_id != b'WAVE':
                return None
            
            # Look for INFO chunk
            while f.tell() < file_size + 8:
                try:
                    chunk_id = f.read(4)
                    if len(chunk_id) < 4:
                        break
                    chunk_size = struct.unpack('<L', f.read(4))[0]
                    
                    if chunk_id == b'LIST':
                        list_type = f.read(4)
                        if list_type == b'INFO':
                            # Look for our custom ISPK chunk
                            remaining = chunk_size - 4
                            while remaining > 0:
                                subchunk_id = f.read(4)
                                subchunk_size = struct.unpack('<L', f.read(4))[0]
                                
                                if subchunk_id == b'ISPK':
                                    # Found our speaker metadata
                                    metadata_bytes = f.read(subchunk_size)
                                    metadata_json = metadata_bytes.decode('utf-8').rstrip('\x00')
                                    return json.loads(metadata_json)
                                else:
                                    f.seek(subchunk_size, 1)  # Skip this subchunk
                                
                                remaining -= (8 + subchunk_size)
                                if subchunk_size % 2 == 1:
                                    f.seek(1, 1)  # Skip padding
                                    remaining -= 1
                        else:
                            f.seek(chunk_size - 4, 1)  # Skip this LIST chunk
                    else:
                        f.seek(chunk_size, 1)  # Skip this chunk
                        if chunk_size % 2 == 1:
                            f.seek(1, 1)  # Skip padding
                            
                except struct.error:
                    break
            
        return None
    except Exception as e:
        print(f"Error reading WAV metadata: {e}")
        return None
