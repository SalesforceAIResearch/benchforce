import json
from typing import Any, Dict
from src.classes.function import Function


class GetLabResults(Function):
    @staticmethod
    def apply(data: Dict[str, Any], patient_identifier: str) -> str:
        patients = data.get('patients', {})
        lab_results = data.get('lab_results', {})
        
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
        
        patient_results = [result for result in lab_results.values() if result.get('patient_id') == patient_id]
        
        if not patient_results:
            return f"Error: No lab results found for patient '{patient_data.get('name')}'"
        
        # Sort by date (most recent first)
        patient_results.sort(key=lambda x: x.get('test_date', ''), reverse=True)
        
        return json.dumps({"patient_id": patient_id, "patient_name": patient_data.get('name'), "lab_results": patient_results})
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_lab_results",
                "description": "Retrieves the laboratory test results for a patient.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "patient_identifier": {
                            "type": "string",
                            "description": "Patient ID (e.g., 'P2001') or patient name (e.g., 'Maria Rodriguez')."
                        }
                    },
                    "required": ["patient_identifier"]
                }
            }
        }