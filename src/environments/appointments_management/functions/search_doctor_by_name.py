import json
from typing import Any, Dict
from src.classes.function import Function

class SearchDoctorByName(Function):
    @staticmethod
    def apply(data: Dict[str, Any], doctor_name: str) -> str:
        doctors = data.get('doctors', [])
        for doctor in doctors:
            if doctor.get("name") == doctor_name:
                return json.dumps(doctor)
        return f"Error: doctor '{doctor_name}' not found"
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_doctor_by_name",
                "description": "Searches for a doctor by name and returns their details.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "doctor_name": {"type": "string", "description": "The full name of the doctor."}
                    },
                    "required": ["doctor_name"]
                }
            }
        }