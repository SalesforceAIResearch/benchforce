import json
from typing import Any, Dict
from src.classes.function import Function

class ListAppointments(Function):
    @staticmethod
    def apply(data: Dict[str, Any]) -> str:
        appointments = data.get('appointments', {})
        return json.dumps(list(appointments.values()))
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_appointments",
                "description": "Lists all scheduled healthcare appointments.",
                "parameters": {"type": "object", "properties": {}}
            }
        }