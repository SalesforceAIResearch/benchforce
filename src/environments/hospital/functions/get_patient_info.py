import json
from typing import Any, Dict
from src.classes.function import Function


class GetPatientInfo(Function):
    @staticmethod
    def apply(data: Dict[str, Any], patient_identifier: str) -> str:
        patients = data.get('patients', {})
        
        # Try direct ID lookup first
        patient_info = patients.get(patient_identifier)
        if patient_info:
            return json.dumps(patient_info)
        
        # Try name lookup (case-insensitive)
        patient_identifier_lower = patient_identifier.lower()
        for patient_id, patient_data in patients.items():
            if patient_data.get('name', '').lower() == patient_identifier_lower:
                return json.dumps(patient_data)
        
        return f"Error: Patient '{patient_identifier}' not found"
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_patient_info",
                "description": "Retrieves basic information about a patient.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "patient_identifier": {
                            "type": "string",
                            "description": "Patient ID (e.g., 'P2001') or patient name (e.g., 'John Smith')."
                        }
                    },
                    "required": ["patient_identifier"]
                }
            }
        }