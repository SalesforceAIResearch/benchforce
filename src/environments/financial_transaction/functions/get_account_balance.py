import json
from typing import Any, Dict
from src.classes.function import Function

class GetAccountBalance(Function):
    @staticmethod
    def apply(data: Dict[str, Any], account_number: str) -> str:
        accounts = data.get('accounts', {})
        account = accounts.get(account_number)
        if not account:
            return "Error: account not found"
        return json.dumps({"account_number": account_number, "balance": account.get("balance")})
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_account_balance",
                "description": "Retrieves the current balance of the specified account.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_number": {
                            "type": "string",
                            "description": "The Chase credit card account number (e.g., 'CC123456789')."
                        }
                    },
                    "required": ["account_number"]
                }
            }
        }