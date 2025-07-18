# Copyright Sierra

import json
from typing import Any, Dict
from src.classes.function import Function


class ModifySubscriptionTier(Function):
    @staticmethod
    def apply(data: Dict[str, Any], subscription_id: str, new_tier: str) -> str:
        subscriptions = data["subscriptions"]
        if subscription_id not in subscriptions:
            return json.dumps({"error": "Subscription not found"})
            
        subscription = subscriptions[subscription_id]
        current_tier = subscription["tier"]
        valid_tiers = ["basic", "professional", "enterprise"]
        
        if new_tier not in valid_tiers:
            return json.dumps({
                "error": f"Invalid tier. Must be one of: {', '.join(valid_tiers)}"
            })
            
        # Check if downgrading (only allowed at renewal)
        tier_levels = {"basic": 1, "professional": 2, "enterprise": 3}
        if tier_levels[new_tier] < tier_levels[current_tier]:
            return json.dumps({
                "error": "Downgrading tier is only allowed at renewal"
            })
            
        # Check minimum seats for new tier
        min_seats = {
            "basic": 5,
            "professional": 25,
            "enterprise": 100
        }
        
        if subscription["seats"] < min_seats[new_tier]:
            return json.dumps({
                "error": f"Need minimum {min_seats[new_tier]} seats for {new_tier} tier"
            })
            
        # Calculate new price
        base_prices = {
            "basic": 10,
            "professional": 20,
            "enterprise": 40
        }
        
        seats = subscription["seats"]
        base_price = base_prices[new_tier]
        
        # Apply volume discounts
        if seats >= 1000:
            discount = 0.20
        elif seats >= 500:
            discount = 0.15
        elif seats >= 100:
            discount = 0.10
        else:
            discount = 0
            
        new_total = base_price * seats * (1 - discount)
        
        subscription["tier"] = new_tier
        subscription["price_per_seat"] = base_price
        subscription["total_price"] = new_total
        
        return json.dumps({
            "success": True,
            "message": f"Updated to {new_tier} tier",
            "new_total": new_total
        })

    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "modify_subscription_tier",
                "description": "Modify the subscription tier (can upgrade immediately, downgrade only at renewal).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subscription_id": {
                            "type": "string",
                            "description": "The subscription ID in format SUB-XXXXX.",
                        },
                        "new_tier": {
                            "type": "string",
                            "description": "The new tier (basic, professional, or enterprise).",
                        },
                    },
                    "required": ["subscription_id", "new_tier"],
                },
            },
        } 