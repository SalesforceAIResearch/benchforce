import json
from typing import Any, Dict
from src.classes.function import Function


class GetPatientMedications(Function):
    @staticmethod
    def apply(data: Dict[str, Any], patient_identifier: str) -> str:
        patients = data.get('patients', {})
        medications = data.get('medications', {})
        
        # Resolve patient by ID or name
        patient_id = None
        patient_data = None
        
        # Try direct ID lookup first
        if patient_identifier in patients:
            patient_id = patient_identifier
            patient_data = patients[patient_identifier]
        else:
            # Try name lookup (case-insensitive)
            patient_identifier_lower = patient_identifier.lower()
            for pid, pdata in patients.items():
                if pdata.get('name', '').lower() == patient_identifier_lower:
                    patient_id = pid
                    patient_data = pdata
                    break
        
        if not patient_data:
            return f"Error: Patient '{patient_identifier}' not found"
        
        patient_medications = [med for med in medications.values() if med.get('patient_id') == patient_id]
        
        if not patient_medications:
            return f"Error: No medications found for patient '{patient_data.get('name')}'"
        
        return json.dumps({"patient_id": patient_id, "patient_name": patient_data.get('name'), "medications": patient_medications})
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_patient_medications",
                "description": "Retrieves the current medication schedule for a patient.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "patient_identifier": {
                            "type": "string",
                            "description": "Patient ID (e.g., 'P2001') or patient name (e.g., 'Robert Wilson')."
                        }
                    },
                    "required": ["patient_identifier"]
                }
            }
        }