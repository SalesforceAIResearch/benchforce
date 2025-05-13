import json
from typing import Any, Dict
from src.classes.function import Function


class RateLead(Function):
    @staticmethod
    def apply(data: Dict[str, Any], lead_id: str, rating: int) -> str:
        rating = int(rating)
        leads = data.get('leads', {})
        if lead_id not in leads:
            return "Error: lead not found"
        if rating < 1 or rating > 5:
            return "Error: rating must be between 1 and 5"
        leads[lead_id]["lead_rating"] = rating
        return json.dumps({"message": "Lead rated", "lead": leads[lead_id]})
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "rate_lead",
                "description": "Rates a lead on a scale from 1 to 5.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "lead_id": {"type": "string", "description": "The unique identifier of the lead."},
                        "rating": {"type": "integer", "description": "Rating between 1 and 5."}
                    },
                    "required": ["lead_id", "rating"]
                }
            }
        }
