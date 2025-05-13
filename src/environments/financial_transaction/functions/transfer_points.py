import json
from typing import Any, Dict
from src.classes.function import Function


class TransferPoints(Function):
    @staticmethod
    def apply(data: Dict[str, Any], from_account: str, to_account: str, points) -> str:
        points = int(points)
        accounts = data.get('accounts', {})
        sender = accounts.get(from_account)
        receiver = accounts.get(to_account)
        if not sender:
            return "Error: sender account not found"
        if not receiver:
            return "Error: receiver account not found"
        if sender.get("points_balance", 0) < points:
            return "Error: insufficient points in sender account"
        sender["points_balance"] -= points
        receiver["points_balance"] = receiver.get("points_balance", 0) + points
        return json.dumps({
            "message": "Points transferred",
            "from_account": from_account,
            "to_account": to_account,
            "points_transferred": points
        })
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "transfer_points",
                "description": "Transfers reward points from one account to another.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "from_account": {"type": "string", "description": "The sender's account number."},
                        "to_account": {"type": "string", "description": "The receiver's account number."},
                        "points": {"type": "integer", "description": "Number of points to transfer."}
                    },
                    "required": ["from_account", "to_account", "points"]
                }
            }
        }