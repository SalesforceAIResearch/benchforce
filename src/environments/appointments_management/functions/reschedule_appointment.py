import json
from typing import Any, Dict
from src.classes.function import Function


class RescheduleAppointment(Function):
    @staticmethod
    def apply(data: Dict[str, Any], confirmation_code: str, new_date: str, new_time: str) -> str:
        appointments = data.get('appointments', {})
        if confirmation_code not in appointments:
            return "Error: appointment not found"
        appointments[confirmation_code]["appointment_date"] = new_date
        appointments[confirmation_code]["appointment_time"] = new_time
        return json.dumps({
            "message": "Appointment rescheduled",
            "appointment": appointments[confirmation_code]
        })
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "reschedule_appointment",
                "description": "Reschedules a healthcare appointment with a new date and time.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "confirmation_code": {"type": "string", "description": "The appointment confirmation code."},
                        "new_date": {"type": "string", "description": "New appointment date (ISO format)."},
                        "new_time": {"type": "string", "description": "New appointment time (HH:MM)."}
                    },
                    "required": ["confirmation_code", "new_date", "new_time"]
                }
            }
        }