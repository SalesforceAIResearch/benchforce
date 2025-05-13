import json
from typing import Any, Dict
from src.classes.function import Function

class ConfirmAppointment(Function):
    @staticmethod
    def apply(data: Dict[str, Any], confirmation_code: str) -> str:
        appointments = data.get('appointments', {})
        if confirmation_code not in appointments:
            return "Error: appointment not found"
        appointments[confirmation_code]["status"] = "confirmed"
        return json.dumps({
            "message": "Appointment confirmed",
            "appointment": appointments[confirmation_code]
        })
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "confirm_appointment",
                "description": "Marks a healthcare appointment as confirmed.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "confirmation_code": {"type": "string", "description": "The appointment confirmation code."}
                    },
                    "required": ["confirmation_code"]
                }
            }
        }