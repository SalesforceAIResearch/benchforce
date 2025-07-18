import json
from typing import Any, Dict
from src.classes.function import Function


class GetOrder(Function):
    @staticmethod
    def apply(data: Dict[str, Any], order_id: str) -> str:
        orders = data.get('orders', {})
        if order_id not in orders:
            return "Error: order not found"
        return json.dumps(orders[order_id])
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_order",
                "description": "Retrieves the details of an order by order ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "Unique identifier for the order (e.g., 'O1001')."
                        }
                    },
                    "required": ["order_id"]
                }
            }
        }
