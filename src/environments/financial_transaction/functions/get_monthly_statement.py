import json
from typing import Any, Dict
from src.classes.function import Function


class GetMonthlyStatement(Function):
    @staticmethod
    def apply(data: Dict[str, Any], account_number: str, statement_month: str) -> str:
        transactions = data.get('transactions', {})
        statement = [txn for txn in transactions.values() if txn.get("account_number") == account_number and txn.get("month") == statement_month]
        summary = {
            "account_number": account_number,
            "statement_month": statement_month,
            "total_transactions": len(statement),
            "transactions": statement
        }
        return json.dumps(summary)
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_monthly_statement",
                "description": "Generates a monthly statement report for a specified credit card account.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_number": {"type": "string", "description": "The credit card account number."},
                        "statement_month": {"type": "string", "description": "The month for which to generate the statement (e.g., '2025-04')."}
                    },
                    "required": ["account_number", "statement_month"]
                }
            }
        }
