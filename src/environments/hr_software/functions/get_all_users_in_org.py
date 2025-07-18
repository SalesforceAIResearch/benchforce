import json
from typing import Any, Dict
from src.classes.function import Function


class GetAllUsersInOrg(Function):
    @staticmethod
    def apply(data: Dict[str, Any], org_id: str) -> str:
        users = data["users"]
        
        # Find all users in the specified organization
        org_users = []
        for user_id, user in users.items():
            if user["org_id"] == org_id:
                org_users.append({
                    "id": user_id,
                    "name": user["name"],
                    "email": user["email"],
                    "department": user["department"],
                    "roles": user["roles"],
                    "status": user["status"]
                })
                if len(org_users) >= 3:
                    break
                
        return json.dumps(org_users)

    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_all_users_in_org",
                "description": "Get a list of all users in an organization",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "org_id": {
                            "type": "string", 
                            "description": "The organization ID in format ORG-XXXXX",
                        }
                    },
                    "required": ["org_id"],
                },
            },
        }
