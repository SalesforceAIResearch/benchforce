import json
from typing import Any, Dict
from src.classes.function import Function

class ListLeads(Function):
    @staticmethod
    def apply(data: Dict[str, Any]) -> str:
        leads = data.get('leads', {})
        return json.dumps(list(leads.values()))
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_leads",
                "description": "Lists all available leads in the system.",
                "parameters": {"type": "object", "properties": {}}
            }
        }