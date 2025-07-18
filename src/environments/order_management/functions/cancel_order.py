import json
from typing import Any, Dict
from src.classes.function import Function


class CancelOrder(Function):
    @staticmethod
    def apply(data: Dict[str, Any], order_id: str) -> str:
        orders = data.get('orders', {})
        if order_id not in orders:
            return "Error: order not found"
        order = orders.pop(order_id)
        return json.dumps({"message": "Order cancelled", "order": order})
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "cancel_order",
                "description": "Cancels an existing order by order ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The unique order ID to cancel."}
                    },
                    "required": ["order_id"]
                }
            }
        }
