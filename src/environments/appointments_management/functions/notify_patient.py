import json
from typing import Any, Dict
from src.classes.function import Function


class NotifyPatient(Function):
    @staticmethod
    def apply(data: Dict[str, Any], confirmation_code: str, message: str) -> str:
        appointments = data.get('appointments', {})
        if confirmation_code not in appointments:
            return "Error: appointment not found"
        appointments[confirmation_code]["notes"] = message
        return json.dumps({"message": "Patient notified", "notification": message})
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "notify_patient",
                "description": "Sends a notification message to the patient for an appointment.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "confirmation_code": {"type": "string", "description": "The appointment confirmation code."},
                        "message": {"type": "string", "description": "Notification message to the patient."}
                    },
                    "required": ["confirmation_code", "message"]
                }
            }
        }