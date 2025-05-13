entries = [
    {
        "id": "entry_9",
        "instructions": "Keep silence",
        "actions": [
            {"name": "get_account_details", "arguments": {"account_holder": "Ian Lee"}}
        ],
        "outputs": [
            "845"
        ]
    },
    {
        "id": "entry_33",
        "instructions": "Your name is Laura Wilson. You want to check your reward points balance for the account CC1012. Do not share your account number until asked by the agent.",
        "actions": [
            {"name": "get_account_balance", "arguments": {"account_number": "CC1012"}}
        ],
        "outputs": [
            "8300"
        ]
    },
    {
        "id": "entry_110",
        "instructions": "Your name is Alice Johnson. You want to generate a monthly statement for your account for March 2025 (account number CC1001). Wait for the agent to ask for your account number before providing it.",
        "actions": [
            {
                "name": "get_monthly_statement",
                "arguments": {"account_number": "CC1001", "statement_month": "2025-03"},
            }
        ],
    },
    {
        "id": "entry_7",
        "instructions": "Your name is Bob Smith. You want to transfer 2000 reward points from your account CC1002 to Charlie William's account CC1003. Only provide the required account numbers when prompted.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Bob Smith"},
            },
            {
                "name": "transfer_points",
                "arguments": {
                    "from_account": "CC1002",
                    "to_account": "CC1003",
                    "points": "2000",
                },
            },
        ],
    },
    {
        "id": "entry_134",
        "instructions": "Your name is Hannah Rodriguez. You want to update a transaction (TXN1033) with amount $25 to a new amount of $50. Only provide the transaction ID when asked.",
        "actions": [
            {"name": "get_transaction", "arguments": {"transaction_id": "TXN1033"}},
            {
                "name": "update_transaction",
                "arguments": {
                    "transaction_id": "TXN1033",
                    "new_amount": "50",
                    "new_description": "Lunch",
                },
            },
        ],
    },
    {
        "id": "entry_114",
        "instructions": "Your name is Ian Lee. You want to update a transaction (TXN1030) from 2025-04 for [random amount] with a corrected amount of $78.50 for online shopping. Only provide the transaction ID when asked.",
        "actions": [
            {"name": "get_transaction", "arguments": {"transaction_id": "TXN1030"}},
            {
                "name": "update_transaction",
                "arguments": {
                    "transaction_id": "TXN1030",
                    "new_amount": "78.5",
                    "new_description": "Online Shopping",
                },
            },
        ],
    },
    {
        "id": "entry_15",
        "instructions": "Your name is Oliver Scott. You want to retrieve a specific transaction on month 2025-04 (TXN1010) with amount $30.25. Do not provide the transaction ID until asked.",
        "actions": [
            {"name": "get_transaction", "arguments": {"transaction_id": "TXN1010"}}
        ],
        "outputs": [
            "Pharmacy",
            "30"
        ]
    },
    {
        "id": "entry_63",
        "instructions": "Your name is Alice Johnson. You want to generate a monthly statement for May 2025 for account number CC1001. Provide your account number only when requested.",
        "actions": [
            {
                "name": "get_monthly_statement",
                "arguments": {"account_number": "CC1001", "statement_month": "2025-05"},
            }
        ],
        "outputs": [
          "clothing"
        ]
    },
    {
        "id": "entry_100",
        "instructions": "Your name is Alice Johnson. You want to list all Chase credit cards available. Provide your account number (CC1001) only when requested.",
        "actions": [{"name": "list_credit_cards", "arguments": {"account_number": "CC1001"}}],
        "outputs": [
          "Sapphire"
        ]
    },
    {
        "id": "entry_22",
        "instructions": "Your name is Alice Johnson. You want to transfer 5,000 reward points from your account number CC1001 to another Chase account number CC1002. Do not reveal account numbers until the agent requests them.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Alice Johnson"},
            },
            {
                "name": "transfer_points",
                "arguments": {
                    "from_account": "CC1001",
                    "to_account": "CC1002",
                    "points": "5000",
                },
            },
        ],
    },
    {
        "id": "entry_39",
        "instructions": "Your name is Charlie Williams. You want to pay your bill for $150 for account number CC1003. Wait until the agent asks for your account number before providing it.",
        "actions": [
            {"name": "get_account_balance", "arguments": {"account_number": "CC1003"}},
            {
                "name": "pay_bill",
                "arguments": {"account_number": "CC1003", "payment_amount": "150"},
            },
        ],
    },
    {
        "id": "entry_86",
        "instructions": "Your name is Bob Smith. You want to list all transactions for your account CC1002. Do not provide your account number until requested.",
        "actions": [
            {"name": "list_transactions", "arguments": {"account_number": "CC1002"}}
        ],
        "outputs": [
            "Dining",
            "Fuel",
            "Pet"
        ]
    },
    {
        "id": "entry_143",
        "instructions": "Your name is Quentin Baker. You want to list all Chase credit cards available. Provide your account number (CC1017) only when requested by the agent.",
        "actions": [{"name": "list_credit_cards", "arguments": {"account_number": "CC1017"}}],
    },
    {
        "id": "entry_52",
        "instructions": "Your name is Diana Brown. You want to retrieve detailed account information by your name. Do not provide any sensitive account details until asked.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Diana Brown"},
            }
        ],
        "outputs": [
            "Diana Brown",
            "6000"
        ]
    },
    {
        "id": "entry_72",
        "instructions": "Your name is Alice Johnson. You want to retrieve your account details using your name. Do not reveal any sensitive details until prompted.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Alice Johnson"},
            }
        ],
        "outputs": [
            "Alice Johnson",
            "1520"
        ]
    },
    {
        "id": "entry_35",
        "instructions": "Your name is Natalie Moore. You want to update a transaction (TXN1017) from May 2025 for $75.50 with a new description of Business Lunch with Client. Wait until the agent asks for the transaction ID before providing details.",
        "actions": [
            {"name": "get_transaction", "arguments": {"transaction_id": "TXN1017"}},
            {
                "name": "update_transaction",
                "arguments": {
                    "transaction_id": "TXN1017",
                    "new_amount": "75.5",
                    "new_description": "Business Lunch with Client",
                },
            },
        ],
    },
    {
        "id": "entry_25",
        "instructions": "Your name is Diana Brown. You want to see the list of all credit cards you own. Only provide details when the agent requests your account number (CC1004).",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Diana Brown"},
            },
            {"name": "list_credit_cards", "arguments": {"account_number": "CC1004"}},
        ],
        "outputs": [
            "Chase Sapphire Reserve"
        ]
    },
    {
        "id": "entry_78",
        "instructions": 'Your name is Oliver Scott. You want to update a transaction in month 2025-05 of $90 (TXN1024) with a corrected description of "Corrected Purchase - Office Supplies". Provide the transaction ID only when the agent asks.',
        "actions": [
            {"name": "get_transaction", "arguments": {"transaction_id": "TXN1024"}},
            {
                "name": "update_transaction",
                "arguments": {
                    "transaction_id": "TXN1024",
                    "new_amount": "90",
                    "new_description": "Corrected Purchase - Office Supplies",
                },
            },
        ],
    },
    {
        "id": "entry_98",
        "instructions": 'Your name is Natalie Moore. You want to update a transaction (TXN1027) from March 2025 for the amount of $35.00 with a new description of "Corrected Description." Provide the transaction ID only when the agent asks.',
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Natalie Moore"},
            },
            {"name": "get_transaction", "arguments": {"transaction_id": "TXN1027"}},
            {
                "name": "update_transaction",
                "arguments": {
                    "transaction_id": "TXN1027",
                    "new_amount": "35",
                    "new_description": "Corrected Description",
                },
            },
        ],
    },
    {
        "id": "entry_13",
        "instructions": "Your name is Michael Anderson. You want to generate a monthly statement for April 2025 for account number CC1013. Provide your account number when prompted.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Michael Anderson"},
            },
            {
                "name": "get_monthly_statement",
                "arguments": {"account_number": "CC1013", "statement_month": "2025-04"},
            },
        ],
        "outputs": [
            "Book purchase",
            "14"
        ]
    },
    {
        "id": "entry_102",
        "instructions": "Your name is Rachel Harris. You want to pay your bill for the full account balance of $880.00 for account number CC1018. Only provide your account number when the agent requests it.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Rachel Harris"},
            },
            {"name": "get_account_balance", "arguments": {"account_number": "CC1018"}},
            {
                "name": "pay_bill",
                "arguments": {"account_number": "CC1018", "payment_amount": "880"},
            },
        ],
    },
    {
        "id": "entry_111",
        "instructions": "Your name is Oliver Scott. You want to dispute an April 2025 transaction (TXN1029) of $12 from account number CC1015 due to being billed an incorrect amount and the charge does not match the agreed-upon price for the service received. Do not share your account number until requested.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Oliver Scott"},
            },
            {"name": "get_transaction", "arguments": {"transaction_id": "TXN1029"}},
            {
                "name": "dispute_transaction",
                "arguments": {
                    "transaction_id": "TXN1029",
                    "reason": "Billed an incorrect amount; charge does not match the agreed-upon price for the service received.",
                },
            },
        ],
    },
    {
        "id": "entry_47",
        "instructions": "Your name is Edward Davis. You want to generate a monthly statement for your account number CC1005 for April 2025. Wait for the agent to ask for your account number before providing it.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Edward Davis"},
            },
            {
                "name": "get_monthly_statement",
                "arguments": {"account_number": "CC1005", "statement_month": "2025-04"},
            },
        ],
        "outputs": [
            "Pharmacy",
            "30"
        ]
    },
    {
        "id": "entry_61",
        "instructions": "Your name is Samuel Lewis. You want to request an increase in your credit card limit to $15,000 for account number CC1019. Wait until the agent asks for your account number before providing it.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Samuel Lewis"},
            },
            {
                "name": "change_credit_card_limit",
                "arguments": {"account_number": "CC1019", "new_limit": "15000"},
            },
        ],
    },
    {
        "id": "entry_64",
        "instructions": "Your name is Laura Wilson. You want to dispute a transaction (TXN1022) from April 2025 for $150 for a spa treatment due to unauthorized charges on account number CC1012. Do not reveal your account number until asked.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Laura Wilson"},
            },
            {"name": "get_transaction", "arguments": {"transaction_id": "TXN1022"}},
            {
                "name": "dispute_transaction",
                "arguments": {
                    "transaction_id": "TXN1022",
                    "reason": "unauthorized charge",
                },
            },
        ],
    },
    {
        "id": "entry_127",
        "instructions": "Your name is Quentin Baker. You want to dispute a transaction (TXN1032) from April 2025 for $130 for furniture due to unauthorized charges on account number CC1017. Do not reveal your account details until asked.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Quentin Baker"},
            },
            {"name": "get_transaction", "arguments": {"transaction_id": "TXN1032"}},
            {
                "name": "dispute_transaction",
                "arguments": {
                    "transaction_id": "TXN1032",
                    "reason": "Unauthorized charges",
                },
            },
        ],
    },
    {
        "id": "entry_66",
        "instructions": "Your name is Charlie Williams. You want to list all transactions for your account number CC1003. Do not provide your account number until the agent requests it.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Charlie Williams"},
            },
            {"name": "list_transactions", "arguments": {"account_number": "CC1003"}},
        ],
        "outputs": [
            "Chase Slate Edge"
        ]
    },
    {
        "id": "entry_23",
        "instructions": "Your name is Bob Smith. You want to update a transaction record (TXN1004) from April 2025 for [random amount] with a corrected amount of $35.20 on account number CC1002. Provide the transaction ID only when asked.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Bob Smith"},
            },
            {"name": "get_transaction", "arguments": {"transaction_id": "TXN1004"}},
            {
                "name": "update_transaction",
                "arguments": {
                    "transaction_id": "TXN1004",
                    "new_amount": "35.2",
                    "new_description": "Fuel purchase",
                },
            },
        ],
    },
    {
        "id": "entry_146",
        "instructions": "Your name is Tina Clark. You want to generate a monthly statement for April 2025 for account number CC1020. Provide your account number only when prompted.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Tina Clark"},
            },
            {
                "name": "get_monthly_statement",
                "arguments": {"account_number": "CC1020", "statement_month": "2025-04"},
            },
        ],
        "outputs": [
            "Breakfast",
            "18"
        ]
    },
    {
        "id": "entry_45",
        "instructions": "Your name is Charlie Williams. You want to request a change in your credit card limit to $15,000 for account number CC1003. Wait until the agent asks for your account number before providing it.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Charlie Williams"},
            },
            {
                "name": "change_credit_card_limit",
                "arguments": {"account_number": "CC1003", "new_limit": "15000"},
            },
        ],
    },
    {
        "id": "entry_11",
        "instructions": "Your name is Kevin Turner. You want to increase your credit card limit for account number CC1011 from $4200 to $5000. Only provide your account number when requested by the agent.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Kevin Turner"},
            },
            {
                "name": "change_credit_card_limit",
                "arguments": {"account_number": "CC1011", "new_limit": "5000"},
            },
        ],
    },
    {
        "id": "entry_126",
        "instructions": "Your name is Ulysses Reed. You want to generate a monthly statement for May 2025 for account number CC1021. Provide your account number only when requested.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Ulysses Reed"},
            },
            {
                "name": "get_monthly_statement",
                "arguments": {"account_number": "CC1021", "statement_month": "2025-05"},
            },
        ],
    },
    {
        "id": "entry_58",
        "instructions": 'Your name is Kevin Turner. You want to update a transaction (TXN1021) from April 2025 for the amount of $80 with a corrected description of "Office Supplies Purchase" on account number CC1011. Only provide the transaction ID when asked.',
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Kevin Turner"},
            },
            {"name": "get_transaction", "arguments": {"transaction_id": "TXN1021"}},
            {
                "name": "update_transaction",
                "arguments": {
                    "transaction_id": "TXN1021",
                    "new_amount": "80",
                    "new_description": "Office Supplies Purchase",
                },
            },
        ],
    },
    {
        "id": "entry_73",
        "instructions": "Your name is Julia Kim. You want to list all transactions for your account number CC1010. Provide your account number only when the agent requests it.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Julia Kim"},
            },
            {"name": "list_transactions", "arguments": {"account_number": "CC1010"}},
        ],
        "outputs": [
            "Flight booking",
            "Coffee"
        ]
    },
    {
        "id": "entry_38",
        "instructions": "Your name is Quentin Baker. You want to request a change in your credit card limit to $15,000 for account number CC1017. Do not provide your account number until asked.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Quentin Baker"},
            },
            {
                "name": "change_credit_card_limit",
                "arguments": {"account_number": "CC1017", "new_limit": "15000"},
            },
        ],
    },
    {
        "id": "entry_147",
        "instructions": "Your name is Rachel Harris. You want to dispute an April 2025 transaction (TXN1035) for $44 due to billing errors. Do not reveal your account details until asked by the agent.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Rachel Harris"},
            },
            {
                "name": "dispute_transaction",
                "arguments": {"transaction_id": "TXN1035", "reason": "billing errors"},
            },
        ],
    },
    {
        "id": "entry_37",
        "instructions": "Your name is Patricia Young. You want to list all your transactions for account number CC1016. Only provide your account number when the agent requests it.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Patricia Young"},
            },
            {"name": "list_transactions", "arguments": {"account_number": "CC1016"}},
        ],
        "outputs": [
            "Online shopping",
            "Streaming subscription"
        ]
    },
    {
        "id": "entry_71",
        "instructions": "Your name is Laura Wilson. You want to update a transaction (TXN1023) from March 2025 for [random amount] with a corrected amount of $22.50 on account number CC1012. Only provide the transaction ID when asked.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Laura Wilson"},
            },
            {"name": "get_transaction", "arguments": {"transaction_id": "TXN1023"}},
            {
                "name": "update_transaction",
                "arguments": {
                    "transaction_id": "TXN1023",
                    "new_amount": "22.5",
                    "new_description": "Ice cream",
                },
            },
        ],
    },
    {
        "id": "entry_129",
        "instructions": "Your name is Charlie Williams. You want to list all transactions for your account CC1003. Do not provide your account number until the agent requests it.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Charlie Williams"},
            },
            {"name": "list_transactions", "arguments": {"account_number": "CC1003"}},
        ],
        "outputs": [
            "Electronics",
            "Coffee",
            "Hardware"
        ]
    },
    {
        "id": "entry_85",
        "instructions": "Your name is Alice Johnson. You want to check your account balance for account number CC1001. Provide your account number only when prompted by the agent.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Alice Johnson"},
            },
            {"name": "get_account_balance", "arguments": {"account_number": "CC1001"}},
        ],
        "outputs": [
            "1520"
        ]
    },
    {
        "id": "entry_135",
        "instructions": "Your name is Ian Lee. You want to retrieve your account details using your name. Do not provide any extra information until requested.",
        "actions": [
            {"name": "get_account_details", "arguments": {"account_holder": "Ian Lee"}}
        ],
        "outputs": [
            "Ian Lee",
            "845"
        ]
    },
    {
        "id": "entry_93",
        "instructions": "Your name is Ian Lee. You want to list all transactions for your account number CC1009. Provide your account number only when the agent asks.",
        "actions": [
            {"name": "get_account_details", "arguments": {"account_holder": "Ian Lee"}},
            {"name": "list_transactions", "arguments": {"account_number": "CC1009"}},
        ],
        "outputs": [
            "Supermarket shopping",
            "Restaurant dinner"
        ]
    },
    {
        "id": "entry_18",
        "instructions": "Your name is Rachel Harris. You want to list all your transactions for account number CC1018. Provide your account number only when requested.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Rachel Harris"},
            },
            {"name": "list_transactions", "arguments": {"account_number": "CC1018"}},
        ],
        "outputs": [
            "Bookstore",
            "Online course"
        ]
    },
    {
        "id": "entry_46",
        "instructions": "Your name is Edward Davis. You want to pay your bill for this month of $340.20 for account number CC1005. Provide your account number only when the agent requests it.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Edward Davis"},
            },
            {"name": "get_account_balance", "arguments": {"account_number": "CC1005"}},
            {
                "name": "pay_bill",
                "arguments": {"account_number": "CC1005", "payment_amount": "340.20"},
            },
        ],
    },
    {
        "id": "entry_139",
        "instructions": "Your name is Michael Anderson. You want to check your reward points balance on account number CC1013. Provide your account number only when the agent asks for it.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Michael Anderson"},
            },
            {
                "name": "get_bonus_points_balance",
                "arguments": {"account_number": "CC1013"},
            },
        ],
        "outputs": [
            "9100"
        ]
    },
    {
        "id": "entry_144",
        "instructions": "Your name is Rachel Harris. You want to request a change in your credit card limit for account number CC1018 from $4,600 to $15,000. Do not provide your account number until the agent asks for it.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Rachel Harris"},
            },
            {
                "name": "change_credit_card_limit",
                "arguments": {"account_number": "CC1018", "new_limit": "15000"},
            },
        ],
    },
    {
        "id": "entry_19",
        "instructions": "Your name is Samuel Lewis. You want to apply 5,000 reward points to reduce your bill on account number CC1019. Wait for the agent to request the number of points before providing them.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Samuel Lewis"},
            },
            {
                "name": "get_bonus_points_balance",
                "arguments": {"account_number": "CC1019"},
            },
            {
                "name": "apply_points_to_bill",
                "arguments": {"account_number": "CC1019", "points_to_apply": "5000"},
            },
        ],
    },
    {
        "id": "entry_40",
        "instructions": "Your name is Samuel Lewis. You want to generate a monthly statement for May 2025 for account number CC1019. Provide your account number only when requested.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Samuel Lewis"},
            },
            {
                "name": "get_monthly_statement",
                "arguments": {"account_number": "CC1019", "statement_month": "2025-05"},
            },
        ],
    },
    {
        "id": "entry_42",
        "instructions": "Your name is Julia Kim. You want to retrieve details of a specific transaction (TXN1018) on account number CC1010. Wait for the agent to ask for the transaction ID before sharing it.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Julia Kim"},
            },
            {"name": "get_transaction", "arguments": {"transaction_id": "TXN1018"}},
        ],
        "outputs": [
            "Flight booking",
            "200"
        ]
    },
    {
        "id": "entry_148",
        "instructions": "Your name is Alice Johnson. You want to check your account balance for account number CC1001. Provide your account number only when prompted by the agent.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Alice Johnson"},
            },
            {"name": "get_account_balance", "arguments": {"account_number": "CC1001"}},
        ],
        "outputs": [
            "1520"
        ]
    },
    {
        "id": "entry_91",
        "instructions": "Your name is Natalie Moore. You want to update a transaction (TXN1026) from April 2025 for [random amount] to a new amount of $60 on account number CC1014. Only provide the transaction ID when requested.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Natalie Moore"},
            },
            {"name": "get_transaction", "arguments": {"transaction_id": "TXN1026"}},
            {
                "name": "update_transaction",
                "arguments": {
                    "transaction_id": "TXN1026",
                    "new_amount": "60",
                    "new_description": "Grocery shopping",
                },
            },
        ],
    },
    {
        "id": "entry_213",
        "tags": ["complex"],
        "instructions": "You are Michael Anderson. List all your transactions and retrieve details of a high-value electronics purchase. Update the transaction description, process a bill payment, and redeem reward points for a voucher.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Michael Anderson"},
            },
            {"name": "list_transactions", "arguments": {"account_number": "CC1013"}},
            {"name": "get_transaction", "arguments": {"transaction_id": "TXN1024"}},
            {
                "name": "update_transaction",
                "arguments": {
                    "transaction_id": "TXN1024",
                    "new_amount": "90",
                    "new_description": "high-value electronics purchase",
                },
            },
            {
                "name": "pay_bill",
                "arguments": {"account_number": "CC1013", "payment_amount": "600"},
            },
            {
                "name": "redeem_points",
                "arguments": {
                    "account_number": "CC1013",
                    "points_to_redeem": "5000",
                    "redemption_type": "Voucher",
                },
            },
        ],
    },
    {
        "id": "entry_219",
        "tags": ["complex"],
        "instructions": "You are Samuel Lewis. Dispute a concert ticket purchase, then check your current account balance and bonus points balance. Retrieve your account details and list your recent transactions to ensure accuracy.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Samuel Lewis"},
            },
            {"name": "get_transaction", "arguments": {"transaction_id": "TXN1036"}},
            {
                "name": "dispute_transaction",
                "arguments": {"transaction_id": "TXN1036", "reason": "Overcharge"},
            },
            {"name": "get_account_balance", "arguments": {"account_number": "CC1019"}},
            {
                "name": "get_bonus_points_balance",
                "arguments": {"account_number": "CC1019"},
            },
            {"name": "list_transactions", "arguments": {"account_number": "CC1019"}},
        ],
    },
    {
        "id": "entry_206",
        "tags": ["complex"],
        "instructions": "You are Fiona Garcia. Check your current balance and bonus points balance. Retrieve details for a clothing store transaction (TXN1011) for $150, dispute that transaction if found incorrect, transfer 2000 reward points to another account (CC1007), and finally list all available credit cards.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Fiona Garcia"},
            },
            {"name": "get_account_balance", "arguments": {"account_number": "CC1006"}},
            {
                "name": "get_bonus_points_balance",
                "arguments": {"account_number": "CC1006"},
            },
            {"name": "get_transaction", "arguments": {"transaction_id": "TXN1011"}},
            {
                "name": "dispute_transaction",
                "arguments": {
                    "transaction_id": "TXN1011",
                    "reason": "Incorrect Amount",
                },
            },
            {
                "name": "transfer_points",
                "arguments": {
                    "from_account": "CC1006",
                    "to_account": "CC1007",
                    "points": "2000",
                },
            },
            {"name": "list_credit_cards", "arguments": {"account_number": "CC1006"}},
        ],
    },
    {
        "id": "entry_214",
        "tags": ["complex"],
        "instructions": "You are Natalie Moore. Retrieve your account details, dispute a taxi fare transaction, check your bonus points balance, update your credit card limit based on recent spending, and list all your transactions for review.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Natalie Moore"},
            },
            {"name": "get_transaction", "arguments": {"transaction_id": "TXN1027"}},
            {
                "name": "dispute_transaction",
                "arguments": {"transaction_id": "TXN1027", "reason": "Overcharge"},
            },
            {
                "name": "get_bonus_points_balance",
                "arguments": {"account_number": "CC1014"},
            },
            {
                "name": "change_credit_card_limit",
                "arguments": {"account_number": "CC1014", "new_limit": "5000"},
            },
            {"name": "list_transactions", "arguments": {"account_number": "CC1014"}},
        ],
    },
    {
        "id": "entry_201",
        "tags": ["complex"],
        "instructions": "You are Alice Johnson. You noticed a discrepancy in your April bill. First, verify your account details, then check your current balance and bonus points balance. Next, retrieve details of a specific April transaction (TXN1042), dispute that transaction, redeem 5,000 bonus points for a voucher, and finally request your April monthly statement.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Alice Johnson"},
            },
            {"name": "get_account_balance", "arguments": {"account_number": "CC1001"}},
            {
                "name": "get_bonus_points_balance",
                "arguments": {"account_number": "CC1001"},
            },
            {"name": "get_transaction", "arguments": {"transaction_id": "TXN1042"}},
            {
                "name": "dispute_transaction",
                "arguments": {"transaction_id": "TXN1042", "reason": "wrong amount"},
            },
            {
                "name": "redeem_points",
                "arguments": {
                    "account_number": "CC1001",
                    "points_to_redeem": "5000",
                    "redemption_type": "voucher",
                },
            },
            {
                "name": "get_monthly_statement",
                "arguments": {"account_number": "CC1001", "statement_month": "2025-04"},
            },
        ],
    },
    {
        "id": "entry_212",
        "tags": ["complex"],
        "instructions": "You are Laura Wilson. Start by checking your bonus points balance, then dispute a points adjustment error. Retrieve your account balance, apply 3000 reward points to lower your bill, and request your April monthly statement.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Laura Wilson"},
            },
            {
                "name": "get_bonus_points_balance",
                "arguments": {"account_number": "CC1012"},
            },
            {
                "name": "dispute_points_adjustment",
                "arguments": {
                    "account_number": "CC1012",
                    "dispute_reason": "Points not credited after last statement",
                },
            },
            {"name": "get_account_balance", "arguments": {"account_number": "CC1012"}},
            {
                "name": "apply_points_to_bill",
                "arguments": {"account_number": "CC1012", "points_to_apply": "3000"},
            },
            {
                "name": "get_monthly_statement",
                "arguments": {"account_number": "CC1012", "statement_month": "2025-04"},
            },
        ],
    },
    {
        "id": "entry_207",
        "tags": ["complex"],
        "instructions": "You are George Martinez. First, list all your transactions and then retrieve details of a gas station purchase. Update the transaction’s description, dispute the transaction if necessary, and finally check your account balance for confirmation.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "George Martinez"},
            },
            {"name": "list_transactions", "arguments": {"account_number": "CC1007"}},
            {"name": "get_transaction", "arguments": {"transaction_id": "TXN1013"}},
            {
                "name": "update_transaction",
                "arguments": {
                    "transaction_id": "TXN1013",
                    "new_amount": "95.5",
                    "new_description": "Gas station propane and snacks",
                },
            },
            {"name": "get_account_balance", "arguments": {"account_number": "CC1007"}},
        ],
    },
    {
        "id": "entry_218",
        "tags": ["complex"],
        "instructions": "You are Rachel Harris. Check your bonus points balance and retrieve your account details. Then, retrieve details of a recent bookstore transaction, update the transaction description if needed, and process a bill installment.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Rachel Harris"},
            },
            {
                "name": "get_bonus_points_balance",
                "arguments": {"account_number": "CC1018"},
            },
            {"name": "get_transaction", "arguments": {"transaction_id": "TXN1034"}},
            {
                "name": "pay_bill",
                "arguments": {"account_number": "CC1018", "payment_amount": "880"},
            },
        ],
    },
    {
        "id": "entry_216",
        "tags": ["complex"],
        "instructions": "You are Patricia Young. Begin by checking your account balance, then retrieve details of a recent online shopping transaction (TXN1030). Update the transaction amount to $60, list all your transactions to verify changes, and process a bill payment of $640.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Patricia Young"},
            },
            {"name": "get_account_balance", "arguments": {"account_number": "CC1016"}},
            {"name": "get_transaction", "arguments": {"transaction_id": "TXN1030"}},
            {
                "name": "update_transaction",
                "arguments": {
                    "transaction_id": "TXN1030",
                    "new_amount": "60",
                    "new_description": "",
                },
            },
            {"name": "list_transactions", "arguments": {"account_number": "CC1016"}},
            {
                "name": "pay_bill",
                "arguments": {"account_number": "CC1016", "payment_amount": "640"},
            },
        ],
    },
    {
        "id": "entry_210",
        "tags": ["complex"],
        "instructions": "You are Julia Kim. Check your current account balance and verify your account details. Retrieve details of a suspicious transaction, dispute it, and then redeem some reward points for cash to offset the expense.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Julia Kim"},
            },
            {"name": "get_account_balance", "arguments": {"account_number": "CC1010"}},
            {"name": "get_transaction", "arguments": {"transaction_id": "TXN1018"}},
            {
                "name": "dispute_transaction",
                "arguments": {
                    "transaction_id": "TXN1018",
                    "reason": "Suspicious transaction",
                },
            },
            {
                "name": "get_bonus_points_balance",
                "arguments": {"account_number": "CC1010"},
            },
            {
                "name": "redeem_points",
                "arguments": {
                    "account_number": "CC1010",
                    "points_to_redeem": "400",
                    "redemption_type": "Cash",
                },
            },
        ],
    },
    {
        "id": "entry_208",
        "tags": ["complex"],
        "instructions": "You are Hannah Rodriguez. Start by checking your bonus points balance and account balance. Then, process a bill payment of $20, redeem 500 reward points for a voucher, and apply an additional 70 reward points to further reduce your bill.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Hannah Rodriguez"},
            },
            {
                "name": "get_bonus_points_balance",
                "arguments": {"account_number": "CC1008"},
            },
            {"name": "get_account_balance", "arguments": {"account_number": "CC1008"}},
            {
                "name": "pay_bill",
                "arguments": {"account_number": "CC1008", "payment_amount": "20"},
            },
            {
                "name": "redeem_points",
                "arguments": {
                    "account_number": "CC1008",
                    "points_to_redeem": "500",
                    "redemption_type": "voucher",
                },
            },
            {
                "name": "apply_points_to_bill",
                "arguments": {"account_number": "CC1008", "points_to_apply": "70"},
            },
        ],
    },
    {
        "id": "entry_217",
        "tags": ["complex"],
        "instructions": "You are Quentin Baker. Request your monthly statement, list all your transactions, and retrieve details of a furniture purchase. Dispute the transaction if necessary, and finally check your account balance.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Quentin Baker"},
            },
            {
                "name": "get_monthly_statement",
                "arguments": {"account_number": "CC1017", "statement_month": "2025-04"},
            },
            {"name": "list_transactions", "arguments": {"account_number": "CC1017"}},
            {"name": "get_transaction", "arguments": {"transaction_id": "TXN1032"}},
            {"name": "get_account_balance", "arguments": {"account_number": "CC1017"}},
        ],
        "outputs": [
            "Furniture purchase",
            "130",
            "Lunch",
            "25",
            "310"
        ]
    },
    {
        "id": "entry_205",
        "tags": ["complex"],
        "instructions": "You are Edward Davis. Begin by requesting your monthly statement for March, then list your transactions. Identify a pharmacy transaction with an error and update it, process a bill payment, and redeem some reward points for cash.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Edward Davis"},
            },
            {
                "name": "get_monthly_statement",
                "arguments": {"account_number": "CC1005", "statement_month": "2025-03"},
            },
            {"name": "list_transactions", "arguments": {"account_number": "CC1005"}},
            {"name": "get_transaction", "arguments": {"transaction_id": "TXN1010"}},
            {
                "name": "update_transaction",
                "arguments": {
                    "transaction_id": "TXN1010",
                    "new_amount": "30.25",
                    "new_description": "Pharmacy",
                },
            },
            {
                "name": "pay_bill",
                "arguments": {"account_number": "CC1005", "payment_amount": "340.2"},
            },
            {
                "name": "get_bonus_points_balance",
                "arguments": {"account_number": "CC1005"},
            },
            {
                "name": "redeem_points",
                "arguments": {
                    "account_number": "CC1005",
                    "points_to_redeem": "5000",
                    "redemption_type": "Cash",
                },
            },
        ],
    },
    {
        "id": "entry_211",
        "tags": ["complex"],
        "instructions": "You are Kevin Turner. Review your account details and current balance, then request to update your credit card limit to $5000. Next, list your recent transactions, retrieve details of a specific transaction (TXN1021) for further inquiry, and process a bill payment of $980.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Kevin Turner"},
            },
            {"name": "get_account_balance", "arguments": {"account_number": "CC1011"}},
            {
                "name": "change_credit_card_limit",
                "arguments": {"account_number": "CC1011", "new_limit": "5000"},
            },
            {"name": "list_transactions", "arguments": {"account_number": "CC1011"}},
            {"name": "get_transaction", "arguments": {"transaction_id": "TXN1021"}},
            {
                "name": "pay_bill",
                "arguments": {"account_number": "CC1011", "payment_amount": "980"},
            },
        ],
    },
    {
        "id": "entry_220",
        "tags": ["complex"],
        "instructions": "You are Tina Clark. Prepare for a detailed review by getting account details and checking your account balance. Request your monthly statement for May, redeem 1,000 reward points for cash, and list your transactions to verify all recent activities.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Tina Clark"},
            },
            {"name": "get_account_balance", "arguments": {"account_number": "CC1020"}},
            {
                "name": "get_monthly_statement",
                "arguments": {"account_number": "CC1020", "statement_month": "2025-05"},
            },
            {
                "name": "redeem_points",
                "arguments": {
                    "account_number": "CC1020",
                    "points_to_redeem": "1000",
                    "redemption_type": "cash",
                },
            },
            {"name": "list_transactions", "arguments": {"account_number": "CC1020"}},
        ],
    },
    {
        "id": "entry_202",
        "tags": ["complex"],
        "instructions": "You are Bob Smith. Start by confirming your account details and current balance. Then, update your credit card limit, apply some reward points to lower your bill, list all your recent transactions, and dispute a points adjustment error that you noticed.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Bob Smith"},
            },
            {"name": "get_account_balance", "arguments": {"account_number": "CC1002"}},
            {
                "name": "change_credit_card_limit",
                "arguments": {"account_number": "CC1002", "new_limit": "5000"},
            },
            {
                "name": "get_bonus_points_balance",
                "arguments": {"account_number": "CC1002"},
            },
            {
                "name": "apply_points_to_bill",
                "arguments": {"account_number": "CC1002", "points_to_apply": "4500"},
            },
            {"name": "list_transactions", "arguments": {"account_number": "CC1002"}},
            {
                "name": "dispute_points_adjustment",
                "arguments": {
                    "account_number": "CC1002",
                    "dispute_reason": "Points adjustment error noticed on account",
                },
            },
        ],
    },
    {
        "id": "entry_203",
        "tags": ["complex"],
        "instructions": "You are Charlie Williams. Review a transaction from an electronics purchase (TXN1005) by retrieving its details, then update the transaction with the correct description. Next, list all your transactions, check your current account balance, and process a partial bill payment of $400.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Charlie Williams"},
            },
            {"name": "get_transaction", "arguments": {"transaction_id": "TXN1005"}},
            {
                "name": "update_transaction",
                "arguments": {
                    "transaction_id": "TXN1005",
                    "new_amount": "",
                    "new_description": "Online Electronics Purchase",
                },
            },
            {"name": "list_transactions", "arguments": {"account_number": "CC1003"}},
            {"name": "get_account_balance", "arguments": {"account_number": "CC1003"}},
            {
                "name": "pay_bill",
                "arguments": {"account_number": "CC1003", "payment_amount": "400"},
            },
        ],
    },
    {
        "id": "entry_209",
        "tags": ["complex"],
        "instructions": "You are Ian Lee. Request your monthly statement for May and list all your transactions. Retrieve details of a shopping transaction that appears incorrect, dispute that transaction, and update a restaurant transaction with the corrected amount of $40.",
        "actions": [
            {"name": "get_account_details", "arguments": {"account_holder": "Ian Lee"}},
            {
                "name": "get_monthly_statement",
                "arguments": {"account_number": "CC1009", "statement_month": "2025-05"},
            },
            {"name": "list_transactions", "arguments": {"account_number": "CC1009"}},
            {"name": "get_transaction", "arguments": {"transaction_id": "TXN1017"}},
            {
                "name": "dispute_transaction",
                "arguments": {"transaction_id": "TXN1017", "reason": "Overcharge"},
            },
            {
                "name": "update_transaction",
                "arguments": {
                    "transaction_id": "TXN1016",
                    "new_amount": "40",
                    "new_description": "",
                },
            },
        ],
    },
    {
        "id": "entry_204",
        "tags": ["complex"],
        "instructions": "You are Diana Brown. Check your bonus points balance and retrieve your account details. Then, look up the details of your recent hotel booking transaction, and apply some reward points to reduce your bill.",
        "actions": [
            {
                "name": "get_account_details",
                "arguments": {"account_holder": "Diana Brown"},
            },
            {
                "name": "get_bonus_points_balance",
                "arguments": {"account_number": "CC1004"},
            },
            {"name": "get_transaction", "arguments": {"transaction_id": "TXN1007"}},
            {
                "name": "apply_points_to_bill",
                "arguments": {"account_number": "CC1004", "points_to_apply": "5000"},
            },
        ],
    },
]
