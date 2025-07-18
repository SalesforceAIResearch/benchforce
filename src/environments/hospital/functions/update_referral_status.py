import json
from typing import Any, Dict
from src.classes.function import Function


class UpdateReferralStatus(Function):
    @staticmethod
    def apply(data: Dict[str, Any], patient_identifier: str, referred_to_doctor_identifier: str, new_status: str) -> str:
        patients = data.get('patients', {})
        doctors = data.get('doctors', {})
        referrals = data.get('referrals', {})
        
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
        
        # Resolve referred-to doctor by ID or name
        referred_to_doctor_id = None
        referred_to_doctor_data = None
        
        # Try direct ID lookup first
        if referred_to_doctor_identifier in doctors:
            referred_to_doctor_id = referred_to_doctor_identifier
            referred_to_doctor_data = doctors[referred_to_doctor_identifier]
        else:
            # Try name lookup (case-insensitive, handle "Dr." prefix)
            doctor_identifier_lower = referred_to_doctor_identifier.lower()
            for did, ddata in doctors.items():
                doctor_name = ddata.get('name', '').lower()
                
                # Exact match
                if doctor_name == doctor_identifier_lower:
                    referred_to_doctor_id = did
                    referred_to_doctor_data = ddata
                    break
                
                # Match: stored="dr. sarah johnson", input="sarah johnson"
                if doctor_name.startswith('dr. ') and doctor_name[4:] == doctor_identifier_lower:
                    referred_to_doctor_id = did
                    referred_to_doctor_data = ddata
                    break
                
                # Match: input="dr. sarah johnson", stored could be "sarah johnson"
                if doctor_identifier_lower.startswith('dr. '):
                    identifier_without_dr = doctor_identifier_lower[4:]
                    if doctor_name == identifier_without_dr:
                        referred_to_doctor_id = did
                        referred_to_doctor_data = ddata
                        break
        
        if not referred_to_doctor_data:
            return f"Error: Doctor '{referred_to_doctor_identifier}' not found"
        
        # Find the referral matching patient and referred-to doctor
        matching_referral = None
        matching_referral_id = None
        
        for ref_id, referral in referrals.items():
            if (referral.get('patient_id') == patient_id and 
                referral.get('referred_to_doctor_id') == referred_to_doctor_id):
                matching_referral = referral
                matching_referral_id = ref_id
                break
        
        if not matching_referral:
            return f"Error: No referral found for patient '{patient_data.get('name')}' to doctor '{referred_to_doctor_data.get('name')}'"
        
        # Validate status
        valid_statuses = ["pending", "scheduled", "completed", "cancelled"]
        if new_status not in valid_statuses:
            return f"Error: Status must be one of: {', '.join(valid_statuses)}"
        
        # Check if status change is valid
        current_status = matching_referral.get('status')
        if current_status == new_status:
            return f"Error: Referral is already {new_status}"
        
        # Prevent invalid status transitions
        if current_status == "completed" and new_status != "completed":
            return "Error: Cannot change status of a completed referral"
        
        if current_status == "cancelled" and new_status not in ["cancelled"]:
            return "Error: Cannot change status of a cancelled referral"
        
        # Update referral status
        old_status = matching_referral['status']
        matching_referral['status'] = new_status
        
        return json.dumps({
            "message": f"Referral status updated successfully from '{old_status}' to '{new_status}'",
            "referral_id": matching_referral_id,
            "patient_name": patient_data.get('name'),
            "referred_to_doctor_name": referred_to_doctor_data.get('name'),
            "old_status": old_status,
            "new_status": new_status,
            "referral": matching_referral
        })
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_referral_status",
                "description": "Updates the status of an existing referral.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "patient_identifier": {
                            "type": "string",
                            "description": "Patient ID (e.g., 'P2003') or patient name (e.g., 'Maria Rodriguez')."
                        },
                        "referred_to_doctor_identifier": {
                            "type": "string",
                            "description": "Doctor ID (e.g., 'D1009') or doctor name (e.g., 'Dr. William Davis') that the patient was referred to."
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New status: 'pending', 'scheduled', 'completed', or 'cancelled'."
                        }
                    },
                    "required": ["patient_identifier", "referred_to_doctor_identifier", "new_status"]
                }
            }
        }