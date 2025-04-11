from src.classes.providers.openai import OpenAIRealtime, OpenAIText
from src.classes.providers.google import GoogleRealtime, GoogleText
from src.classes.providers.anthropic import AnthropicText
from src.classes.providers.x import XAIText
from src.classes.providers.openai_compatible import OpenAICompatibleText
from src.classes.providers.togetherai import TogetherAIText
from src.classes.providers.cartesia import CartesiaTTS
from src.classes.providers.deepgram import DeepgramSTT

from src.classes.helper import Helper

from abc import ABC, abstractmethod
from enum import Enum

import copy

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

class GoogleTextProvider(BaseProvider):
    def get_agent(self, modalities, instructions, functions, functions_handler, base_model, agent_instance, **kwargs):
        return GoogleText(modalities, instructions, functions, functions_handler, base_model, agent_instance)

class GoogleRealtimeProvider(BaseProvider):
    def get_agent(self, modalities, instructions, functions, functions_handler, base_model, agent_instance, **kwargs):
        return GoogleRealtime(modalities, instructions, functions, functions_handler, base_model, agent_instance)
    
class AnthropicProvider(BaseProvider):
    def get_agent(self, modalities, instructions, functions, functions_handler, base_model, agent_instance, **kwargs):
        return AnthropicText(modalities, instructions, functions, functions_handler, base_model, agent_instance)

class XAIProvider(BaseProvider):
    def get_agent(self, modalities, instructions, functions, functions_handler, base_model, agent_instance, **kwargs):
        return XAIText(modalities, instructions, functions, functions_handler, base_model, agent_instance)

class OpenAICompatibleTextProvider(BaseProvider):
    def get_agent(self, modalities, instructions, functions, functions_handler, base_model, agent_instance, **kwargs):
        return OpenAICompatibleText(modalities, instructions, functions, functions_handler, base_model, agent_instance)

class TogetherAITextProvider(BaseProvider):
    def get_agent(self, modalities, instructions, functions, functions_handler, base_model, agent_instance, **kwargs):
        return TogetherAIText(modalities, instructions, functions, functions_handler, base_model, agent_instance)
    
class CartesiaProvider(BaseProvider):
    def get_agent(self, model, tts_clean_model, sample_rate, voice):
        return CartesiaTTS(model, tts_clean_model, sample_rate, voice)
    
class DeepgramProvider(BaseProvider):
    def get_agent(self, model):
        return DeepgramSTT(model)
    

class ModelProvider(Enum):
    OPENAI = "openai"
    OPENAI_COMPATIBLE = "openai_compatible"
    ANTHROPIC = "anthropic"
    GOOGLE = "google"
    X = "x"
    CARTESIA = "cartesia"
    DEEPGRAM = "deepgram"
    TOGETHERAI = "together"


MODEL_PROVIDER_MAP = {
    "gpt-4o": ModelProvider.OPENAI,
    "gpt-4o-realtime-preview": ModelProvider.OPENAI,
    "gpt-4o-mini": ModelProvider.OPENAI,
    "gpt-4.5-preview": ModelProvider.OPENAI,
    "claude-3-7-sonnet-20250219": ModelProvider.ANTHROPIC,
    "claude-3-5-sonnet-20241022": ModelProvider.ANTHROPIC,
    "gemini-2.0-flash-exp": ModelProvider.GOOGLE,
    "gemini-2.0-flash-001": ModelProvider.GOOGLE,
    "gemini-2.0-flash-live-001": ModelProvider.GOOGLE,
    "gemini-2.5-pro-preview-03-25": ModelProvider.GOOGLE,
    "sonic": ModelProvider.CARTESIA,
    "nova-3": ModelProvider.DEEPGRAM,
    "grok-2-1212": ModelProvider.X,
    "grok-2-latest": ModelProvider.X,
    "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8": ModelProvider.TOGETHERAI,
    "meta-llama/Llama-4-Scout-17B-16E-Instruct": ModelProvider.TOGETHERAI,
}

PROVIDER_FACTORY = {
    ModelProvider.OPENAI: {
        'text': OpenAITextProvider,
        'realtime': OpenAIRealtimeProvider,
    },
    ModelProvider.GOOGLE: {
        'text': GoogleTextProvider,
        'realtime': GoogleRealtimeProvider,
    },
    ModelProvider.ANTHROPIC: {
        'text': AnthropicProvider
    },
    ModelProvider.X: {
        'text': XAIProvider
    },
    ModelProvider.OPENAI_COMPATIBLE: {
        'text': OpenAICompatibleTextProvider
    },
    ModelProvider.TOGETHERAI: {
        'text': TogetherAITextProvider
    },
    ModelProvider.CARTESIA: CartesiaProvider,
    ModelProvider.DEEPGRAM: DeepgramProvider,
}

class Provider():
    def __init__(self):
        pass


    def get_instructions(self, type, environment, entry):
        return (environment if type == "agent" else entry).get("instructions")
    
    def get_functions(self, type, environment):
        if type == "agent":
            return environment.get("functions")
        return {}
    
    def get_functions_data(self, type, environment):
        if type == "agent":
            return environment.get("data")
        return {}

    async def functions_handler(self, function_name, **kwargs):
        if function_name == 'exit_conversation':
            await self.participant_instance.terminate_session()

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
            voice = None
        else:
            raise ValueError(f"Unknown type: {type}")

        is_openai_compatible = config.client_openai_compatible_chat_model if participant_instance.type == "client" else config.agent_openai_compatible_chat_model

        if is_openai_compatible:
            provider_class = PROVIDER_FACTORY.get(ModelProvider.OPENAI_COMPATIBLE, {}).get(type)
        
        else:
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
        clean_base_model = config.client_tts_clean_model if participant_type == "client" else config.agent_tts_clean_model
        voice = config.client_tts_voice if participant_type == "client" else config.agent_tts_voice
        sample_rate = config.sample_rate 

        provider_enum = MODEL_PROVIDER_MAP.get(base_model)
        if provider_enum is None:
            raise ValueError(f"Provider for model {base_model} is not implemented")
        
        provider_class = PROVIDER_FACTORY.get(provider_enum, {})
        if provider_class is None:
            raise ValueError(f"Provider for {provider_enum.value} is not implemented")
        
        provider_instance = provider_class()
        return provider_instance.get_agent(base_model, clean_base_model, sample_rate, voice)  
      
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

