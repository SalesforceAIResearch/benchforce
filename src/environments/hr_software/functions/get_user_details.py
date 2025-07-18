# Copyright Sierra

import json
from typing import Any, Dict
from src.classes.function import Function


class GetUserDetails(Function):
    @staticmethod
    def apply(data: Dict[str, Any], user_id: str) -> str:
        users = data["users"]
        if user_id in users:
            return json.dumps(users[user_id])
        return json.dumps({"error": "User not found"})

    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_details",
                "description": "Get the details of a user including role, department, permissions, and status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user ID in format USR-XXXXX.",
                        },
                    },
                    "required": ["user_id"],
                },
            },
        } 