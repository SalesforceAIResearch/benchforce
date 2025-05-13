import json
from typing import Any, Dict
from src.classes.function import Function


class TransferLead(Function):
    @staticmethod
    def apply(data: Dict[str, Any], lead_id: str, new_rep_name: str) -> str:
        leads = data.get('leads', {})
        sales_reps = data.get('sales_reps', [])
        if lead_id not in leads:
            return "Error: lead not found"
        rep_id = None
        for rep in sales_reps:
            if rep.get("name") == new_rep_name:
                rep_id = rep.get("rep_id")
                break
        if rep_id is None:
            return f"Error: sales representative '{new_rep_name}' not found"
        leads[lead_id]["assigned_rep"] = rep_id
        return json.dumps({"message": "Lead transferred", "lead": leads[lead_id]})
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "transfer_lead",
                "description": "Transfers a lead from its current representative to a new one.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "lead_id": {"type": "string", "description": "The unique identifier of the lead."},
                        "new_rep_name": {"type": "string", "description": "The full name of the new sales representative."}
                    },
                    "required": ["lead_id", "new_rep_name"]
                }
            }
        }