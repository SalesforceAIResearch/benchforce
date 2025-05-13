import json
from typing import Any, Dict
from src.classes.function import Function


class ChangeCreditCardLimit(Function):
    @staticmethod
    def apply(data: Dict[str, Any], account_number: str, new_limit: float) -> str:
        accounts = data.get('accounts', {})
        account = accounts.get(account_number)
        if not account:
            return "Error: account not found"
        account["credit_limit"] = new_limit
        return json.dumps({
            "message": "Credit card limit updated",
            "account_number": account_number,
            "new_limit": new_limit
        })
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "change_credit_card_limit",
                "description": "Updates the credit card limit for a specified account.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_number": {"type": "string", "description": "The credit card account number."},
                        "new_limit": {"type": "number", "description": "The new credit limit to set."}
                    },
                    "required": ["account_number", "new_limit"]
                }
            }
        }