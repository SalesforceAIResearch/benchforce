# Copyright Sierra

import json
from typing import Any, Dict
from src.classes.function import Function


class TransferToHumanAgents(Function):
    @staticmethod
    def apply(data: Dict[str, Any], reason: str) -> str:
        return json.dumps({
            "message": "Transferring to human agent",
            "reason": reason,
            "status": "transferred"
        })

    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "transfer_to_human_agents",
                "description": "Transfer the conversation to a human agent when the request cannot be handled within the scope of available actions.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reason": {
                            "type": "string",
                            "description": "The reason for transferring to a human agent.",
                        },
                    },
                    "required": ["reason"],
                },
            },
        } 