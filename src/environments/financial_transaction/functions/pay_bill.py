import json
from typing import Any, Dict
from src.classes.function import Function


class PayBill(Function):
    @staticmethod
    def apply(data: Dict[str, Any], account_number: str, payment_amount: float) -> str:
        payment_amount = float(payment_amount)
        accounts = data.get('accounts', {})
        account = accounts.get(account_number)
        if not account:
            return "Error: account not found"
        current_balance = account.get("balance", 0)
        if payment_amount > current_balance:
            return "Error: payment amount exceeds current balance"
        account["balance"] = current_balance - payment_amount
        account.setdefault("payments", []).append({
            "amount": payment_amount,
            "status": "processed"
        })
        return json.dumps({
            "message": "Bill payment processed",
            "account_number": account_number,
            "new_balance": account["balance"]
        })
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "pay_bill",
                "description": "Processes a payment for the credit card bill.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_number": {"type": "string", "description": "The credit card account number."},
                        "payment_amount": {"type": "number", "description": "The amount to pay towards the bill."}
                    },
                    "required": ["account_number", "payment_amount"]
                }
            }
        }