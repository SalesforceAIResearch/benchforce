# Copyright Sierra

import json
from typing import Any, Dict
from src.classes.function import Function


class ModifyUserStatus(Function):
    @staticmethod
    def apply(data: Dict[str, Any], user_id: str, new_status: str, org_id: str) -> str:
        orgs = data["organizations"]
        users = data["users"]
        
        if org_id not in orgs:
            return json.dumps({"error": "Organization not found"})
        
        if user_id not in users:
            return json.dumps({"error": "User not found"})
            
        user = users[user_id]
        if user["org_id"] != org_id:
            return json.dumps({"error": "User does not belong to the specified organization"})
            
        valid_statuses = ["active", "pending", "suspended", "terminated", "locked"]
        if new_status not in valid_statuses:
            return json.dumps({"error": f"Invalid status. Must be one of: {', '.join(valid_statuses)}"})
            
        user["status"] = new_status
        return json.dumps({"success": True, "message": f"User status updated to {new_status}"})

    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "modify_user_status",
                "description": "Modify a user's status (active, pending, suspended, terminated, or locked).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user ID in format USR-XXXXX.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status (active, pending, suspended, terminated, or locked).",
                        },
                        "org_id": {
                            "type": "string",
                            "description": "The organization ID in format ORG-XXXXX.",
                        },
                    },
                    "required": ["user_id", "new_status", "org_id"],
                },
            },
        } 