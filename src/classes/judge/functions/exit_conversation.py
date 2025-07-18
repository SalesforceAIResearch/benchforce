from typing import Any, Dict
from src.classes.function import Function
from textwrap import dedent


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
                "description": dedent("""
                    Ends the current conversation session.
                    This function should be called when the conversation is finished, and the requester has confirmed that they no longer need assistance.
                    The conversation is finished when the request is either resolved or cannot be resolved, or if there is nothing more to say.
                """),
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                },
            },
        }