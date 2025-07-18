import json
from typing import List
from openai import AsyncOpenAI
import os
import websockets

from src.environments import configs
from src.classes.agents.core.agent import Agent, AgentConfig, AgentResponse, ToolCall
from src.classes.utils import make_logger
from src.classes.provider import Provider
from src.classes.helper import Helper

logger = make_logger(name="OpenAIAgent")


class OpenAIAgent(Agent):
    """
    OpenAI agent with function calling support.
    """

    AGENT_CONFIG = AgentConfig(
        type="openai",
        description="OpenAI agent with function calling support",
        log_name="OpenAIAgent",
        log_icon="👴",
        supports_voice=True,
        supports_text=True,
    )

    def __init__(self, session_id: str, config_name: str, planner_env: str, mode: str, config=None):
        super().__init__(
            session_id=session_id,
            config_name=config_name,
            planner_env=planner_env,
            mode=mode,
            config=config,
        )
        
        self.client = None
        self.model = getattr(self.config, 'agent_chat_model', 'gpt-4.1-mini') if self.config else 'gpt-4.1-mini'
        print(f"AGENT CHAT MODEL: {self.model}")
        self.conversation_history = []
        self.environment = configs.get(self.config.environment)
        self.provider = Provider()
        self.provider.set_environment(self.environment)
        self.provider.set_functions_data("agent")
        self.system_prompt = self.provider.get_instructions("agent", self.environment, None)
        self.functions_data = self.provider.get_functions("agent", self.environment)
        self.functions = Helper.oai_parse_functions(list(self.functions_data.values()))
        self.functions_handler = self.provider.agent_functions_handler
        
    async def initialize(self) -> None:
        """Initialize OpenAI client"""
        try:
            self.client = AsyncOpenAI(api_key= os.getenv('OPENAI_API_KEY', ''))
            
            # Add system message
            self.conversation_history = [{
                "role": "system",
                "content": self.system_prompt
            }]
            
            logger.info("OpenAI client initialized successfully")
            
        except ImportError:
            logger.error("OpenAI package not installed. Install with: pip install openai")
            raise
        except Exception as e:
            logger.error(f"Failed to initialize OpenAI client: {e}")
            raise
    
    async def process_message(self, user_input: str) -> AgentResponse:
        """Process user message through OpenAI with function calling"""
        if not self.client:
            raise RuntimeError("OpenAI client not initialized")
        
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_input
        })
        
        try:
            # Process response recursively to handle multiple function calls
            all_tool_calls = []
            final_response_text = await self._process_response_recursive(all_tool_calls)
            
            return AgentResponse(text=final_response_text or "I processed your request.", tool_calls=all_tool_calls)
            
        except Exception as e:
            logger.error(f"Error processing message with OpenAI: {e}")
            return AgentResponse(text=f"I encountered an error: {str(e)}")
    
    async def _process_response_recursive(self, all_tool_calls: List[ToolCall]) -> str:
        """Recursively process OpenAI responses and handle function calls"""
        # Call OpenAI API
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=self.conversation_history,
            tools=self.functions if self.functions else None,
            tool_choice="auto" if self.functions else None
        )
        
        message = response.choices[0].message
        
        # Handle function calls
        if message.tool_calls:
            # Add assistant message with tool calls to history
            self.conversation_history.append(message)
            
            # Process each tool call
            for tool_call in message.tool_calls:
                function_name = tool_call.function.name
                try:
                    function_args = json.loads(tool_call.function.arguments)
                except json.JSONDecodeError as e:
                    logger.error(f"Error parsing arguments for function {function_name}: {e}")
                    function_args = {}
                
                # Execute the function
                try:
                    function_result = await self.functions_handler(function_name, **function_args)
                except Exception as e:
                    logger.error(f"Error executing function {function_name}: {e}")
                    function_result = f"Error executing function: {str(e)}"
          
                # Add function result to conversation history
                self.conversation_history.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(function_result)
                })
                    
                # Create tool call for our system
                all_tool_calls.append(ToolCall(
                    name=function_name,
                    arguments=function_args
                ))
            
            # Recursively process the response after function execution
            return await self._process_response_recursive(all_tool_calls)
        else:
            # No more function calls, return the final response
            response_text = message.content
            
            # Add final response to history
            if response_text:
                self.conversation_history.append({
                    "role": "assistant",
                    "content": response_text
                })
            
            return response_text
    
    async def close(self) -> None:
        """Clean up resources"""
        if self.client:
            await self.client.close()
        logger.info("OpenAI agent close completed")

    @staticmethod
    async def get_pending_sessions(host: str, port: int):
        async with websockets.connect(f"ws://{host}:{port}") as ws:
            await ws.send(json.dumps({
                "session_id": "system-check",
                "role": "system",
                "message": json.dumps({"event": "benchforce.get_pending_sessions"})
            }))
            response = await ws.recv()
            data = json.loads(response)
            return data.get("data", []) if data.get("status") == "success" else []
