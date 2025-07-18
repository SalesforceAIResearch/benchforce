import json
from typing import Any, Dict
from src.classes.function import Function


class GetOrderHistory(Function):
    @staticmethod
    def apply(data: Dict[str, Any], customer_id: str) -> str:
        orders = data.get('orders', {})
        history = [order for order in orders.values() if order.get("customer_id") == customer_id]
        return json.dumps(history)
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_order_history",
                "description": "Retrieves the order history for a specified customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Unique customer identifier."}
                    },
                    "required": ["customer_id"]
                }
            }
        }
