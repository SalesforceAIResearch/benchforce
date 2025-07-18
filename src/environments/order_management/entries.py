entries = [
    {
        "id": "entry_1",
        "instructions": "Your name is Michael Thompson. Your customer ID is C1013 and your email is michael.thompson@gap.com. You have an order with order ID O1033, and you need to check its shipping status. Do not provide the order ID until prompted. After confirmation, ask if you can update the shipping address to 415 Mission Street, San Francisco, CA 94105.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "verified_email": "michael.thompson@gap.com",
                },
            },
        ],
    },
]
