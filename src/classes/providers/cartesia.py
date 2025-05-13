import os
from openai import OpenAI
from cartesia import Cartesia

TTS_CLEAN = """You are tasked with normalizing text for a Text-to-Speech (TTS) system. Your job is to take a raw text input
and transform it into a form that a TTS engine can easily process. 

This includes:
1. Expanding abbreviations, acronyms, and contractions.
2. Converting numbers into their word forms.
3. Expanding dates, times, and units of measurement into their spoken equivalents.
4. Handling special characters (such as "$", "#", "*", ">", "<", "\n", "-") and ensuring they are converted into
their words equivalents.
5. Correctly formatting currency, percentage, and other symbols.
6. Preserving proper names and specific phrases but normalizing other text elements.

Here's the text to normalize:
Text: {instruction}
Please output the normalized instruction only without anything else!
"""

class CartesiaTTS:
    def __init__(self, model, tts_clean_model, sample_rate, voice):
        self.client = Cartesia(api_key=os.getenv("CARTESIA_API_KEY"))
        self.clean_client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        self.model = model
        self.tts_clean_model = tts_clean_model
        self.sample_rate = sample_rate
        self.voice = voice

    def clean_query(self, query: str):
        chat_completion = self.clean_client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": TTS_CLEAN.format(instruction=query),
                }
            ],
            model=self.tts_clean_model,
        )
        return chat_completion.choices[0].message.content
        
    def process(self, query: str):
        clean_query = self.clean_query(query=query)
        audio_bytes = self.client.tts.bytes(
            model_id=self.model,
            transcript=clean_query,
            voice_id=self.voice,
            language="en",
            output_format={
                "container": "wav", 
                "sample_rate": self.sample_rate,
                "encoding": "pcm_s16le",
            },
        )

        return audio_bytes