import json
from typing import Any, Dict
from src.classes.function import Function


class GetAppointment(Function):
    @staticmethod
    def apply(data: Dict[str, Any], confirmation_code: str) -> str:
        appointments = data.get('appointments', {})
        if confirmation_code not in appointments:
            return "Error: appointment not found"
        return json.dumps(appointments[confirmation_code])
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_appointment",
                "description": "Returns a healthcare appointment by confirmation code.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "confirmation_code": {
                            "type": "string",
                            "description": "The confirmation code for the appointment (e.g., 'HC12345')."
                        }
                    },
                    "required": ["confirmation_code"]
                }
            }
        }
