import json
from typing import Any, Dict
from src.classes.function import Function


class FindUserByEmail(Function):
    @staticmethod
    def apply(data: Dict[str, Any], email: str) -> str:
        users = data["users"]
        
        # Search for user with matching email
        for user_id, user in users.items():
            if user["email"].lower() == email.lower():
                return json.dumps({
                    "user_id": user_id,
                    "name": user["name"],
                    "email": user["email"],
                    "department": user["department"],
                    "roles": user["roles"],
                    "org_id": user["org_id"],
                    "status": user["status"]
                })
                
        return json.dumps({
            "error": "No user found with that email address"
        })

    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_user_by_email",
                "description": "Find a user by their email address",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "email": {
                            "type": "string",
                            "description": "Email address of the user to find",
                        }
                    },
                    "required": ["email"],
                },
            },
        }
