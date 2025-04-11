import json
from typing import Any, Dict
from src.classes.function import Function


class UpdateLead(Function):
    @staticmethod
    def apply(
        data: Dict[str, Any],
        lead_id: str,
        name: str = "",
        contact_number: str = "",
        email: str = "",
        company: str = "",
        industry: str = "",
        source: str = "",
        status: str = "",
        notes: str = ""
    ) -> str:
        leads = data.get('leads', {})
        if lead_id not in leads:
            return "Error: lead not found"
        lead = leads[lead_id]
        if name: lead["name"] = name
        if contact_number: lead["contact_number"] = contact_number
        if email: lead["email"] = email
        if company: lead["company"] = company
        if industry: lead["industry"] = industry
        if source: lead["source"] = source
        if status: lead["status"] = status
        if notes: lead["notes"] = notes
        return json.dumps({"message": "Lead updated", "lead": lead})
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_lead",
                "description": "Updates the information for an existing lead.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "lead_id": {"type": "string", "description": "The unique identifier of the lead."},
                        "name": {"type": "string", "description": "Updated full name (optional)."},
                        "contact_number": {"type": "string", "description": "Updated contact number (optional). Format - (555) 123-4567"},
                        "email": {"type": "string", "description": "Updated email address (optional)."},
                        "company": {"type": "string", "description": "Updated company name (optional)."},
                        "industry": {"type": "string", "description": "Updated industry (optional)."},
                        "source": {"type": "string", "description": "Updated lead source (optional)."},
                        "status": {"type": "string", "description": "Updated lead status (optional)."},
                        "notes": {"type": "string", "description": "Updated notes (optional)."}
                    },
                    "required": ["lead_id"]
                }
            }
        }