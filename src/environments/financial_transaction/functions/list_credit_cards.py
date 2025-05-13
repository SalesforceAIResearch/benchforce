import json
from typing import Any, Dict
from src.classes.function import Function

class ListCreditCards(Function):
    @staticmethod
    def apply(data: Dict[str, Any], account_number: str) -> str:
        cards = data.get('credit_cards', [])
        
        filtered_cards = [card for card in cards if card.get('account_number') == account_number]
        return json.dumps(filtered_cards)
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_credit_cards",
                "description": "Lists all Chase credit cards available to the user.",
                "parameters": {
                    'type': 'object',
                    'properties': {
                    'account_number': { 'type': 'string', 'description': 'The Chase account number.' },
                    },
                    'required': ['account_number']
                },
            }
        }