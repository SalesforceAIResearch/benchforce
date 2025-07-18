from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, Any, List, Optional

from src.classes.utils import make_logger

logger = make_logger(name="Agent")


class ToolCall:
    """Represents a tool call with name and arguments"""
    def __init__(self, name: str, arguments: Dict[str, Any]):
        self.name = name
        self.arguments = arguments
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "tool_name": self.name,
            "tool_args": self.arguments
        }


class AgentResponse:
    """Represents an agent's response to user input"""
    def __init__(self, text: str, tool_calls: Optional[List[ToolCall]] = None):
        self.text = text
        self.tool_calls = tool_calls or []
    
    def has_tools(self) -> bool:
        return len(self.tool_calls) > 0


@dataclass(frozen=True)
class AgentConfig:
    type: str
    description: str = ""

    supports_voice: bool = False
    supports_text: bool = False

    log_name: str = "Agent"
    log_icon: str = "👩‍💼"

    def supports_mode(self, mode: str) -> bool:
        return (
            mode == "voice" and self.supports_voice or
            mode == "text" and self.supports_text
        )


class Agent(ABC):
    """
    Pure agent interface focused only on message processing and response generation.
    All WebSocket and lifecycle management is handled elsewhere.
    """
    
    AGENT_CONFIG = None  # Subclasses should override this

    def __init__(
            self,
            session_id: str,
            config_name: str,
            planner_env: str,
            mode: str,
            config = None,
    ):
        if not self.AGENT_CONFIG.supports_mode(mode):
            raise ValueError(f"Agent {self.AGENT_CONFIG.type} does not support {mode} mode")

        self.session_id = session_id
        self.config_name = config_name
        self.planner_env = planner_env
        self.mode = mode
        self.config = config
        
        logger.debug(f"Initialized agent for session {session_id} in {mode} mode")
    
    @abstractmethod
    async def initialize(self) -> None:
        """
        Initialize the agent (connect to external services, load models, etc.)
        Called once before processing begins.
        """
        pass
    
    @abstractmethod
    async def process_message(self, user_input: str) -> AgentResponse:
        """
        Process a user message and generate a response.
        This is the core method that defines agent behavior.
        
        Args:
            user_input: The user's input text
            
        Returns:
            AgentResponse containing text response and any tool calls
        """
        pass
    
    @abstractmethod
    async def close(self) -> None:
        """
        Clean up agent resources (close connections, save state, etc.)
        Called when the session ends.
        """
        pass
    
    # Optional hooks for specific behaviors
    
    async def pre_process_text(self, text: str) -> str:
        """
        Pre-process text input before main processing.
        Override for text cleaning, normalization, etc.
        """
        return text
    
    async def post_process_text(self, text: str) -> str:
        """
        Post-process text output after main processing.
        Override for text formatting, cleaning, etc.
        """
        return text
    
    async def handle_tool_result(self, tool_call: ToolCall, result: Any) -> None:
        """
        Handle the result of a tool execution.
        Override to update agent state, log results, etc.
        """
        logger.debug(f"Tool {tool_call.name} executed with result: {result}")
    
    def should_terminate(self) -> bool:
        """
        Check if the agent wants to terminate the session.
        Override to implement custom termination logic.
        """
        return False
    
    def get_agent_info(self) -> Dict[str, Any]:
        """
        Get information about this agent instance.
        Used for logging and debugging.
        """
        return {
            "session_id": self.session_id,
            "config_name": self.config_name,
            "planner_env": self.planner_env,
            "mode": self.mode,
            "type": self.__class__.__name__
        }
