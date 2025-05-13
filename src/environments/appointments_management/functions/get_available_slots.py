import json
from typing import Any, Dict
from src.classes.function import Function


class GetAvailableSlots(Function):
    @staticmethod
    def apply(data: Dict[str, Any], appointment_date: str) -> str:
        slots = data.get('available_slots', {}).get(appointment_date, [])
        return json.dumps(slots)
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_available_slots",
                "description": "Returns available time slots for appointments on a given date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "appointment_date": {"type": "string", "description": "The date (ISO format) to check available slots."}
                    },
                    "required": ["appointment_date"]
                }
            }
        }