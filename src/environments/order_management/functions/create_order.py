import json
from typing import Any, Dict
from src.classes.function import Function


class CreateOrder(Function):
    @staticmethod
    def apply(
        data: Dict[str, Any],
        order_id: str,
        customer_id: str,
        shipping_address: str,
        billing_address: str,
        items: str,
        order_status: str,
        total_amount: float,
        coupon_code: str = ""
    ) -> str:
        orders = data.get('orders', {})
        if order_id in orders:
            return "Error: order already exists"
        order = {
            "order_id": order_id,
            "customer_id": customer_id,
            "shipping_address": shipping_address,
            "billing_address": billing_address,
            "items": items,
            "order_status": order_status,
            "total_amount": total_amount,
            "coupon_code": coupon_code,
            "tracking_number": "",
            "return_requested": False
        }
        orders[order_id] = order
        data['orders'] = orders
        return json.dumps({"message": "Order created", "order": order})
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_order",
                "description": "Creates a new order with customer and order details.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "Unique order ID (e.g., 'O1001')."},
                        "customer_id": {"type": "string", "description": "Unique customer identifier."},
                        "shipping_address": {"type": "string", "description": "Shipping address for the order."},
                        "billing_address": {"type": "string", "description": "Billing address for the order."},
                        "items": {"type": "string", "description": "Comma-separated list of item SKUs."},
                        "order_status": {"type": "string", "description": "Order status (e.g., 'processing')."},
                        "total_amount": {"type": "number", "description": "Total amount for the order."},
                        "coupon_code": {"type": "string", "description": "Coupon code applied (optional)."}
                    },
                    "required": ["order_id", "customer_id", "shipping_address", "billing_address", "items", "order_status", "total_amount"]
                }
            }
        }
