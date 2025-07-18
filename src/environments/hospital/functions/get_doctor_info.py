import json
from typing import Any, Dict
from src.classes.function import Function


class GetDoctorInfo(Function):
    @staticmethod
    def apply(data: Dict[str, Any], doctor_identifier: str) -> str:
        doctors = data.get('doctors', {})
        
        # Try direct ID lookup first
        doctor_info = doctors.get(doctor_identifier)
        if doctor_info:
            return json.dumps(doctor_info)
        
        # Try name lookup (case-insensitive, handle "Dr." prefix)
        doctor_identifier_lower = doctor_identifier.lower()
        
        for doctor_id, doctor_data in doctors.items():
            doctor_name = doctor_data.get('name', '').lower()
            
            # Exact match
            if doctor_name == doctor_identifier_lower:
                return json.dumps(doctor_data)
            
            # Match: stored="dr. sarah johnson", input="sarah johnson"
            if doctor_name.startswith('dr. ') and doctor_name[4:] == doctor_identifier_lower:
                return json.dumps(doctor_data)
            
            # Match: input="dr. sarah johnson", stored could be "sarah johnson" (unlikely but handle it)
            if doctor_identifier_lower.startswith('dr. '):
                identifier_without_dr = doctor_identifier_lower[4:]
                if doctor_name == identifier_without_dr:
                    return json.dumps(doctor_data)
        
        return f"Error: Doctor '{doctor_identifier}' not found"
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_doctor_info",
                "description": "Retrieves information about a doctor.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "doctor_identifier": {
                            "type": "string",
                            "description": "Doctor ID (e.g., 'D1001') or doctor name (e.g., 'Dr. Sarah Johnson' or 'Sarah Johnson')."
                        }
                    },
                    "required": ["doctor_identifier"]
                }
            }
        }