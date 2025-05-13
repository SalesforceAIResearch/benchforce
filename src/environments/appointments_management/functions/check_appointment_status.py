import json
from typing import Any, Dict
from src.classes.function import Function


class CheckAppointmentStatus(Function):
    @staticmethod
    def apply(data: Dict[str, Any], confirmation_code: str) -> str:
        appointments = data.get('appointments', {})
        if confirmation_code not in appointments:
            return "Error: appointment not found"
        status = appointments[confirmation_code].get("status", "pending")
        return json.dumps({"confirmation_code": confirmation_code, "status": status})
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "check_appointment_status",
                "description": "Retrieves the current status of a healthcare appointment.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "confirmation_code": {"type": "string", "description": "The appointment confirmation code."}
                    },
                    "required": ["confirmation_code"]
                }
            }
        }