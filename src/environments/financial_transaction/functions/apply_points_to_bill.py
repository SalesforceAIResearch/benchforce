import json
from typing import Any, Dict
from src.classes.function import Function


class ApplyPointsToBill(Function):
    @staticmethod
    def apply(data: Dict[str, Any], account_number: str, points_to_apply) -> str:
        points_to_apply = int(points_to_apply)
        accounts = data.get('accounts', {})
        account = accounts.get(account_number)
        if not account:
            return "Error: account not found"
        current_points = account.get("points_balance", 0)
        if points_to_apply > current_points:
            return "Error: insufficient points"
        credit = points_to_apply * 0.01
        account["balance"] = max(account.get("balance", 0) - credit, 0)
        account["points_balance"] = current_points - points_to_apply
        return json.dumps({
            "message": "Points applied to bill",
            "account_number": account_number,
            "new_balance": account["balance"],
            "remaining_points": account["points_balance"]
        })
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "apply_points_to_bill",
                "description": "Applies a specified number of reward points to reduce the account bill.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_number": {"type": "string", "description": "The credit card account number."},
                        "points_to_apply": {"type": "integer", "description": "Number of reward points to apply."}
                    },
                    "required": ["account_number", "points_to_apply"]
                }
            }
        }