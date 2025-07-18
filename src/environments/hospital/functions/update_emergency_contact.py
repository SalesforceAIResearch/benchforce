import json
from typing import Any, Dict
from src.classes.function import Function


class UpdateEmergencyContact(Function):
    @staticmethod
    def apply(data: Dict[str, Any], patient_identifier: str, contact_name: str, contact_phone: str) -> str:
        patients = data.get('patients', {})
        
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
        
        patients[patient_id]['emergency_contact'] = contact_name
        patients[patient_id]['emergency_phone'] = contact_phone
        
        return json.dumps({
            "message": "Emergency contact updated successfully",
            "patient_id": patient_id,
            "patient_name": patient_data.get('name'),
            "emergency_contact": contact_name,
            "emergency_phone": contact_phone
        })
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_emergency_contact",
                "description": "Updates the emergency contact information for a patient.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "patient_identifier": {
                            "type": "string",
                            "description": "Patient ID (e.g., 'P2001') or patient name (e.g., 'Robert Wilson')."
                        },
                        "contact_name": {
                            "type": "string",
                            "description": "Name of the emergency contact person."
                        },
                        "contact_phone": {
                            "type": "string",
                            "description": "Phone number of the emergency contact person."
                        }
                    },
                    "required": ["patient_identifier", "contact_name", "contact_phone"]
                }
            }
        }