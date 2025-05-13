import json
from typing import Any, Dict
from src.classes.function import Function

class CancelAppointment(Function):
    @staticmethod
    def apply(data: Dict[str, Any], confirmation_code: str) -> str:
        appointments = data.get('appointments', {})
        if confirmation_code not in appointments:
            return "Error: appointment not found"
        appointment = appointments.pop(confirmation_code)
        return json.dumps({"message": "Appointment cancelled", "appointment": appointment})
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "cancel_appointment",
                "description": "Cancels a healthcare appointment using its confirmation code.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "confirmation_code": {"type": "string", "description": "The appointment confirmation code."}
                    },
                    "required": ["confirmation_code"]
                }
            }
        }
