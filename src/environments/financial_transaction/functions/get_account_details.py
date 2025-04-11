import json
from typing import Any, Dict
from src.classes.function import Function


class GetAccountDetails(Function):
    @staticmethod
    def apply(data: Dict[str, Any], account_holder: str) -> str:
        accounts = data.get('accounts', {})
        for acc in accounts.values():
            if acc.get("account_holder") == account_holder:
                return json.dumps(acc)
        return f"Error: account for '{account_holder}' not found"
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_account_details",
                "description": "Retrieves account details by account holder's name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_holder": {"type": "string", "description": "The full name of the account holder."}
                    },
                    "required": ["account_holder"]
                }
            }
        }