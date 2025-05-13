import json
from typing import Any, Dict
from src.classes.function import Function

class RecordCallOutcome(Function):
    @staticmethod
    def apply(data: Dict[str, Any], lead_id: str, rep_name: str, call_outcome: str) -> str:
        calls = data.get('calls', {})
        call_id = f"CALL_{lead_id}"
        calls[call_id] = {
            "lead_id": lead_id,
            "rep_name": rep_name,
            "call_outcome": call_outcome
        }
        data['calls'] = calls
        return json.dumps({"message": "Call outcome recorded", "call": calls[call_id]})
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "record_call_outcome",
                "description": "Records the outcome of a sales call with a lead.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "lead_id": {"type": "string", "description": "The unique identifier of the lead."},
                        "rep_name": {"type": "string", "description": "Name of the sales representative making the call."},
                        "call_outcome": {"type": "string", "description": "Outcome of the call (e.g., 'interested', 'not interested')."}
                    },
                    "required": ["lead_id", "rep_name", "call_outcome"]
                }
            }
        }