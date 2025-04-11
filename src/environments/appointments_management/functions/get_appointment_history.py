import json
from typing import Any, Dict
from src.classes.function import Function

class GetAppointmentHistory(Function):
    @staticmethod
    def apply(data: Dict[str, Any], patient_name: str) -> str:
        patients = data.get('patients', [])
        patient_id = None
        for patient in patients:
            if patient.get("name") == patient_name:
                patient_id = patient.get("patient_id")
                break
        if patient_id is None:
            return f"Error: patient '{patient_name}' not found"

        history = []
        appointments = data.get('appointments', {})
        for appointment in appointments.values():
            if appointment.get("patient_id") == patient_id:
                history.append(appointment)
        return json.dumps(history)
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_appointment_history",
                "description": "Retrieves the past appointments for a specific patient (lookup by name).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "patient_name": {"type": "string", "description": "The name of the patient."}
                    },
                    "required": ["patient_name"]
                }
            }
        }