import os
import time
import backoff
from elevenlabs.client import ElevenLabs, RequestOptions

from src.classes import utils

logger = utils.make_logger(name="ElevenlabsTTS")

MAX_TIME = 120
REQ_TIMEOUT = 30


class ElevenlabsTTS:
    def __init__(self, model, sample_rate, voice):
        self.client = ElevenLabs(
            api_key=os.getenv("ELEVENLABS_API_KEY"),
        )
        self.model = model
        self.sample_rate = sample_rate
        self.voice = voice

    @backoff.on_exception(backoff.expo, exception=Exception, factor=0.1, base=2, max_value=10, max_time=MAX_TIME, logger=logger)
    def process_stream(self, query: str):
        logger.debug("Processing audio stream...")
        start_time = time.time()
        response = self.client.text_to_speech.convert_as_stream(
                text=query,
                voice_id=self.voice,
                model_id=self.model,
                output_format="pcm_" + str(self.sample_rate),
                apply_text_normalization='on',
                request_options=RequestOptions(
                    timeout_in_seconds=REQ_TIMEOUT,
                )
            )
        logger.debug(f"...audio stream processed in {time.time() - start_time:0.3f} seconds.")
        return response
        
    @backoff.on_exception(backoff.expo, exception=Exception, factor=0.1, base=2, max_value=10, max_time=MAX_TIME, logger=logger)
    def process(self, query: str):
        logger.debug("Processing audio...")
        start_time = time.time()
        audio_bytes = b"".join(
            self.client.text_to_speech.convert_as_stream(
                text=query,
                voice_id=self.voice,
                model_id=self.model,
                output_format="pcm_" + str(self.sample_rate),
                apply_text_normalization='on',
                request_options=RequestOptions(
                    timeout_in_seconds=REQ_TIMEOUT,
                )
            )
        )
        logger.debug(f"...audio processed in {time.time() - start_time:0.3f} seconds.")
        return audio_bytes
