import json
from typing import Any, Dict
from src.classes.function import Function


class RateAppointment(Function):
    @staticmethod
    def apply(data: Dict[str, Any], confirmation_code: str, rating) -> str:
        appointments = data.get('appointments', {})
        if confirmation_code not in appointments:
            return "Error: appointment not found"
        if int(rating) < 1 or int(rating) > 5:
            return "Error: rating must be between 1 and 5"
        appointments[confirmation_code]["rating"] = int(rating)
        return json.dumps({"message": "Appointment rated", "appointment": appointments[confirmation_code]})
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "rate_appointment",
                "description": "Rates a healthcare appointment on a scale of 1 to 5.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "confirmation_code": {"type": "string", "description": "The appointment confirmation code."},
                        "rating": {"type": "integer", "description": "Rating value between 1 and 5."}
                    },
                    "required": ["confirmation_code", "rating"]
                }
            }
        }