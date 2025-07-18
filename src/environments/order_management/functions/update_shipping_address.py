import json
from typing import Any, Dict
from src.classes.function import Function


class UpdateShippingAddress(Function):
    @staticmethod
    def apply(data: Dict[str, Any], order_id: str, new_shipping_address: str) -> str:
        orders = data.get('orders', {})
        if order_id not in orders:
            return "Error: order not found"
        orders[order_id]["shipping_address"] = new_shipping_address
        return json.dumps({"message": "Shipping address updated", "order": orders[order_id]})
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_shipping_address",
                "description": "Updates the shipping address for a given order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The unique order ID."},
                        "new_shipping_address": {"type": "string", "description": "The new shipping address."}
                    },
                    "required": ["order_id", "new_shipping_address"]
                }
            }
        }
