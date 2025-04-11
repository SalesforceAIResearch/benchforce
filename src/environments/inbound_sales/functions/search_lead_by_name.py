import json
from typing import Any, Dict
from src.classes.function import Function

class SearchLeadByName(Function):
    @staticmethod
    def apply(data: Dict[str, Any], name: str) -> str:
        leads = data.get('leads', {})
        for lead in leads.values():
            if lead.get("name") == name:
                return json.dumps(lead)
        return f"Error: lead '{name}' not found"
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_lead_by_name",
                "description": "Searches for a lead by full name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "Full name of the lead."}
                    },
                    "required": ["name"]
                }
            }
        }