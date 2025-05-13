import json
from typing import Any, Dict
from src.classes.function import Function

class CreateAppointment(Function):
    @staticmethod
    def apply(
        data: Dict[str, Any],
        confirmation_code: str,
        appointment_id: str,
        patient_name: str,
        doctor_name: str,
        appointment_date: str,
        appointment_time: str,
        status: str,
        department: str,
        clinic: str,
        reason: str,
        notes: str = ""
    ) -> str:
        patients = data.get('patients', [])
        doctors = data.get('doctors', [])
        patient_id = None
        doctor_id = None

        for patient in patients:
            if patient.get("name") == patient_name:
                patient_id = patient.get("patient_id")
                break
        if patient_id is None:
            return f"Error: patient '{patient_name}' not found"

        for doctor in doctors:
            if doctor.get("name") == doctor_name:
                doctor_id = doctor.get("doctor_id")
                break
        if doctor_id is None:
            return f"Error: doctor '{doctor_name}' not found"

        appointments = data.get('appointments', {})
        if confirmation_code in appointments:
            return "Error: appointment already exists"

        appointment = {
            "confirmation_code": confirmation_code,
            "appointment_id": appointment_id,
            "patient_id": patient_id,
            "doctor_id": doctor_id,
            "appointment_date": appointment_date,
            "appointment_time": appointment_time,
            "status": status,
            "department": department,
            "clinic": clinic,
            "reason": reason,
            "notes": notes
        }
        appointments[confirmation_code] = appointment
        data['appointments'] = appointments
        return json.dumps({"message": "Appointment scheduled", "appointment": appointment})
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_appointment",
                "description": "Schedules a new healthcare appointment using patient and doctor names.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "confirmation_code": {"type": "string", "description": "Unique confirmation code (e.g., 'HC12345')."},
                        "appointment_id": {"type": "string", "description": "Unique appointment identifier."},
                        "patient_name": {"type": "string", "description": "Name of the patient."},
                        "doctor_name": {"type": "string", "description": "Name of the doctor."},
                        "appointment_date": {"type": "string", "description": "Date of the appointment (ISO format)."},
                        "appointment_time": {"type": "string", "description": "Time of the appointment (HH:MM)."},
                        "status": {"type": "string", "description": "Status (e.g., pending, confirmed)."},
                        "department": {"type": "string", "description": "Department (e.g., Cardiology)."},
                        "clinic": {"type": "string", "description": "Clinic location or name."},
                        "reason": {"type": "string", "description": "Reason for the appointment."},
                        "notes": {"type": "string", "description": "Additional notes (optional)."}
                    },
                    "required": ["confirmation_code", "appointment_id", "patient_name", "doctor_name", "appointment_date", "appointment_time", "status", "department", "clinic", "reason"]
                }
            }
        }