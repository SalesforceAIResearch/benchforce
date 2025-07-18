import json
from typing import Any, Dict
from src.classes.function import Function


class RemoveCoupon(Function):
    @staticmethod
    def apply(data: Dict[str, Any], order_id: str) -> str:
        orders = data.get('orders', {})
        if order_id not in orders:
            return "Error: order not found"
        orders[order_id]["coupon_code"] = ""
        return json.dumps({"message": "Coupon removed", "order": orders[order_id]})
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_coupon",
                "description": "Removes the applied coupon code from an order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The unique order ID."}
                    },
                    "required": ["order_id"]
                }
            }
        }
