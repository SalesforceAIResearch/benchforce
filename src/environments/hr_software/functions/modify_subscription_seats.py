# Copyright Sierra

import json
from typing import Any, Dict
from src.classes.function import Function


class ModifySubscriptionSeats(Function):
    @staticmethod
    def apply(data: Dict[str, Any], subscription_id: str, new_seat_count: int) -> str:
        subscriptions = data["subscriptions"]
        if subscription_id not in subscriptions:
            return json.dumps({"error": "Subscription not found"})
            
        subscription = subscriptions[subscription_id]
        tier = subscription["tier"]
        
        # Check minimum seats by tier
        min_seats = {
            "basic": 5,
            "professional": 25,
            "enterprise": 100
        }
        
        if new_seat_count < min_seats[tier]:
            return json.dumps({
                "error": f"Minimum seats for {tier} tier is {min_seats[tier]}"
            })
            
        # Check if reducing seats (only allowed at renewal)
        if new_seat_count < subscription["seats"]:
            return json.dumps({
                "error": "Seat reduction is only allowed at renewal"
            })
            
        # Calculate price with volume discounts
        base_price = subscription["price_per_seat"]
        if new_seat_count >= 1000:
            discount = 0.20  # 20% off
        elif new_seat_count >= 500:
            discount = 0.15  # 15% off
        elif new_seat_count >= 100:
            discount = 0.10  # 10% off
        else:
            discount = 0
            
        new_total = base_price * new_seat_count * (1 - discount)
        
        subscription["seats"] = new_seat_count
        subscription["total_price"] = new_total
        
        return json.dumps({
            "success": True,
            "message": f"Updated to {new_seat_count} seats",
            "new_total": new_total
        })

    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "modify_subscription_seats",
                "description": "Modify the number of seats in a subscription (can only increase, not decrease).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subscription_id": {
                            "type": "string",
                            "description": "The subscription ID in format SUB-XXXXX.",
                        },
                        "new_seat_count": {
                            "type": "integer",
                            "description": "The new number of seats.",
                        },
                    },
                    "required": ["subscription_id", "new_seat_count"],
                },
            },
        } 

