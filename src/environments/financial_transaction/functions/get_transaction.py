import json
from typing import Any, Dict
from src.classes.function import Function


class GetTransaction(Function):
    @staticmethod
    def apply(data: Dict[str, Any], transaction_id: str) -> str:
        transactions = data.get('transactions', {})
        transaction = transactions.get(transaction_id)
        if not transaction:
            return "Error: transaction not found"
        return json.dumps(transaction)
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_transaction",
                "description": "Returns details of a transaction identified by its transaction ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "transaction_id": {
                            "type": "string",
                            "description": "The unique transaction identifier (e.g., 'TXN1001')."
                        }
                    },
                    "required": ["transaction_id"]
                }
            }
        }