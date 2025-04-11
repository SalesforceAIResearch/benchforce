import json
from typing import Any, Dict
from src.classes.function import Function



class FollowUpLead(Function):
    @staticmethod
    def apply(data: Dict[str, Any], lead_id: str, followup_action: str) -> str:
        followups = data.get('followups', {})
        followup_id = f"FUP_{lead_id}"
        followups[followup_id] = {
            "lead_id": lead_id,
            "followup_action": followup_action
        }
        data['followups'] = followups
        return json.dumps({"message": "Follow-up recorded", "followup": followups[followup_id]})
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "follow_up_lead",
                "description": "Records a follow-up action for a lead.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "lead_id": {"type": "string", "description": "The unique identifier of the lead."},
                        "followup_action": {"type": "string", "description": "Description of the follow-up action (e.g., 'send email')."}
                    },
                    "required": ["lead_id", "followup_action"]
                }
            }
        }