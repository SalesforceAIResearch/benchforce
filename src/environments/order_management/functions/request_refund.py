import json
from typing import Any, Dict
from src.classes.function import Function


class RequestRefund(Function):
    @staticmethod
    def apply(data: Dict[str, Any], order_id: str, refund_reason: str) -> str:
        orders = data.get('orders', {})
        if order_id not in orders:
            return "Error: order not found"
        orders[order_id]["refund_requested"] = True
        orders[order_id]["refund_reason"] = refund_reason
        return json.dumps({"message": "Refund requested", "order": orders[order_id]})
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "request_refund",
                "description": "Initiates a refund request for an order, stating the reason.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The unique order ID."},
                        "refund_reason": {"type": "string", "description": "Reason for the refund request."}
                    },
                    "required": ["order_id", "refund_reason"]
                }
            }
        }
