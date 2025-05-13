import json
from typing import Any, Dict
from src.classes.function import Function


class ListTransactions(Function):
    @staticmethod
    def apply(data: Dict[str, Any], account_number: str) -> str:
        transactions = data.get('transactions', {})
        account_transactions = [txn for txn in transactions.values() if txn.get("account_number") == account_number]
        return json.dumps(account_transactions)
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_transactions",
                "description": "Lists all transactions associated with a given account number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_number": {
                            "type": "string",
                            "description": "The account number for which to list transactions."
                        }
                    },
                    "required": ["account_number"]
                }
            }
        }
