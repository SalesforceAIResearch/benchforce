import json
from typing import Any, Dict
from src.classes.function import Function

class ListSalesReps(Function):
    @staticmethod
    def apply(data: Dict[str, Any]) -> str:
        sales_reps = data.get('sales_reps', {})
        return json.dumps(sales_reps)
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_sales_reps",
                "description": "Lists all available sales representatives.",
                "parameters": {"type": "object", "properties": {}}
            }
        }