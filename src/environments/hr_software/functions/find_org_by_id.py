# Copyright Sierra

import json
from typing import Any, Dict
from src.classes.function import Function


class FindOrgById(Function):
    @staticmethod
    def apply(data: Dict[str, Any], org_id: str) -> str:
        orgs = data["organizations"]
        if org_id in orgs:
            return json.dumps({"found": True, "org_id": org_id})
        return json.dumps({"found": False, "error": "Organization not found"})

    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_org_by_id",
                "description": "Find an organization by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "org_id": {
                            "type": "string",
                            "description": "The organization ID in format ORG-XXXXX.",
                        },
                    },
                    "required": ["org_id"],
                },
            },
        } 