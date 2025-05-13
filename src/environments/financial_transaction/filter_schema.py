filter_schema = {
    "credit_cards": {
        "credit_card_id": True,
        "account_number": True,
        "card_type": True,
        "issuing_bank": True,
        "issued_date": True,
    },
    "transactions": {
        "*": {
            "transaction_id": True,
            "account_number": True,
            "amount": True,
            "description": False,
            "month": True,
        }
    },
    "accounts": {
        "*": {
            "account_number": True,
            "account_holder": True,
            "balance": True,
            "points_balance": True,
            "credit_limit": True,
            "redemptions": True,
            "payments": True,
            "points_disputes": False,
        }
    },
}
