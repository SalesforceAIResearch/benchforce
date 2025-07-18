# Copyright Sierra

import json
from typing import Any, Dict
from src.classes.function import Function


class CalculateServiceCredits(Function):
    @staticmethod
    def apply(data: Dict[str, Any], subscription_id: str, downtime_minutes: int) -> str:
        subscriptions = data["subscriptions"]
        if subscription_id not in subscriptions:
            return json.dumps({"error": "Subscription not found"})
            
        subscription = subscriptions[subscription_id]
        tier = subscription["tier"]
        monthly_fee = subscription["total_price"]
        
        # Calculate SLA breach percentage
        minutes_per_month = 43200  # 30 days * 24 hours * 60 minutes
        actual_uptime_percentage = 100 * (1 - downtime_minutes / minutes_per_month)
        
        # Check against SLA by tier
        sla_targets = {
            "enterprise": 99.99,  # ≤ 4.32 minutes downtime/month
            "professional": 99.95,  # ≤ 21.6 minutes downtime/month
            "basic": 99.9  # ≤ 43.2 minutes downtime/month
        }
        
        if actual_uptime_percentage >= sla_targets[tier]:
            return json.dumps({
                "credits": 0,
                "message": f"No SLA breach. Actual uptime: {actual_uptime_percentage:.3f}%"
            })
            
        # Calculate credits based on tier
        credit_rates = {
            "enterprise": 0.10,  # 10% of monthly fee per 0.1% below SLA
            "professional": 0.05,  # 5% of monthly fee per 0.1% below SLA
            "basic": 0.03  # 3% of monthly fee per 0.1% below SLA
        }
        
        percentage_below_sla = sla_targets[tier] - actual_uptime_percentage
        credit_multiplier = percentage_below_sla / 0.1  # per 0.1% below SLA
        credit_amount = monthly_fee * credit_rates[tier] * credit_multiplier
        
        # Cap at 100% of monthly fee
        credit_amount = min(credit_amount, monthly_fee)
        
        return json.dumps({
            "credits": credit_amount,
            "actual_uptime": actual_uptime_percentage,
            "sla_target": sla_targets[tier],
            "percentage_below_sla": percentage_below_sla
        })

    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_service_credits",
                "description": "Calculate service credits based on verified downtime duration.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subscription_id": {
                            "type": "string",
                            "description": "The subscription ID in format SUB-XXXXX.",
                        },
                        "downtime_minutes": {
                            "type": "integer",
                            "description": "The duration of verified downtime in minutes.",
                        },
                    },
                    "required": ["subscription_id", "downtime_minutes"],
                },
            },
        } 