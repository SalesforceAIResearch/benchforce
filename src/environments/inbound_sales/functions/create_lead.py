import json
from typing import Any, Dict
from src.classes.function import Function

class CreateLead(Function):
    @staticmethod
    def apply(
        data: Dict[str, Any],
        lead_id: str,
        name: str,
        contact_number: str,
        email: str,
        company: str,
        industry: str,
        source: str,
        status: str,
        notes: str = ""
    ) -> str:
        leads = data.get('leads', {})
        if lead_id in leads:
            return "Error: lead already exists"
        lead = {
            "lead_id": lead_id,
            "name": name,
            "contact_number": contact_number,
            "email": email,
            "company": company,
            "industry": industry,
            "source": source,
            "status": status,
            "notes": notes
        }
        leads[lead_id] = lead
        data['leads'] = leads
        return json.dumps({"message": "Lead created", "lead": lead})
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_lead",
                "description": "Creates a new lead with the provided details.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "lead_id": {"type": "string", "description": "Unique lead identifier (e.g., 'L1001')."},
                        "name": {"type": "string", "description": "Full name of the lead."},
                        "contact_number": {"type": "string", "description": "Lead's phone number."},
                        "email": {"type": "string", "description": "Lead's email address."},
                        "company": {"type": "string", "description": "Company name of the lead."},
                        "industry": {"type": "string", "description": "Industry of the company."},
                        "source": {"type": "string", "description": "Source where the lead was generated (e.g., 'website')."},
                        "status": {"type": "string", "description": "Current status of the lead (e.g., 'new')."},
                        "notes": {"type": "string", "description": "Additional notes (optional)."}
                    },
                    "required": ["lead_id", "name", "contact_number", "email", "company", "industry", "source", "status"]
                }
            }
        }