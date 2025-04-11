import json
from typing import Any, Dict
from src.classes.function import Function

class ListPatients(Function):
    @staticmethod
    def apply(data: Dict[str, Any]) -> str:
        patients = data.get('patients', [])
        return json.dumps(patients)
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_patients",
                "description": "Lists all patients registered in the system.",
                "parameters": {"type": "object", "properties": {}}
            }
        }