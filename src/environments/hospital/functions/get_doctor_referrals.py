import json
from typing import Any, Dict
from src.classes.function import Function


class GetDoctorReferrals(Function):
    @staticmethod
    def apply(data: Dict[str, Any], doctor_identifier: str, referral_type: str = "all") -> str:
        doctors = data.get('doctors', {})
        referrals = data.get('referrals', {})
        
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
        
        # Validate referral type
        valid_types = ["all", "outgoing", "incoming"]
        if referral_type not in valid_types:
            return f"Error: Referral type must be one of: {', '.join(valid_types)}"
        
        doctor_referrals = []
        
        # Filter referrals based on type
        for referral in referrals.values():
            if referral_type == "all":
                if referral.get('referring_doctor_id') == doctor_id or referral.get('referred_to_doctor_id') == doctor_id:
                    doctor_referrals.append(referral)
            elif referral_type == "outgoing":
                if referral.get('referring_doctor_id') == doctor_id:
                    doctor_referrals.append(referral)
            elif referral_type == "incoming":
                if referral.get('referred_to_doctor_id') == doctor_id:
                    doctor_referrals.append(referral)
        
        if not doctor_referrals:
            return json.dumps({
                "message": f"No {referral_type} referrals found for {doctor_data.get('name')}",
                "doctor_id": doctor_id,
                "doctor_name": doctor_data.get('name'),
                "referral_type": referral_type,
                "referrals": []
            })
        
        # Sort by referral date (most recent first)
        doctor_referrals.sort(key=lambda x: x.get('referral_date', ''), reverse=True)
        
        # Categorize referrals by status for summary
        status_summary = {}
        for referral in doctor_referrals:
            status = referral.get('status', 'unknown')
            status_summary[status] = status_summary.get(status, 0) + 1
        
        return json.dumps({
            "doctor_id": doctor_id,
            "doctor_name": doctor_data.get('name'),
            "referral_type": referral_type,
            "total_referrals": len(doctor_referrals),
            "status_summary": status_summary,
            "referrals": doctor_referrals
        })
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_doctor_referrals",
                "description": "Retrieves referrals for a specific doctor (outgoing referrals made by the doctor, incoming referrals to the doctor, or all).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "doctor_identifier": {
                            "type": "string",
                            "description": "Doctor ID (e.g., 'D1001') or doctor name (e.g., 'Dr. Sarah Johnson' or 'Sarah Johnson')."
                        },
                        "referral_type": {
                            "type": "string",
                            "description": "Type of referrals to retrieve: 'all', 'outgoing' (made by doctor), or 'incoming' (to doctor). Defaults to 'all'."
                        }
                    },
                    "required": ["doctor_identifier"]
                }
            }
        }