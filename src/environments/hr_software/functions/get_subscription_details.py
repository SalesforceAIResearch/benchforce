# Copyright Sierra

import json
from typing import Any, Dict
from src.classes.function import Function


class GetSubscriptionDetails(Function):
    @staticmethod
    def apply(data: Dict[str, Any], subscription_id: str) -> str:
        subscriptions = data["subscriptions"]
        if subscription_id in subscriptions:
            return json.dumps(subscriptions[subscription_id])
        return json.dumps({"error": "Subscription not found"})

    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_subscription_details",
                "description": "Get the details of a subscription including tier, seats, dates, and configured modules.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subscription_id": {
                            "type": "string",
                            "description": "The subscription ID in format SUB-XXXXX.",
                        },
                    },
                    "required": ["subscription_id"],
                },
            },
        } 