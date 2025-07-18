import json
from typing import Any, Dict
from src.classes.function import Function


class ScheduleAppointment(Function):
    @staticmethod
    def apply(data: Dict[str, Any], patient_identifier: str, doctor_identifier: str, appointment_time: str, appointment_date: str, department: str) -> str:
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
                
                # Match: stored="dr. sarah johnson", input="dr. sarah johnson" (already handled by exact match)
                # Match: input="dr. sarah johnson", stored could be "sarah johnson" (unlikely but let's handle it)
                if doctor_identifier_lower.startswith('dr. '):
                    identifier_without_dr = doctor_identifier_lower[4:]
                    if doctor_name == identifier_without_dr:
                        doctor_id = did
                        doctor_data = ddata
                        break
        
        if not doctor_data:
            return f"Error: Doctor '{doctor_identifier}' not found"
        
        # Verify doctor is in the correct department
        if doctor_data.get('department') != department:
            return f"Error: Doctor {doctor_data.get('name')} is not in {department} department"
        
        # Check if this exact appointment already exists
        for appt in appointments.values():
            if (appt.get('patient_id') == patient_id and
                appt.get('doctor_id') == doctor_id and
                appt.get('appointment_date') == appointment_date and
                appt.get('appointment_time') == appointment_time and
                appt.get('department') == department and
                appt.get('status') == 'scheduled'):
                return "Error: This appointment is already scheduled"
        
        # Generate new appointment ID
        existing_ids = list(appointments.keys())
        if existing_ids:
            # Extract numbers from IDs and find the max
            numbers = [int(aid[1:]) for aid in existing_ids if aid.startswith('A') and aid[1:].isdigit()]
            new_id = f"A{max(numbers) + 1}" if numbers else "A3001"
        else:
            new_id = "A3001"
        
        # Create appointment
        appointment = {
            "appointment_id": new_id,
            "patient_id": patient_id,
            "doctor_id": doctor_id,
            "appointment_time": appointment_time,
            "appointment_date": appointment_date,
            "department": department,
            "status": "scheduled"
        }
        
        # Add to appointments
        appointments[new_id] = appointment
        
        return json.dumps({"message": "Appointment scheduled successfully", "appointment": appointment})
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "schedule_appointment",
                "description": "Schedules a new appointment for a patient with a specific doctor.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "patient_identifier": {
                            "type": "string",
                            "description": "Patient ID (e.g., 'P2001') or patient name (e.g., 'Emily Davis')."
                        },
                        "doctor_identifier": {
                            "type": "string",
                            "description": "Doctor ID (e.g., 'D1001') or doctor name (e.g., 'Dr. Sarah Johnson' or 'Sarah Johnson')."
                        },
                        "appointment_time": {
                            "type": "string",
                            "description": "Time of the appointment (e.g., '10:00 AM')."
                        },
                        "appointment_date": {
                            "type": "string",
                            "description": "Date of the appointment (e.g., '2024-01-15')."
                        },
                        "department": {
                            "type": "string",
                            "description": "Department where the appointment will take place (e.g., 'Cardiology')."
                        }
                    },
                    "required": ["patient_identifier", "doctor_identifier", "appointment_time", "appointment_date", "department"]
                }
            }
        }