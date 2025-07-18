import json
from typing import Any, Dict, Optional
from src.classes.function import Function


class ConfirmCustomerIdentity(Function):
    @staticmethod
    def apply(data: Dict[str, Any], customer_id: Optional[str] = None, verified_email: Optional[str] = None) -> str:
        customers = data.get("customers", [])
        
        if customer_id:
            match = next((c for c in customers if c.get("customer_id") == customer_id), None)
            if match:
                return json.dumps({
                    "status": "confirmed",
                    "method": "customer_id",
                    "customer": match
                })

        if verified_email:
            match = next((c for c in customers if c.get("email") == verified_email), None)
            if match:
                return json.dumps({
                    "status": "confirmed",
                    "method": "verified_email",
                    "customer": match
                })

        return json.dumps({
            "status": "not_confirmed",
            "reason": "No matching customer found with provided identifiers."
        })

    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "confirm_customer_identity",
                "description": "Confirms the customer's identity using provided identifiers such as customer ID or verified email address. Request additional details (e.g., order ID) only if sufficient context is provided.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "The unique identifier for the customer."
                        },
                        "verified_email": {
                            "type": "string",
                            "description": "The customer's verified email address."
                        }
                    },
                    "required": []
                }
            }
        }
