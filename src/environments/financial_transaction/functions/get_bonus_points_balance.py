import json
from typing import Any, Dict
from src.classes.function import Function


class GetBonusPointsBalance(Function):
    @staticmethod
    def apply(data: Dict[str, Any], account_number: str) -> str:
        accounts = data.get('accounts', {})
        account = accounts.get(account_number)
        if not account:
            return "Error: account not found"
        return json.dumps({
            "account_number": account_number,
            "points_balance": account.get("points_balance")
        })

    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_bonus_points_balance",
                "description": "Retrieves the current bonus points balance of the specified account.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_number": {
                            "type": "string",
                            "description": "The Chase account number for which to check bonus points (e.g., 'CC123456789')."
                        }
                    },
                    "required": ["account_number"]
                }
            }
        }
