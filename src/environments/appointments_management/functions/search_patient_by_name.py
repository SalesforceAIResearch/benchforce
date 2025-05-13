import json
from typing import Any, Dict
from src.classes.function import Function

class SearchPatientByName(Function):
    @staticmethod
    def apply(data: Dict[str, Any], patient_name: str) -> str:
        patients = data.get('patients', [])
        for patient in patients:
            if patient.get("name") == patient_name:
                return json.dumps(patient)
        return f"Error: patient '{patient_name}' not found"
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_patient_by_name",
                "description": "Searches for a patient by name and returns their details.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "patient_name": {"type": "string", "description": "The full name of the patient."}
                    },
                    "required": ["patient_name"]
                }
            }
        }