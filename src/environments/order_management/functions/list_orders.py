import json
from typing import Any, Dict
from src.classes.function import Function


class ListOrders(Function):
    @staticmethod
    def apply(data: Dict[str, Any], customer_id: str) -> str:
        orders = data.get('orders', {})
        customer_orders = [order for order in orders.values() if order.get("customer_id") == customer_id]
        return json.dumps(customer_orders)
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_orders",
                "description": "Lists all orders associated with a given customer ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Unique customer identifier."}
                    },
                    "required": ["customer_id"]
                }
            }
        }
