import json
from typing import Any, Dict
from src.classes.function import Function


class GenerateOrderReport(Function):
    @staticmethod
    def apply(data: Dict[str, Any], report_date: str) -> str:
        orders = data.get('orders', {})
        report_orders = [order for order in orders.values() if order.get("created_date", "").startswith(report_date)]
        summary = {
            "report_date": report_date,
            "total_orders": len(report_orders),
            "orders": report_orders
        }
        return json.dumps(summary)
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_order_report",
                "description": "Generates a summary report of orders created on a specified date (YYYY-MM-DD or YYYY-MM).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_date": {"type": "string", "description": "The date for the report in YYYY-MM-DD or YYYY-MM format."}
                    },
                    "required": ["report_date"]
                }
            }
        }
