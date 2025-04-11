import json
from typing import Any, Dict
from src.classes.function import Function

class AssignLeadToRep(Function):
    @staticmethod
    def apply(data: Dict[str, Any], lead_id: str, rep_name: str) -> str:
        leads = data.get('leads', {})
        sales_reps = data.get('sales_reps', [])
        if lead_id not in leads:
            return "Error: lead not found"
        rep_id = None
        for rep in sales_reps:
            if rep.get("name") == rep_name:
                rep_id = rep.get("rep_id")
                break
        if rep_id is None:
            return f"Error: sales representative '{rep_name}' not found"
        leads[lead_id]["assigned_rep"] = rep_id
        return json.dumps({"message": "Lead assigned to rep", "lead": leads[lead_id]})
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        # Uses rep_name to assign lead.
        return {
            "type": "function",
            "function": {
                "name": "assign_lead_to_rep",
                "description": "Assigns a lead to a sales representative by name (looked up internally).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "lead_id": {"type": "string", "description": "The unique identifier of the lead."},
                        "rep_name": {"type": "string", "description": "The full name of the sales representative."}
                    },
                    "required": ["lead_id", "rep_name"]
                }
            }
        }