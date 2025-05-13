import json
from typing import Any, Dict
from src.classes.function import Function


class GetLeadHistory(Function):
    @staticmethod
    def apply(data: Dict[str, Any], lead_id: str) -> str:
        history = data.get('lead_history', {}).get(lead_id, [])
        return json.dumps(history)
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_lead_history",
                "description": "Retrieves the activity history for a given lead.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "lead_id": {"type": "string", "description": "The unique identifier of the lead."}
                    },
                    "required": ["lead_id"]
                }
            }
        }