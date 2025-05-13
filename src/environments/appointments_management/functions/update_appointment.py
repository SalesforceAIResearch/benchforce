import json
from typing import Any, Dict
from src.classes.function import Function


class UpdateAppointment(Function):
    @staticmethod
    def apply(
        data: Dict[str, Any],
        confirmation_code: str,
        appointment_date: str = "",
        appointment_time: str = "",
        status: str = "",
        doctor_name: str = "",
        department: str = "",
        clinic: str = "",
        reason: str = "",
        notes: str = ""
    ) -> str:
        appointments = data.get('appointments', {})
        if confirmation_code not in appointments:
            return "Error: appointment not found"
        appointment = appointments[confirmation_code]
        if appointment_date: appointment["appointment_date"] = appointment_date
        if appointment_time: appointment["appointment_time"] = appointment_time
        if status: appointment["status"] = status
        if doctor_name:
            doctors = data.get('doctors', [])
            doctor_id = None
            for doctor in doctors:
                if doctor.get("name") == doctor_name:
                    doctor_id = doctor.get("doctor_id")
                    break
            if doctor_id is None:
                return f"Error: doctor '{doctor_name}' not found"
            appointment["doctor_id"] = doctor_id
        if department: appointment["department"] = department
        if clinic: appointment["clinic"] = clinic
        if reason: appointment["reason"] = reason
        if notes: appointment["notes"] = notes
        return json.dumps({"message": "Appointment updated", "appointment": appointment})
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_appointment",
                "description": "Modifies specific fields of a healthcare appointment. Use doctor_name to change the doctor (lookup is performed).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "confirmation_code": {"type": "string", "description": "The appointment confirmation code."},
                        "appointment_date": {"type": "string", "description": "New appointment date (optional)."},
                        "appointment_time": {"type": "string", "description": "New appointment time (optional)."},
                        "status": {"type": "string", "description": "New status (optional)."},
                        "doctor_name": {"type": "string", "description": "New doctor name (optional)."},
                        "department": {"type": "string", "description": "New department (optional)."},
                        "clinic": {"type": "string", "description": "New clinic name (optional)."},
                        "reason": {"type": "string", "description": "New reason (optional)."},
                        "notes": {"type": "string", "description": "New notes (optional)."}
                    },
                    "required": ["confirmation_code"]
                }
            }
        }