import json
from typing import Any, Dict
from src.classes.function import Function


class UpdateTransaction(Function):
    @staticmethod
    def apply(data: Dict[str, Any], transaction_id: str, new_amount: float = None, new_description: str = "") -> str:
        transactions = data.get('transactions', {})
        if transaction_id not in transactions:
            return "Error: transaction not found"
        transaction = transactions[transaction_id]
        if new_amount is not None:
            transaction["amount"] = new_amount
        if new_description:
            transaction["description"] = new_description
        return json.dumps({"message": "Transaction updated", "transaction": transaction})
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_transaction",
                "description": "Updates the amount and/or description of a transaction.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "transaction_id": {"type": "string", "description": "The unique transaction identifier."},
                        "new_amount": {"type": "number", "description": "The new amount for the transaction (optional)."},
                        "new_description": {"type": "string", "description": "The new description for the transaction (optional)."}
                    },
                    "required": ["transaction_id"]
                }
            }
        }
