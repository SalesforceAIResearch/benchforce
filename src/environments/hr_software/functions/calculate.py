# Copyright Sierra

import json
from typing import Any, Dict
from src.classes.function import Function


class Calculate(Function):
    @staticmethod
    def apply(data: Dict[str, Any], expression: str) -> str:
        try:
            # Only allow basic arithmetic operations
            allowed_chars = set("0123456789+-*/(). ")
            if not all(c in allowed_chars for c in expression):
                return json.dumps({
                    "error": "Invalid characters in expression. Only numbers and basic arithmetic operators (+,-,*,/,()) are allowed."
                })
            
            # Evaluate the expression safely
            result = eval(expression, {"__builtins__": {}}, {})
            return json.dumps({"result": result})
            
        except Exception as e:
            return json.dumps({
                "error": f"Failed to calculate expression: {str(e)}"
            })

    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate",
                "description": "Perform basic arithmetic calculations (+, -, *, /).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "expression": {
                            "type": "string",
                            "description": "The arithmetic expression to evaluate (e.g., '2 + 2' or '150 * 0.9').",
                        },
                    },
                    "required": ["expression"],
                },
            },
        } 