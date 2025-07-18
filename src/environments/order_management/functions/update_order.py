import json
from typing import Any, Dict
from src.classes.function import Function


class UpdateOrder(Function):
    @staticmethod
    def apply(data: Dict[str, Any], order_id: str, order_status: str = "") -> str:
        orders = data.get('orders', {})
        if order_id not in orders:
            return "Error: order not found"
        if order_status:
            orders[order_id]["order_status"] = order_status
        return json.dumps({"message": "Order updated", "order": orders[order_id]})
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_order",
                "description": "Updates miscellaneous order details, such as order status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The unique order ID."},
                        "order_status": {"type": "string", "description": "The new status for the order (optional)."}
                    },
                    "required": ["order_id"]
                }
            }
        }
