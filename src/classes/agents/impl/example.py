from src.classes.agents.core.agent import Agent, AgentConfig, AgentResponse


class ExampleAgent(Agent):
    """Minimal example agent - always responds with the same message."""

    AGENT_CONFIG = AgentConfig(
        type="example",
        description="Simple text agent for demonstration purposes",
        log_name="ExampleAgent",
        log_icon="🥳",
        supports_voice=False,
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

    async def initialize(self) -> None:
        """Initialize the agent"""
        pass

    async def process_message(self, user_input: str) -> AgentResponse:
        """Always return the same response"""
        environment = self.config.environment if self.config and hasattr(self.config, "environment") else "unknown"
        return AgentResponse(text=f"I'm {self.name}. I'm in the '{environment}' environment, and all I ask is for you to tell me more!")
    
    async def close(self) -> None:
        """Clean up resources"""
        pass
