import json
from typing import Any, Dict
from src.classes.function import Function


class GetPatientReferrals(Function):
    @staticmethod
    def apply(data: Dict[str, Any], patient_identifier: str) -> str:
        patients = data.get('patients', {})
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
        
        # Find all referrals for this patient
        patient_referrals = [referral for referral in referrals.values() if referral.get('patient_id') == patient_id]
        
        if not patient_referrals:
            return json.dumps({
                "message": f"No referrals found for patient '{patient_data.get('name')}'",
                "patient_id": patient_id,
                "patient_name": patient_data.get('name'),
                "referrals": []
            })
        
        # Sort by referral date (most recent first)
        patient_referrals.sort(key=lambda x: x.get('referral_date', ''), reverse=True)
        
        return json.dumps({
            "patient_id": patient_id,
            "patient_name": patient_data.get('name'),
            "total_referrals": len(patient_referrals),
            "referrals": patient_referrals
        })
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_patient_referrals",
                "description": "Retrieves all referrals for a specific patient, sorted by date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "patient_identifier": {
                            "type": "string",
                            "description": "Patient ID (e.g., 'P2001') or patient name (e.g., 'Emily Davis')."
                        }
                    },
                    "required": ["patient_identifier"]
                }
            }
        }