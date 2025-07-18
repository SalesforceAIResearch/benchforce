import json
from typing import Any, Dict
from src.classes.function import Function


class GetAppointment(Function):
    @staticmethod
    def apply(data: Dict[str, Any], patient_identifier: str) -> str:
        patients = data.get('patients', {})
        appointments = data.get('appointments', {})
        
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
        
        # Find the appointment matching the given criteria
        target_appointment = None
        appointment_id = None
        
        for appt_id, appt in appointments.items():
            if (appt.get('patient_id') == patient_id and
                appt.get('status') == 'scheduled'):
                target_appointment = appt
                appointment_id = appt_id
                break

        if not target_appointment:
            return f"Error: No appointment found for patient '{patient_identifier}'"
        
        return json.dumps({
            "appointment_id": appointment_id,
            "patient_id": patient_id,
            "patient_name": patient_data.get('name'),
            "doctor_id": target_appointment.get('doctor_id'),
            "doctor_name": target_appointment.get('doctor_name'),
        })
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_appointment",
                "description": "Retrieves the appointment details for a patient.",
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
        
    
