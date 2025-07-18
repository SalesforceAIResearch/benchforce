import json
from typing import Any, Dict
from src.classes.function import Function


class CancelAppointment(Function):
    @staticmethod
    def apply(data: Dict[str, Any], patient_identifier: str, doctor_identifier: str, appointment_date: str, appointment_time: str) -> str:
        patients = data.get('patients', {})
        doctors = data.get('doctors', {})
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
        
        # Resolve doctor by ID or name
        doctor_id = None
        doctor_data = None
        
        # Try direct ID lookup first
        if doctor_identifier in doctors:
            doctor_id = doctor_identifier
            doctor_data = doctors[doctor_identifier]
        else:
            # Try name lookup (case-insensitive, handle "Dr." prefix)
            doctor_identifier_lower = doctor_identifier.lower()
            for did, ddata in doctors.items():
                doctor_name = ddata.get('name', '').lower()
                
                # Exact match
                if doctor_name == doctor_identifier_lower:
                    doctor_id = did
                    doctor_data = ddata
                    break
                
                # Match: stored="dr. sarah johnson", input="sarah johnson"
                if doctor_name.startswith('dr. ') and doctor_name[4:] == doctor_identifier_lower:
                    doctor_id = did
                    doctor_data = ddata
                    break
                
                # Match: input="dr. sarah johnson", stored could be "sarah johnson"
                if doctor_identifier_lower.startswith('dr. '):
                    identifier_without_dr = doctor_identifier_lower[4:]
                    if doctor_name == identifier_without_dr:
                        doctor_id = did
                        doctor_data = ddata
                        break
        
        if not doctor_data:
            return f"Error: Doctor '{doctor_identifier}' not found"
        
        # Find the appointment matching the given criteria
        target_appointment = None
        appointment_id = None
        
        for appt_id, appt in appointments.items():
            if (appt.get('patient_id') == patient_id and
                appt.get('doctor_id') == doctor_id and
                appt.get('appointment_date') == appointment_date and
                appt.get('appointment_time') == appointment_time):
                target_appointment = appt
                appointment_id = appt_id
                break
        
        # Check if appointment exists
        if not target_appointment:
            return f"Error: Appointment not found for {patient_data.get('name')} with {doctor_data.get('name')} on {appointment_date} at {appointment_time}"
        
        # Check if appointment is already cancelled
        if target_appointment.get('status') == 'cancelled':
            return "Error: Appointment is already cancelled"
        
        # Check if appointment is completed
        if target_appointment.get('status') == 'completed':
            return "Error: Cannot cancel a completed appointment"
        
        # Cancel the appointment
        target_appointment['status'] = 'cancelled'
        
        return json.dumps({
            "message": "Appointment cancelled successfully",
            "appointment_id": appointment_id,
            "patient_id": patient_id,
            "patient_name": patient_data.get('name'),
            "doctor_id": doctor_id,
            "doctor_name": doctor_data.get('name'),
            "appointment_date": appointment_date,
            "appointment_time": appointment_time,
            "status": "cancelled"
        })
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "cancel_appointment",
                "description": "Cancels an existing appointment based on patient, doctor, date and time.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "patient_identifier": {
                            "type": "string",
                            "description": "Patient ID (e.g., 'P2001') or patient name (e.g., 'John Smith')."
                        },
                        "doctor_identifier": {
                            "type": "string",
                            "description": "Doctor ID (e.g., 'D1001') or doctor name (e.g., 'Dr. Sarah Johnson' or 'Sarah Johnson')."
                        },
                        "appointment_date": {
                            "type": "string",
                            "description": "Date of the appointment to cancel (e.g., '2024-01-15')."
                        },
                        "appointment_time": {
                            "type": "string",
                            "description": "Time of the appointment to cancel (e.g., '10:00 AM')."
                        }
                    },
                    "required": ["patient_identifier", "doctor_identifier", "appointment_date", "appointment_time"]
                }
            }
        }