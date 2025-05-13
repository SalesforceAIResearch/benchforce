import json
from typing import Any, Dict
from src.classes.function import Function



class DisputePointsAdjustment(Function):
    @staticmethod
    def apply(data: Dict[str, Any], account_number: str, dispute_reason: str) -> str:
        accounts = data.get('accounts', {})
        account = accounts.get(account_number)
        if not account:
            return "Error: account not found"
        account.setdefault("points_disputes", []).append({
            "reason": dispute_reason,
            "status": "pending"
        })
        return json.dumps({
            "message": "Points adjustment dispute initiated",
            "account_number": account_number,
            "dispute_reason": dispute_reason
        })
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "dispute_points_adjustment",
                "description": "Initiates a dispute regarding a points adjustment on the account.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_number": {"type": "string", "description": "The credit card account number."},
                        "dispute_reason": {"type": "string", "description": "The reason for disputing the points adjustment."}
                    },
                    "required": ["account_number", "dispute_reason"]
                }
            }
        }