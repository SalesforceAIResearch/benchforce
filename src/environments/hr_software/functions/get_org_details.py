# Copyright Sierra

import json
from typing import Any, Dict
from src.classes.function import Function


class GetOrgDetails(Function):
    @staticmethod
    def apply(data: Dict[str, Any], org_id: str) -> str:
        orgs = data["organizations"]
        if org_id in orgs:
            return json.dumps(orgs[org_id])
        return json.dumps({"error": "Organization not found"})

    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_org_details",
                "description": "Get the details of an organization including contact info, subscription, and settings.",
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