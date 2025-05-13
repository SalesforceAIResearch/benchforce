import json
from typing import Any, Dict
from src.classes.function import Function

class ListDoctors(Function):
    @staticmethod
    def apply(data: Dict[str, Any]) -> str:
        doctors = data.get('doctors', [])
        return json.dumps(doctors)
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_doctors",
                "description": "Lists all doctors available in the system.",
                "parameters": {"type": "object", "properties": {}}
            }
        }