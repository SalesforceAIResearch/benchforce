from typing import Any, Dict
from src.classes.function import Function


class ExitConversation(Function):
    @staticmethod
    def apply(data: Any) -> str:
        return ""
        

    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "exit_conversation",
                "description": """Ends the current conversation session. 
This function should be called when the conversation is finished, 
and the user has confirmed that they no longer need assistance.""",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                },
            },
        }
