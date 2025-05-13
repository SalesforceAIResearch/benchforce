import json
from typing import Any, Dict
from src.classes.function import Function


class DisqualifyLead(Function):
    @staticmethod
    def apply(data: Dict[str, Any], lead_id: str, disqualify_reason: str) -> str:
        leads = data.get('leads', {})
        if lead_id not in leads:
            return "Error: lead not found"
        leads[lead_id]["status"] = "disqualified"
        leads[lead_id]["disqualify_reason"] = disqualify_reason
        return json.dumps({"message": "Lead disqualified", "lead": leads[lead_id]})
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "disqualify_lead",
                "description": "Marks a lead as disqualified with a reason.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "lead_id": {"type": "string", "description": "The unique identifier of the lead."},
                        "disqualify_reason": {"type": "string", "description": "Reason for disqualification."}
                    },
                    "required": ["lead_id", "disqualify_reason"]
                }
            }
        }