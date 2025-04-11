import json
from typing import Any, Dict
from src.classes.function import Function

class DisputeTransaction(Function):
    @staticmethod
    def apply(data: Dict[str, Any], transaction_id: str, reason: str) -> str:
        transactions = data.get('transactions', {})
        if transaction_id not in transactions:
            return "Error: transaction not found"
        transaction = transactions[transaction_id]
        transaction["dispute"] = {
            "status": "pending",
            "reason": reason
        }
        return json.dumps({"message": "Dispute initiated", "transaction": transaction})
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "dispute_transaction",
                "description": "Initiates a dispute for a transaction, providing a reason for the dispute.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "transaction_id": {
                            "type": "string",
                            "description": "The unique transaction identifier."
                        },
                        "reason": {
                            "type": "string",
                            "description": "The reason for disputing the transaction."
                        }
                    },
                    "required": ["transaction_id", "reason"]
                }
            }
        }