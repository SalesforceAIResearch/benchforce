import json
from typing import Any, Dict
from src.classes.function import Function


class GetLead(Function):
    @staticmethod
    def apply(data: Dict[str, Any], lead_id: str) -> str:
        leads = data.get('leads', {})
        if lead_id not in leads:
            return "Error: lead not found"
        return json.dumps(leads[lead_id])
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_lead",
                "description": "Retrieves a lead by its unique lead ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "lead_id": {
                            "type": "string",
                            "description": "The unique identifier for the lead (e.g., 'L1001')."
                        }
                    },
                    "required": ["lead_id"]
                }
            }
        }