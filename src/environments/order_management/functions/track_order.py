import json
from typing import Any, Dict
from src.classes.function import Function


class TrackOrder(Function):
    @staticmethod
    def apply(data: Dict[str, Any], order_id: str) -> str:
        orders = data.get('orders', {})
        if order_id not in orders:
            return "Error: order not found"
        order = orders[order_id]
        tracking = order.get("tracking_number", "")
        status = order.get("order_status", "unknown")
        return json.dumps({"order_id": order_id, "tracking_number": tracking, "order_status": status})
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "track_order",
                "description": "Returns the tracking information and current status for an order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The unique order ID to track."}
                    },
                    "required": ["order_id"]
                }
            }
        }
