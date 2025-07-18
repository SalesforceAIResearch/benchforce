filter_schema = {
    "orders": {
        "*": {
            "order_id": True,
            "customer_id": True,
            "shipping_address": True,
            "billing_address": True,
            "items": True,
            "order_status": True,
            "total_amount": True,
            "coupon_code": True,
            "tracking_number": True,
            "return_requested": True,
            "refund_requested": True,
            "created_date": False,
        }
    },
    "customers": {
        "customer_id": True,
        "name": True,
        "email": True,
        "phone": True,
    },
}
