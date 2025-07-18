import json
from typing import Any, Dict
from src.classes.function import Function


class ReturnOrder(Function):
    @staticmethod
    def apply(data: Dict[str, Any], order_id: str, return_reason: str) -> str:
        orders = data.get('orders', {})
        if order_id not in orders:
            return "Error: order not found"
        order = orders[order_id]
        order["return_requested"] = True
        order["return_reason"] = return_reason
        return json.dumps({"message": "Return process initiated", "order": order})
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "return_order",
                "description": "Initiates the return process for an order, providing a reason for return.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The unique order ID to return."},
                        "return_reason": {"type": "string", "description": "The reason for returning the order."}
                    },
                    "required": ["order_id", "return_reason"]
                }
            }
        }
