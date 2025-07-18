import json
from typing import Any, Dict
from src.classes.function import Function


class ApplyCoupon(Function):
    @staticmethod
    def apply(data: Dict[str, Any], order_id: str, coupon_code: str) -> str:
        orders = data.get('orders', {})
        if order_id not in orders:
            return "Error: order not found"
        orders[order_id]["coupon_code"] = coupon_code
        return json.dumps({"message": "Coupon applied", "order": orders[order_id]})
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "apply_coupon",
                "description": "Applies a coupon code to the specified order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The unique order ID."},
                        "coupon_code": {"type": "string", "description": "The coupon code to apply."}
                    },
                    "required": ["order_id", "coupon_code"]
                }
            }
        }
