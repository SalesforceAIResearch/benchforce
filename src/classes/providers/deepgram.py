import os
import json
import httpx
from pydub import AudioSegment
import io

from deepgram import (
    DeepgramClient,
    DeepgramClientOptions,
    PrerecordedOptions,
    FileSource,
)

from deepgram.utils import verboselogs


class DeepgramSTT:
    def __init__(self, base_model):
        config: DeepgramClientOptions = DeepgramClientOptions(
            verbose=verboselogs.ERROR,
        )
        self.client: DeepgramClient = DeepgramClient(api_key=os.getenv("DEEPGRAM_API_KEY"), config=config)
        self.base_model = base_model

    def normalize_audio(self, audio_bytes, sample_rate=24000, channels=1, sample_width=2):
        if audio_bytes[:4] != b"RIFF":
            audio = AudioSegment(
                data=audio_bytes,
                sample_width=sample_width,
                frame_rate=sample_rate,
                channels=channels
            )
        else:
            audio_stream = io.BytesIO(audio_bytes)
            try:
                audio = AudioSegment.from_file(audio_stream)
            except Exception as e:
                raise

            audio = audio.set_channels(channels).set_frame_rate(sample_rate)

        buffer = io.BytesIO()
        audio.export(buffer, format="wav")
        normalized_bytes = buffer.getvalue()
        
        return normalized_bytes

    def process_audio(self, audio_data):
        payload: FileSource = {
            "buffer": self.normalize_audio(audio_data),
        }
        options: PrerecordedOptions = PrerecordedOptions(
            model=self.base_model,
            smart_format=True,
            utterances=True,
            punctuate=True,
            diarize=True,
        )

        response = self.client.listen.rest.v("1").transcribe_file(
            payload, options, timeout=httpx.Timeout(300.0, connect=10.0)
        )

    
        transcript = json.loads(response.to_json())['results']['channels'][0]['alternatives'][0]['transcript']
        return transcript

