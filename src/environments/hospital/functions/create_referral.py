import json
from typing import Any, Dict
from src.classes.function import Function
from datetime import datetime


class CreateReferral(Function):
    @staticmethod
    def apply(data: Dict[str, Any], patient_identifier: str, referring_doctor_identifier: str, referred_to_doctor_identifier: str, referred_to_department: str, priority: str = "routine") -> str:
        patients = data.get('patients', {})
        doctors = data.get('doctors', {})
        referrals = data.get('referrals', {})
        
        # Resolve patient by ID or name
        patient_id = None
        patient_data = None
        
        if patient_identifier in patients:
            patient_id = patient_identifier
            patient_data = patients[patient_identifier]
        else:
            patient_identifier_lower = patient_identifier.lower()
            for pid, pdata in patients.items():
                if pdata.get('name', '').lower() == patient_identifier_lower:
                    patient_id = pid
                    patient_data = pdata
                    break
        
        if not patient_data:
            return f"Error: Patient '{patient_identifier}' not found"
        
        # Resolve referring doctor by ID or name
        referring_doctor_id = None
        referring_doctor_data = None
        
        if referring_doctor_identifier in doctors:
            referring_doctor_id = referring_doctor_identifier
            referring_doctor_data = doctors[referring_doctor_identifier]
        else:
            referring_doctor_identifier_lower = referring_doctor_identifier.lower()
            for did, ddata in doctors.items():
                doctor_name = ddata.get('name', '').lower()
                if (doctor_name == referring_doctor_identifier_lower or
                    (doctor_name.startswith('dr. ') and doctor_name[4:] == referring_doctor_identifier_lower) or
                    (referring_doctor_identifier_lower.startswith('dr. ') and doctor_name == referring_doctor_identifier_lower[4:])):
                    referring_doctor_id = did
                    referring_doctor_data = ddata
                    break
        
        if not referring_doctor_data:
            return f"Error: Referring doctor '{referring_doctor_identifier}' not found"
        
        # Resolve referred-to doctor by ID or name
        referred_to_doctor_id = None
        referred_to_doctor_data = None
        
        if referred_to_doctor_identifier in doctors:
            referred_to_doctor_id = referred_to_doctor_identifier
            referred_to_doctor_data = doctors[referred_to_doctor_identifier]
        else:
            referred_to_doctor_identifier_lower = referred_to_doctor_identifier.lower()
            for did, ddata in doctors.items():
                doctor_name = ddata.get('name', '').lower()
                if (doctor_name == referred_to_doctor_identifier_lower or
                    (doctor_name.startswith('dr. ') and doctor_name[4:] == referred_to_doctor_identifier_lower) or
                    (referred_to_doctor_identifier_lower.startswith('dr. ') and doctor_name == referred_to_doctor_identifier_lower[4:])):
                    referred_to_doctor_id = did
                    referred_to_doctor_data = ddata
                    break
        
        if not referred_to_doctor_data:
            return f"Error: Referred-to doctor '{referred_to_doctor_identifier}' not found"
        
        # Validate referred-to doctor is in correct department
        if referred_to_doctor_data.get('department') != referred_to_department:
            return f"Error: Dr. {referred_to_doctor_data.get('name')} is not in {referred_to_department} department"
        
        # Validate priority
        valid_priorities = ["urgent", "routine", "stat"]
        if priority not in valid_priorities:
            return f"Error: Priority must be one of: {', '.join(valid_priorities)}"
        
        # Generate new referral ID
        existing_ids = list(referrals.keys())
        if existing_ids:
            numbers = [int(rid[1:]) for rid in existing_ids if rid.startswith('R') and rid[1:].isdigit()]
            new_id = f"R{max(numbers) + 1}" if numbers else "R6001"
        else:
            new_id = "R6001"
        
        # Get current date
        referral_date = datetime.now().strftime("%Y-%m-%d")
        
        # Create referral
        referral = {
            "referral_id": new_id,
            "patient_id": patient_id,
            "referring_doctor_id": referring_doctor_id,
            "referred_to_doctor_id": referred_to_doctor_id,
            "referring_department": referring_doctor_data.get('department'),
            "referred_to_department": referred_to_department,
            "referral_date": referral_date,
            "status": "pending",
            "priority": priority
        }
        
        # Add to referrals
        referrals[new_id] = referral
        
        return json.dumps({
            "message": "Referral created successfully",
            "referral": referral
        })
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_referral",
                "description": "Creates a new referral from one doctor to another specialist.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "patient_identifier": {
                            "type": "string",
                            "description": "Patient ID (e.g., 'P2001') or patient name (e.g., 'Alice Johnson')."
                        },
                        "referring_doctor_identifier": {
                            "type": "string",
                            "description": "Doctor ID (e.g., 'D1001') or doctor name (e.g., 'Dr. John Adams' or 'John Adams')."
                        },
                        "referred_to_doctor_identifier": {
                            "type": "string",
                            "description": "Doctor ID (e.g., 'D1002') or doctor name (e.g., 'Dr. Sarah Johnson' or 'Sarah Johnson')."
                        },
                        "referred_to_department": {
                            "type": "string",
                            "description": "Department of the specialist (e.g., 'Cardiology', 'Neurology')."
                        },
                        "priority": {
                            "type": "string",
                            "description": "Priority level: 'urgent', 'routine', or 'stat'. Defaults to 'routine'."
                        }
                    },
                    "required": ["patient_identifier", "referring_doctor_identifier", "referred_to_doctor_identifier", "referred_to_department"]
                }
            }
        }