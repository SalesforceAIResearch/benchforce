import os
import json
import time
import backoff
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

from src.classes import utils
from src.classes.constants import AUDIO_SAMPLE_RATE

logger = utils.make_logger(name="DeepgramSTT")

MAX_TIME = 120
REQ_TIMEOUT = 30


class DeepgramSTT:
    def __init__(self, base_model):
        config: DeepgramClientOptions = DeepgramClientOptions(
            verbose=verboselogs.ERROR,
        )
        self.client: DeepgramClient = DeepgramClient(api_key=os.getenv("DEEPGRAM_API_KEY"), config=config)
        self.base_model = base_model

    def normalize_audio(self, audio_bytes, sample_rate=AUDIO_SAMPLE_RATE, channels=1, sample_width=2):
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

    @backoff.on_exception(backoff.expo, exception=Exception, factor=0.1, base=2, max_value=10, max_time=MAX_TIME, logger=logger)
    def process_audio(self, audio_data):
        logger.debug("Processing audio...")
        start_time = time.time()
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
            source=payload,
            options=options,
            timeout=httpx.Timeout(REQ_TIMEOUT),
        )
    
        transcript = json.loads(response.to_json())['results']['channels'][0]['alternatives'][0]['transcript']
        logger.debug(f"...audio processed in {time.time() - start_time:0.3f} seconds.")
        return transcript

