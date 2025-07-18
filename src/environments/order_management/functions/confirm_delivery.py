import json
from typing import Any, Dict
from src.classes.function import Function


class ConfirmDelivery(Function):
    @staticmethod
    def apply(data: Dict[str, Any], order_id: str) -> str:
        orders = data.get('orders', {})
        if order_id not in orders:
            return "Error: order not found"
        orders[order_id]["order_status"] = "delivered"
        return json.dumps({"message": "Order delivery confirmed", "order": orders[order_id]})
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "confirm_delivery",
                "description": "Marks an order as delivered.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The unique order ID."}
                    },
                    "required": ["order_id"]
                }
            }
        }
