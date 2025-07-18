import json
from typing import Any, Dict
from src.classes.function import Function


class UpdateBillingAddress(Function):
    @staticmethod
    def apply(data: Dict[str, Any], order_id: str, new_billing_address: str) -> str:
        orders = data.get('orders', {})
        if order_id not in orders:
            return "Error: order not found"
        orders[order_id]["billing_address"] = new_billing_address
        return json.dumps({"message": "Billing address updated", "order": orders[order_id]})
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_billing_address",
                "description": "Updates the billing address for a specific order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The unique order ID."},
                        "new_billing_address": {"type": "string", "description": "The new billing address."}
                    },
                    "required": ["order_id", "new_billing_address"]
                }
            }
        }
