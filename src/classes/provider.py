from src.classes.providers.openai import OpenAIRealtime, OpenAIText
from src.classes.providers.elevenlabs import ElevenlabsTTS
from src.classes.providers.deepgram import DeepgramSTT

from src.classes.helper import Helper

from src.classes.judge.functions import JUDGE_FUNCTIONS_MAP
from src.classes.judge.system_prompt_wrapper import system_prompt_wrapper

from abc import ABC, abstractmethod
from enum import Enum

import copy
import pdb

class BaseProvider(ABC):
    @abstractmethod
    def get_agent(self, modalities, instructions, functions, functions_handler, base_model, agent_instance, **kwargs):
        pass


class OpenAITextProvider(BaseProvider):
    def get_agent(self, modalities, instructions, functions, functions_handler, base_model, agent_instance, **kwargs):
        return OpenAIText(modalities, instructions, functions, functions_handler, base_model, agent_instance)


class OpenAIRealtimeProvider(BaseProvider):
    def get_agent(self, modalities, instructions, functions, functions_handler, base_model, agent_instance, **kwargs):
        voice = kwargs.get("voice", None)
        return OpenAIRealtime(modalities, instructions, functions, functions_handler, base_model, agent_instance, voice)
    

class ElevenlabsProvider(BaseProvider):
    def get_agent(self, model, sample_rate, voice):
        return ElevenlabsTTS(model, sample_rate, voice)
    

class DeepgramProvider(BaseProvider):
    def get_agent(self, model):
        return DeepgramSTT(model)
    

class ModelProvider(Enum):
    OPENAI = "openai"
    ELEVENLABS = "elevenlabs"
    DEEPGRAM = "deepgram"
    TOGETHERAI = "together"
    EXAMPLE = "example"


MODEL_PROVIDER_MAP = {
    "gpt-4.1": ModelProvider.OPENAI,
    "gpt-4.1-nano": ModelProvider.OPENAI,
    "gpt-4.1-mini": ModelProvider.OPENAI,
    "gpt-4o": ModelProvider.OPENAI,
    "gpt-4o-realtime-preview": ModelProvider.OPENAI,
    "gpt-4o-mini": ModelProvider.OPENAI,
    "gpt-4.5-preview": ModelProvider.OPENAI,
    "eleven_multilingual_v2": ModelProvider.ELEVENLABS,
    "eleven_turbo_v2_5": ModelProvider.ELEVENLABS,
    "nova-3": ModelProvider.DEEPGRAM,
}

PROVIDER_FACTORY = {
    ModelProvider.OPENAI: {
        'text': OpenAITextProvider,
        'realtime': OpenAIRealtimeProvider,
    },
    ModelProvider.ELEVENLABS: ElevenlabsProvider,
    ModelProvider.DEEPGRAM: DeepgramProvider,
}


class Provider():
    def __init__(self):
        pass

    def set_environment(self, environment):
        self.environment = environment

    def set_functions_data(self, type):
        self.functions_data = copy.deepcopy(self.get_functions_data(type, self.environment))

    def get_instructions(self, type, environment, entry):
        prompt = (environment if type == "agent" else entry).get("instructions")

        if not (hasattr(self, 'participant_instance') and self.participant_instance.with_agent) and type == "client":
            return system_prompt_wrapper.replace("{{AGENDA_PLACEHOLDER}}", prompt)

        return prompt
    
    def get_functions(self, type, environment):
        if type == "agent":
            return environment.get("functions")
        elif not self.participant_instance.with_agent:
            return JUDGE_FUNCTIONS_MAP
        return {}
    
    def get_functions_data(self, type, environment):
        if type == "agent":
            return environment.get("data")
        return {}

    async def functions_handler(self, function_name, **kwargs):
        if function_name == 'exit_conversation':
            await self.participant_instance.terminate_session()

        function_class = self.environment.get('functions')[function_name] if self.participant_instance.with_agent or self.participant_instance.type == "agent" else JUDGE_FUNCTIONS_MAP[function_name]
        function_instance = function_class()
        return function_instance.apply(self.functions_data, **kwargs)

    async def agent_functions_handler(self, function_name, **kwargs):
        function_class = self.environment.get('functions')[function_name]
        function_instance = function_class()
        return function_instance.apply(self.functions_data, **kwargs)

    def get_agent(self, entry, config, participant_instance, type, environment, agent_instance):
        self.type = type
        self.environment = environment
        self.participant_instance = participant_instance
        self.functions_data = copy.deepcopy(self.get_functions_data(participant_instance.type, environment))
    
        if type == 'realtime':
            base_model = config.client_realtime_model if participant_instance.type == "client" else config.agent_realtime_model
            voice = config.client_realtime_voice if participant_instance.type == "client" else config.agent_realtime_voice
        elif type == 'text':
            base_model = config.client_chat_model if participant_instance.type == "client" else config.agent_chat_model
            #pdb.set_trace()
            print(f"CLIENT MODEL TEXT: {base_model}")
            voice = None
        else:
            raise ValueError(f"Unknown type: {type}")

        provider_enum = MODEL_PROVIDER_MAP.get(base_model)
        if provider_enum is None:
            raise ValueError(f"Provider for model {base_model} is not implemented")
            
        provider_class = PROVIDER_FACTORY.get(provider_enum, {}).get(type)

        if provider_class is None:
            raise ValueError(f"Provider for {provider_enum.value} with type {type} is not implemented")
        
        modalities = Helper.get_modalities(participant_instance.type, config.client_mode, config.agent_mode)
        instructions = self.get_instructions(participant_instance.type, environment, entry)
        functions = self.get_functions(participant_instance.type, environment)

        provider_instance = provider_class()
        return provider_instance.get_agent(modalities=modalities, instructions=instructions, functions=functions, functions_handler=self.functions_handler, base_model=base_model, agent_instance=agent_instance, voice=voice)
    
    def get_tts(self, config, participant_type):
        base_model = config.client_tts_model if participant_type == "client" else config.agent_tts_model
        voice = config.client_tts_voice if participant_type == "client" else config.agent_tts_voice
        sample_rate = config.sample_rate

        provider_enum = MODEL_PROVIDER_MAP.get(base_model)
        if provider_enum is None:
            raise ValueError(f"Provider for model {base_model} is not implemented")
        
        provider_class = PROVIDER_FACTORY.get(provider_enum, {})
        if provider_class is None:
            raise ValueError(f"Provider for {provider_enum.value} is not implemented")
        
        provider_instance = provider_class()
        return provider_instance.get_agent(base_model, sample_rate, voice)
      
    def get_stt(self, config, participant_type):
        base_model = config.client_stt_model if participant_type == "client" else config.agent_stt_model

        provider_enum = MODEL_PROVIDER_MAP.get(base_model)
        if provider_enum is None:
            raise ValueError(f"Provider for model {base_model} is not implemented")
        
        provider_class = PROVIDER_FACTORY.get(provider_enum, {})
        if provider_class is None:
            raise ValueError(f"Provider for {provider_enum.value} is not implemented")
        
        provider_instance = provider_class()
        return provider_instance.get_agent(base_model)
