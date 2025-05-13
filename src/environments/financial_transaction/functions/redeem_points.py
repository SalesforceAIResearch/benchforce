import json
from typing import Any, Dict
from src.classes.function import Function


class RedeemPoints(Function):
    @staticmethod
    def apply(data: Dict[str, Any], account_number: str, points_to_redeem: int, redemption_type: str) -> str:
        points_to_redeem = int(points_to_redeem)
        accounts = data.get('accounts', {})
        account = accounts.get(account_number)
        if not account:
            return "Error: account not found"
        current_points = account.get("points_balance", 0)
        if points_to_redeem > current_points:
            return "Error: insufficient points"
        conversion_rate = 0.01 if redemption_type == "cash" else 0.012
        value = points_to_redeem * conversion_rate
        account["points_balance"] = current_points - points_to_redeem
        account.setdefault("redemptions", []).append({
            "type": redemption_type,
            "points_redeemed": points_to_redeem,
            "value": value
        })
        return json.dumps({
            "message": "Points redeemed",
            "redemption_type": redemption_type,
            "value": value,
            "remaining_points": account["points_balance"]
        })
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "redeem_points",
                "description": "Redeems a specified number of reward points for cash or vouchers.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_number": {"type": "string", "description": "The credit card account number."},
                        "points_to_redeem": {"type": "integer", "description": "Number of points to redeem."},
                        "redemption_type": {"type": "string", "description": "Type of redemption: 'cash' or 'voucher'."}
                    },
                    "required": ["account_number", "points_to_redeem", "redemption_type"]
                }
            }
        }