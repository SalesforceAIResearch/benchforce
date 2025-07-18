# Copyright Sierra

import json
from typing import Any, Dict, List
from src.classes.function import Function


class ModifyUserPermissions(Function):
    @staticmethod
    def apply(data: Dict[str, Any], user_id: str, new_permissions: List[str], org_id: str) -> str:
        orgs = data["organizations"]
        users = data["users"]
        
        if org_id not in orgs:
            return json.dumps({"error": "Organization not found"})
        
        if user_id not in users:
            return json.dumps({"error": "User not found"})
            
        user = users[user_id]
        if user["org_id"] != org_id:
            return json.dumps({"error": "User does not belong to the specified organization"})
            
        valid_permissions = {
            "admin", "manage_users", "manage_billing", "manage_security",
            "manage_team", "view_reports", "approve_requests", "view_own_profile",
            "submit_requests", "access_api", "deploy_code", "run_reports",
            "export_data", "manage_documents", "approve_basic_requests"
        }
        
        invalid_permissions = [p for p in new_permissions if p not in valid_permissions]
        if invalid_permissions:
            return json.dumps({
                "error": f"Invalid permissions found: {', '.join(invalid_permissions)}. "
                f"Valid permissions are: {', '.join(sorted(valid_permissions))}"
            })
            
        user["permissions"] = new_permissions
        return json.dumps({
            "success": True, 
            "message": f"User permissions updated to: {', '.join(new_permissions)}"
        })

    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "modify_user_permissions",
                "description": "Modify a user's permissions list. Users can have multiple permissions.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user ID in format USR-XXXXX.",
                        },
                        "org_id": {
                            "type": "string",
                            "description": "The organization ID in format ORG-XXXXX.",
                        },
                        "new_permissions": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of permissions to assign to the user. Valid permissions: admin, manage_users, manage_billing, manage_security, manage_team, view_reports, approve_requests, view_own_profile, submit_requests, access_api, deploy_code, run_reports, export_data, manage_documents, approve_basic_requests",
                        }
                    },
                    "required": ["user_id", "new_permissions", "org_id"],
                },
            },
        }
