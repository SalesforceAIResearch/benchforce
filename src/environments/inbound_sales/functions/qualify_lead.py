import json
from typing import Any, Dict
from src.classes.function import Function


class QualifyLead(Function):
    @staticmethod
    def apply(data: Dict[str, Any], lead_id: str, qualification_score: int) -> str:
        qualification_score = int(qualification_score)
        leads = data.get('leads', {})
        if lead_id not in leads:
            return "Error: lead not found"
        lead = leads[lead_id]
        lead["qualification_score"] = qualification_score
        lead["status"] = "qualified" if qualification_score >= 70 else "needs review"
        return json.dumps({"message": "Lead qualified", "lead": lead})
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "qualify_lead",
                "description": "Assigns a qualification score to a lead and updates its status accordingly.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "lead_id": {"type": "string", "description": "The unique identifier of the lead."},
                        "qualification_score": {"type": "integer", "description": "Score (0-100) indicating lead quality."}
                    },
                    "required": ["lead_id", "qualification_score"]
                }
            }
        }