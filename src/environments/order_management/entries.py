entries = [
    {
        "id": "entry_63",
        "instructions": "Your name is Michael Thompson. Your customer ID is C1013 and your email is michael.thompson@gap.com. You have an order with order ID O1033, and you need to check its shipping status. Do not provide the order ID until prompted. After confirmation, ask if you can update the shipping address to 415 Mission Street, San Francisco, CA 94105.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1013",
                    "verified_email": "michael.thompson@gap.com",
                },
            },
            {"name": "track_order", "arguments": {"order_id": "O1033"}},
            {
                "name": "update_shipping_address",
                "arguments": {
                    "order_id": "O1033",
                    "new_shipping_address": "415 Mission Street, San Francisco, CA 94105",
                },
            },
        ],
    },
    {
        "id": "entry_2",
        "instructions": "Your name is Bob Smith. Your customer ID is C1002 and your email address is bob.smith@gap.com. You have a recent order with order ID O1002, and you're wondering about your order status. Do not disclose the order ID until the agent specifically asks. Once the agent retrieves your order details, ask for the current tracking information. Provide your order ID only if the agent requests it, and do not volunteer additional details.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1002",
                    "verified_email": "bob.smith@gap.com",
                },
            },
            {"name": "get_order", "arguments": {"order_id": "O1002"}},
            {"name": "track_order", "arguments": {"order_id": "O1002"}},
        ],
        "outputs": [
            "456 Oak"
        ]
    },
    {
        "id": "entry_139",
        "instructions": "Your name is Diana Brown. Your customer ID is C1004 and your email address is diana.brown@gap.com. You have an order with order ID O1004, and you wish to check its details. Do not provide the order ID until the agent asks. Once confirmed, ask if you can update your billing address (123 Maple Avenue, Apt 12, Houston, TX 77003).",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1014",
                    "verified_email": "nina.anderson@gap.com",
                },
            },
            {"name": "get_order", "arguments": {"order_id": "O1004"}},
            {
                "name": "update_billing_address",
                "arguments": {
                    "order_id": "O1004",
                    "new_billing_address": "123 Maple Avenue, Apt 12, Houston, TX 77003",
                },
            },
        ],
    },
    {
        "id": "entry_12",
        "instructions": "Your name is Bob Smith. Your customer ID is C1002 and your email address is bob.smith@gap.com. You have an order with order ID O1012 and want to know the current status. Do not share the order ID until the agent asks. Once the status is confirmed, ask if you can request a refund due to a billing error.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1002",
                    "verified_email": "bob.smith@gap.com",
                },
            },
            {"name": "track_order", "arguments": {"order_id": "O1012"}},
            {
                "name": "request_refund",
                "arguments": {
                    "order_id": "O1012",
                    "refund_reason": "Overcharged for the order",
                },
            },
        ],
    },
    {
        "id": "entry_47",
        "instructions": "Your name is Vanessa Perez. Your customer ID is C1022 and your email address is vanessa.perez@gap.com. You have an order with order ID O1042, and you want to inquire about its tracking information. Hold off on sharing the order ID until prompted. After confirmation, ask if you can change the billing address.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1022",
                    "verified_email": "vanessa.perez@gap.com",
                },
            },
            {"name": "track_order", "arguments": {"order_id": "O1042"}},
            {
                "name": "update_billing_address",
                "arguments": {
                    "order_id": "O1042",
                    "new_billing_address": "123 New Street Apt 45B Springfield, IL 62701 USA",
                },
            },
        ],
    },
    {
        "id": "entry_59",
        "instructions": "Your name is Diana Brown. You need to check the details of your order with order ID O1014. Do not reveal the order ID until asked. After confirmation, ask if you can update your shipping address to 456 Oak Avenue, Apartment 12B, Austin, TX 73301 because it is incorrect.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "Diana Brown",
                    "verified_email": "diana.brown@gap.com",
                },
            },
            {"name": "get_order", "arguments": {"order_id": "O1014"}},
            {"name": "track_order", "arguments": {"order_id": "O1014"}},
            {
                "name": "update_shipping_address",
                "arguments": {
                    "order_id": "O1014",
                    "new_shipping_address": "456 Oak Avenue, Apartment 12B, Austin, TX 73301",
                },
            },
        ],
    },
    {
        "id": "entry_121",
        "instructions": "Your name is Ulysses Martinez. Your customer ID is C1021 and your email address is ulysses.martinez@gap.com. You have an order with order ID O1041, and you wish to verify its details. Do not reveal the order ID until the agent asks. Once confirmed, ask if you can update your shipping address.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1021",
                    "verified_email": "ulysses.martinez@gap.com",
                },
            },
            {"name": "get_order", "arguments": {"order_id": "O1041"}},
            {
                "name": "update_shipping_address",
                "arguments": {
                    "order_id": "O1041",
                    "new_shipping_address": "456 Oak Avenue, Apt 12C, Springfield, IL 62702",
                },
            },
        ],
    },
    {
        "id": "entry_107",
        "instructions": "Your name is George Martinez. Your customer ID is C1007 and your email address is george.martinez@gap.com. You have an order with order ID O1017, and you need to check the tracking information. Do not share the order ID until the agent asks. Once confirmed, ask if you can update your billing address.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1007",
                    "verified_email": "george.martinez@gap.com",
                },
            },
            {"name": "track_order", "arguments": {"order_id": "O1017"}},
            {
                "name": "update_billing_address",
                "arguments": {
                    "order_id": "O1017",
                    "new_billing_address": "123 Maple Street, Springfield, IL 62701",
                },
            },
        ],
    },
    {
        "id": "entry_55",
        "instructions": "Your name is Edward Davis. You want to review the details for your order with ID O1005. Do not provide the order ID until the agent asks. After confirmation, ask if you can update your shipping address to 123 Maplewood Lane, Evergreen Heights, CA 90210, due to a relocation.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1005",
                    "verified_email": "edward.davis@gap.com",
                },
            },
            {"name": "get_order", "arguments": {"order_id": "O1005"}},
            {
                "name": "update_shipping_address",
                "arguments": {
                    "order_id": "O1005",
                    "new_shipping_address": "123 Maplewood Lane, Evergreen Heights, CA 90210",
                },
            },
        ],
    },
    {
        "id": "entry_100",
        "instructions": "Your name is Julia Kim. Your customer ID is C1010 and your email address is julia.kim@gap.com. You have an order with order ID O1010, and you wish to check its delivery status. Do not share the order ID until prompted. After confirmation, ask if you can cancel the order due to a duplicate order.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1010",
                    "verified_email": "julia.kim@gap.com",
                },
            },
            {"name": "track_order", "arguments": {"order_id": "O1010"}},
            {"name": "cancel_order", "arguments": {"order_id": "O1010"}},
        ],
    },
    {
        "id": "entry_65",
        "instructions": "Your name is Julia Kim. Your customer ID is C1010 and your email address is julia.kim@gap.com. You have an order with order ID O1020, and you wish to verify its details. Hold off on providing the order ID until prompted. After confirmation, ask if you can update your billing address to 1234 Oak Street, Suite 200, Atlanta, GA 30309.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "Julia Kim",
                    "verified_email": "julia.kim@gap.com",
                },
            },
            {"name": "get_order", "arguments": {"order_id": "O1020"}},
            {
                "name": "update_billing_address",
                "arguments": {
                    "order_id": "O1020",
                    "new_billing_address": "1234 Oak Street, Suite 200, Atlanta, GA 30309",
                },
            },
        ],
    },
    {
        "id": "entry_67",
        "instructions": "Your name is Bob Smith. Your customer ID is C1002 and your email address is bob.smith@gap.com. You have an order with order ID O1022, and you wish to review its tracking details. Do not provide the order ID until the agent requests it. After confirmation, ask if you can update your shipping address (415 Mission Street, 3rd Floor, San Francisco, CA 94105, United States).",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1002",
                    "verified_email": "bob.smith@gap.com",
                },
            },
            {"name": "track_order", "arguments": {"order_id": "O1022"}},
            {
                "name": "update_shipping_address",
                "arguments": {
                    "order_id": "O1022",
                    "new_shipping_address": "415 Mission Street, 3rd Floor, San Francisco, CA 94105, United States",
                },
            },
        ],
    },
    {
        "id": "entry_147",
        "instructions": "Your name is Vanessa Perez. Your customer ID is C1022 and your email address is vanessa.perez@gap.com. You have an order with order ID O1042, and you wish to check its tracking details. Do not provide the order ID until requested. Once confirmed, ask if you can cancel the order due to an incorrect shipment.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1022",
                    "verified_email": "vanessa.perez@gap.com",
                },
            },
            {"name": "track_order", "arguments": {"order_id": "O1042"}},
            {"name": "cancel_order", "arguments": {"order_id": "O1042"}},
        ],
    },
    {
        "id": "entry_56",
        "instructions": "Your name is Fiona Garcia. Your customer ID is C1006 and your email address is fiona.garcia@gap.com. You have an order with order ID O1006, and you want to know its delivery status. Do not disclose the order ID until requested. Once confirmed, ask if you can cancel the order because of an error.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1006",
                    "verified_email": "fiona.garcia@gap.com",
                },
            },
            {"name": "track_order", "arguments": {"order_id": "O1006"}},
            {"name": "cancel_order", "arguments": {"order_id": "O1006"}},
        ],
    },
    {
        "id": "entry_14",
        "instructions": "Your name is Nina Anderson. Your customer ID is C1014 and your email address is nina.anderson@gap.com. You have an order with order ID O1034 and wish to check if it has been delivered. Do not provide the order ID until prompted. Once confirmed, ask if you can initiate a return because the item is defective.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1014",
                    "verified_email": "nina.anderson@gap.com",
                },
            },
            {"name": "track_order", "arguments": {"order_id": "O1034"}},
            {"name": "confirm_delivery", "arguments": {"order_id": "O1034"}},
            {
                "name": "return_order",
                "arguments": {"order_id": "O1034", "return_reason": "Defective item"},
            },
        ],
    },
    {
        "id": "entry_120",
        "instructions": "Your name is Tina Lewis. You want to know the delivery status of your order with ID O1040. Do not provide the order ID until prompted. After confirmation, ask if you can apply coupon code GAP10 for a discount.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1020",
                    "verified_email": "tina.lewis@gap.com",
                },
            },
            {"name": "get_order", "arguments": {"order_id": "O1040"}},
            {"name": "track_order", "arguments": {"order_id": "O1040"}},
            {
                "name": "apply_coupon",
                "arguments": {"order_id": "O1040", "coupon_code": "GAP10"},
            },
        ],
    },
    {
        "id": "entry_38",
        "instructions": "Your name is Michael Thompson. Your customer ID is C1013 and your email address is michael.thompson@gap.com. You have an order with order ID O1033 and need to check its tracking status. Do not provide the order ID until the agent asks. Once confirmed, ask if you can cancel the order if the shipment is delayed.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1013",
                    "verified_email": "michael.thompson@gap.com",
                },
            },
            {"name": "track_order", "arguments": {"order_id": "O1033"}},
            {"name": "cancel_order", "arguments": {"order_id": "O1033"}},
        ],
    },
    {
        "id": "entry_15",
        "instructions": "Your name is Oliver Garcia. Your customer ID is C1015 and your email is oliver.garcia@gap.com. You have an order with order ID O1035 and want to verify its details. Do not mention the order ID until the agent asks. After confirmation, ask to update the billing address due to a recent change in payment method.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1015",
                    "verified_email": "oliver.garcia@gap.com",
                },
            },
            {"name": "get_order", "arguments": {"order_id": "O1035"}},
            {
                "name": "update_billing_address",
                "arguments": {
                    "order_id": "O1035",
                    "new_billing_address": "789 Pine St, Apt 5B, Miami, FL 33102",
                },
            },
        ],
    },
    {
        "id": "entry_116",
        "instructions": "Your name is Pamela Scott. You want to track your order with order ID O1036. Do not provide the order ID until requested. After confirmation, ask if you can apply a coupon code SAVE15 for savings.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1016",
                    "verified_email": "pamela.scott@gap.com",
                },
            },
            {"name": "get_order", "arguments": {"order_id": "O1036"}},
            {"name": "track_order", "arguments": {"order_id": "O1036"}},
            {
                "name": "apply_coupon",
                "arguments": {"order_id": "O1036", "coupon_code": "SAVE15"},
            },
        ],
    },
    {
        "id": "entry_143",
        "instructions": "Your name is Hannah Rodriguez. You wish to review the details of your order with order ID O1008. Do not provide the order ID until the agent requests it. Once confirmed, ask if you can return the order due to a duplicate entry.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1008",
                    "verified_email": "hannah.rodriguez@gap.com",
                },
            },
            {"name": "get_order", "arguments": {"order_id": "O1008"}},
            {
                "name": "return_order",
                "arguments": {"order_id": "O1008", "return_reason": "Duplicate entry"},
            },
        ],
    },
    {
        "id": "entry_39",
        "instructions": "Your name is Samuel Clark. You want to review the details of your order with order ID O1039. Do not reveal the order ID until requested. After confirmation, ask if you can initiate a return because the item is not as expected.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1019",
                    "verified_email": "samuel.clark@gap.com",
                },
            },
            {"name": "get_order", "arguments": {"order_id": "O1039"}},
            {
                "name": "return_order",
                "arguments": {
                    "order_id": "O1039",
                    "return_reason": "The item was not as expected",
                },
            },
        ],
    },
    {
        "id": "entry_77",
        "instructions": "Your name is Laura Wilson. You want to know the current status of your order with order ID O1032. Do not reveal the order ID until the agent asks. Once confirmed, ask if you can update your billing address to 888 Park Ave, Suite 300, Los Angeles, CA 90017.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C012",
                    "verified_email": "laura.wilson@gap.com",
                },
            },
            {"name": "get_order", "arguments": {"order_id": "O1032"}},
            {
                "name": "update_billing_address",
                "arguments": {
                    "order_id": "O1032",
                    "new_billing_address": "888 Park Ave, Suite 300, Los Angeles, CA 90017",
                },
            },
        ],
        "outputs": [
            "888 Park"
        ]
    },
    {
        "id": "entry_99",
        "instructions": "Your name is Ian Lee. You want to track your order with order ID O1019. Do not reveal the order ID until the agent asks. Once confirmed, ask if you can update your shipping address to 123 Maple Street, Apt 4B, Springfield, IL 62704, USA.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1009",
                    "verified_email": "ian.lee@gap.com",
                },
            },
            {"name": "get_order", "arguments": {"order_id": "O1019"}},
            {"name": "track_order", "arguments": {"order_id": "O1019"}},
            {
                "name": "update_shipping_address",
                "arguments": {
                    "order_id": "O1019",
                    "new_shipping_address": "123 Maple Street, Apt 4B, Springfield, IL 62704, USA",
                },
            },
        ],
    },
    {
        "id": "entry_108",
        "instructions": "Your name is Hannah Rodriguez. Your customer ID is C1008 and your email is hannah.rodriguez@gap.com. You have an order with order ID O1028, and you wish to review its details. Do not provide the order ID until prompted. After confirmation, ask if you can cancel the order due to a duplicate entry.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1008",
                    "verified_email": "hannah.rodriguez@gap.com",
                },
            },
            {"name": "get_order", "arguments": {"order_id": "O1028"}},
            {"name": "cancel_order", "arguments": {"order_id": "O1028"}},
        ],
    },
    {
        "id": "entry_123",
        "instructions": "Your name is William Rodriguez. You wish to review the details of your order with order ID O1043. Do not reveal the order ID until the agent asks. Once confirmed, ask if you can cancel the order due to incorrect items.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1023",
                    "verified_email": "william.rodriguez@gap.com",
                },
            },
            {"name": "get_order", "arguments": {"order_id": "O1043"}},
            {"name": "cancel_order", "arguments": {"order_id": "O1043"}},
        ],
    },
    {
        "id": "entry_7",
        "instructions": "Your name is Alice Johnson. Your customer ID is C1001 and your email address is alice.johnson@gap.com. You have an order with order ID O1001 and need to verify its shipping address. Do not disclose the order ID until the agent prompts you. Once confirmed, request a change to the shipping address to 256 Oak Ave, Unit 12B, Cambridge, MA 02139 due to a recent relocation.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1001",
                    "verified_email": "alice.johnson@gap.com",
                },
            },
            {"name": "get_order", "arguments": {"order_id": "O1001"}},
            {
                "name": "update_shipping_address",
                "arguments": {
                    "order_id": "O1001",
                    "new_shipping_address": "256 Oak Ave, Unit 12B, Cambridge, MA 02139",
                },
            },
        ],
    },
    {
        "id": "entry_36",
        "instructions": "Your name is Pamela Scott. Your customer ID is C1016 and your email address is pamela.scott@gap.com. You have an order with order ID O1036 and want to verify the order status. Do not reveal the order ID until prompted. After confirmation, ask if you can initiate a refund due to an overcharge.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1016",
                    "verified_email": "pamela.scott@gap.com",
                },
            },
            {"name": "get_order", "arguments": {"order_id": "O1036"}},
            {
                "name": "request_refund",
                "arguments": {
                    "order_id": "O1036",
                    "refund_reason": "Overcharge due to a discrepancy between the listed price and the final amount charged at checkout.",
                },
            },
        ],
    },
    {
        "id": "entry_22",
        "instructions": "Your name is Bob Smith. Your customer ID is C1002 and your email address is bob.smith@gap.com. You have an order with order ID O1022 and need to review the order details. Do not reveal the order ID until prompted. Once confirmed, ask if you can cancel the order because of a duplicate purchase.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1002",
                    "verified_email": "bob.smith@gap.com",
                },
            },
            {"name": "get_order", "arguments": {"order_id": "O1022"}},
            {"name": "cancel_order", "arguments": {"order_id": "O1022"}},
        ],
    },
    {
        "id": "entry_31",
        "instructions": "Your name is Kevin Moore. Your customer ID is C1011 and your email address is kevin.moore@gap.com. You have an order with order ID O1031 and need to check the order status. Do not reveal the order ID until prompted. After confirmation, ask if you can apply a coupon code to the order.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1011",
                    "verified_email": "kevin.moore@gap.com",
                },
            },
            {"name": "track_order", "arguments": {"order_id": "O1031"}},
            {
                "name": "apply_coupon",
                "arguments": {"order_id": "O1031", "coupon_code": "SAVE20"},
            },
        ],
    },
    {
        "id": "entry_138",
        "instructions": "Your name is Michael Thompson. You want to track your order with order ID O1033. Do not reveal the order ID until requested. After confirmation, ask if you can return the order due to an error with the order.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1013",
                    "verified_email": "michael.thompson@gap.com",
                },
            },
            {"name": "get_order", "arguments": {"order_id": "O1033"}},
            {"name": "track_order", "arguments": {"order_id": "O1033"}},
            {
                "name": "return_order",
                "arguments": {
                    "order_id": "O1033",
                    "return_reason": "Error with the order",
                },
            },
        ],
    },
    {
        "id": "entry_102",
        "instructions": "Your name is Alice Johnson. Your customer ID is C1001 and your email address is alice.johnson@gap.com. You have an order with order ID O1001, and you need to check its tracking details. Hold off on revealing the order ID until prompted. After confirmation, ask if you can apply the coupon code SAVE20.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1001",
                    "verified_email": "alice.johnson@gap.com",
                },
            },
            {"name": "track_order", "arguments": {"order_id": "O1001"}},
            {
                "name": "apply_coupon",
                "arguments": {"order_id": "O1001", "coupon_code": "SAVE20"},
            },
        ],
    },
    {
        "id": "entry_28",
        "instructions": "Your name is Hannah Rodriguez. Your customer ID is C1008 and your email address is hannah.rodriguez@gap.com. You have an order with order ID O1028 and need to check the current order status. Hold off on providing the order ID until the agent asks. Once confirmed, ask if you can cancel the order due to a change of mind.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1008",
                    "verified_email": "hannah.rodriguez@gap.com",
                },
            },
            {"name": "track_order", "arguments": {"order_id": "O1028"}},
            {"name": "cancel_order", "arguments": {"order_id": "O1028"}},
        ],
    },
    {
        "id": "entry_129",
        "instructions": "Your name is Samuel Clark. You wish to verify its details the details of your order with order ID O1039. Hold off on sharing the order ID until prompted. Once confirmed, ask if you can initiate a return due to a defect in one of the items.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1019",
                    "verified_email": "samuel.clark@gap.com",
                },
            },
            {"name": "get_order", "arguments": {"order_id": "O1039"}},
            {
                "name": "return_order",
                "arguments": {
                    "order_id": "O1039",
                    "return_reason": "Defect in one of the items",
                },
            },
        ],
    },
    {
        "id": "entry_98",
        "instructions": "Your name is William Rodriguez. Your customer ID is C1023 and your email address is william.rodriguez@gap.com. You have an order with order ID O1043, and you need to review the order status. Hold off on providing the order ID until requested. After confirmation, ask if you can apply a coupon code for a discount.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1023",
                    "verified_email": "william.rodriguez@gap.com",
                },
            },
            {"name": "track_order", "arguments": {"order_id": "O1043"}},
            {
                "name": "apply_coupon",
                "arguments": {"order_id": "O1043", "coupon_code": "SAVE20"},
            },
        ],
    },
    {
        "id": "entry_43",
        "instructions": "Your name is William Rodriguez. Your customer ID is C1023 and your email address is william.rodriguez@gap.com. You have an order with order ID O1043 and wish to review its details. Do not disclose the order ID until the agent asks. After confirmation, ask if you can initiate a refund for a billing error.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1023",
                    "verified_email": "william.rodriguez@gap.com",
                },
            },
            {"name": "get_order", "arguments": {"order_id": "O1043"}},
            {
                "name": "request_refund",
                "arguments": {"order_id": "O1043", "refund_reason": "Billing error"},
            },
        ],
    },
    {
        "id": "entry_104",
        "instructions": "Your name is Diana Brown. Your customer ID is C1004 and your email address is diana.brown@gap.com. You have an order with order ID O1014, and you want to verify its delivery status. Do not reveal the order ID until asked. After confirmation, ask if you can initiate a return due to a damaged item.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1004",
                    "verified_email": "diana.brown@gap.com",
                },
            },
            {"name": "track_order", "arguments": {"order_id": "O1014"}},
            {
                "name": "return_order",
                "arguments": {"order_id": "O1014", "return_reason": "damaged item"},
            },
        ],
    },
    {
        "id": "entry_101",
        "instructions": "Your name is Alice Johnson. You want to verify the details of your order with order ID O1011. Do not provide the order ID until the agent asks. Once confirmed, ask if you can update your billing address to 456 Elm St, Apt 10C, New York, NY 10002.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1001",
                    "verified_email": "alice.johnson@gap.com",
                },
            },
            {"name": "get_order", "arguments": {"order_id": "O1011"}},
            {
                "name": "update_billing_address",
                "arguments": {
                    "order_id": "O1011",
                    "new_billing_address": "456 Elm St, Apt 10C, New York, NY 10002",
                },
            },
        ],
    },
    {
        "id": "entry_71",
        "instructions": "Your name is Fiona Garcia. Your customer ID is C1006 and your email address is fiona.garcia@gap.com. You have an order with order ID O1026, and you wish to verify its tracking information. Do not reveal the order ID until requested. After confirmation, ask if you can apply a coupon code for a discount.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1006",
                    "verified_email": "fiona.garcia@gap.com",
                },
            },
            {"name": "track_order", "arguments": {"order_id": "O1026"}},
            {
                "name": "apply_coupon",
                "arguments": {"order_id": "O1026", "coupon_code": "SAVE20"},
            },
        ],
    },
    {
        "id": "entry_85",
        "instructions": "Your name is Tina Lewis. You want to track your order with order ID O1040. Do not reveal the order ID until the agent asks. Once confirmed, ask if you can update your billing address to 123 Maple Street, Springfield, IL, 62701.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1020",
                    "verified_email": "tina.lewis@gap.com",
                },
            },
            {"name": "get_order", "arguments": {"order_id": "O1040"}},
            {"name": "track_order", "arguments": {"order_id": "O1040"}},
            {
                "name": "update_billing_address",
                "arguments": {
                    "order_id": "O1040",
                    "new_billing_address": "123 Maple Street, Springfield, IL, 62701",
                },
            },
        ],
    },
    {
        "id": "entry_34",
        "instructions": "Your name is Alice Johnson. Your customer ID is C1001 and your email address is alice.johnson@gap.com. You have an order with order ID O1001 and want to know if a return has been initiated. Do not reveal the order ID until requested. After confirmation, ask if you can update the shipping address.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1001",
                    "verified_email": "alice.johnson@gap.com",
                },
            },
            {"name": "track_order", "arguments": {"order_id": "O1001"}},
            {
                "name": "update_shipping_address",
                "arguments": {
                    "order_id": "O1001",
                    "new_shipping_address": "123 Main St, Apt 4B, New York, NY 10001",
                },
            },
        ],
        "outputs": [
            "123 Main"
        ]
    },
    {
        "id": "entry_3",
        "instructions": "Your name is Charlie Williams. Your customer ID is C1003 and your email address is charlie.williams@gap.com. Your order O1003 was delivered recently, but one of the items arrived damaged. Do not reveal your order ID until the agent requests it. After the agent confirms your order details, you will request a refund or initiate a return. When asked for the reason, state that the item was damaged, and only provide the order ID if explicitly prompted.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1003",
                    "verified_email": "charlie.williams@gap.com",
                },
            },
            {"name": "track_order", "arguments": {"order_id": "O1003"}},
            {"name": "confirm_delivery", "arguments": {"order_id": "O1003"}},
            {
                "name": "return_order",
                "arguments": {
                    "order_id": "O1003",
                    "return_reason": "Item damaged during delivery",
                },
            },
        ],
    },
    {
        "id": "entry_96",
        "instructions": "Your name is Charlie Williams. Your customer ID is C1003 and your email address is charlie.williams@gap.com. You have an order with order ID O1003, and you want to verify its delivery status. Do not reveal the order ID until prompted. After confirmation, ask if you can initiate a return because the product is defective.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1003",
                    "verified_email": "charlie.williams@gap.com",
                },
            },
            {"name": "track_order", "arguments": {"order_id": "O1003"}},
            {
                "name": "return_order",
                "arguments": {
                    "order_id": "O1003",
                    "return_reason": "product is defective",
                },
            },
        ],
    },
    {
        "id": "entry_80",
        "instructions": "Your name is Xavier Johnson. You want to verify the details on your order with order ID O1044. Do not reveal the order ID until requested. After confirmation, ask if you can initiate a refund because the product did not meet expectations and was unsatisfactory in quality.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "Xavier Johnson",
                    "verified_email": "xavier.johnson@gap.com",
                },
            },
            {"name": "get_order", "arguments": {"order_id": "O1044"}},
            {
                "name": "request_refund",
                "arguments": {
                    "order_id": "O1044",
                    "refund_reason": "The product did not meet expectations and was unsatisfactory in quality",
                },
            },
        ],
    },
    {
        "id": "entry_54",
        "instructions": "Your name is Hannah Rodriguez. Your customer ID is C1008 and your email address is hannah.rodriguez@gap.com. You have an order with order ID O1008, and you need to check its tracking information. Do not share the order ID until prompted. Once confirmed, ask if you can initiate a refund due to shipping delays.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1008",
                    "verified_email": "hannah.rodriguez@gap.com",
                },
            },
            {"name": "track_order", "arguments": {"order_id": "O1008"}},
            {
                "name": "request_refund",
                "arguments": {"order_id": "O1008", "refund_reason": "Shipping delays"},
            },
        ],
    },
    {
        "id": "entry_10",
        "instructions": "Your name is Julia Kim. Your customer ID is C1010 and your email address is julia.kim@gap.com. You have an order with order ID O1010 and want to review your order history. Do not reveal the order ID until asked. Once the order details are confirmed, ask to cancel the order if it has not been shipped yet.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1010",
                    "verified_email": "julia.kim@gap.com",
                },
            },
            {"name": "get_order_history", "arguments": {"customer_id": "C1010"}},
            {"name": "track_order", "arguments": {"order_id": "O1010"}},
            {"name": "cancel_order", "arguments": {"order_id": "O1010"}},
        ],
    },
    {
        "id": "entry_26",
        "instructions": "Your name is Alice Johnson. You want to check the tracking number on your order with order ID O1021.. Do not reveal the order ID until the agent asks. After confirmation, ask if you can request a refund because the shipping cost was higher than initially quoted during checkout.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1001",
                    "verified_email": "alice.johnson@gap.com",
                },
            },
            {"name": "get_order", "arguments": {"order_id": "O1021"}},
            {"name": "track_order", "arguments": {"order_id": "O1021"}},
            {
                "name": "request_refund",
                "arguments": {
                    "order_id": "O1021",
                    "refund_reason": "Shipping cost was higher than initially quoted during checkout",
                },
            },
        ],
    },
    {
        "id": "entry_61",
        "instructions": "Your name is Fiona Garcia. Your customer ID is C1006 and your email address is fiona.garcia@gap.com. You have an order with order ID O1016, and you want to check the tracking number. Hold off on revealing the order ID until requested. After confirmation, ask if you can update your billing address.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1006",
                    "verified_email": "fiona.garcia@gap.com",
                },
            },
            {"name": "track_order", "arguments": {"order_id": "O1016"}},
            {
                "name": "update_billing_address",
                "arguments": {
                    "order_id": "O1016",
                    "new_billing_address": "123 Elm Street, Springfield, IL 62701",
                },
            },
        ],
    },
    {
        "id": "entry_207",
        "tags": ["complex"],
        "instructions": "Your name is Fiona Garcia, customer ID C1006, email fiona.garcia@gap.com. 1. Confirm your identity, then retrieve your order history. 2. Check the status of O1006. 3. Apply the coupon code 'GAP20' to O1006 if it is 'processing.' 4. You notice order O1016 also belongs to you, so you decide to cancel O1016.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1006",
                    "verified_email": "fiona.garcia@gap.com",
                },
            },
            {"name": "get_order_history", "arguments": {"customer_id": "C1006"}},
            {"name": "track_order", "arguments": {"order_id": "O1006"}},
            {
                "name": "apply_coupon",
                "arguments": {"order_id": "O1006", "coupon_code": "GAP20"},
            },
            {"name": "get_order", "arguments": {"order_id": "O1016"}},
            {"name": "cancel_order", "arguments": {"order_id": "O1016"}},
        ],
    },
    {
        "id": "entry_208",
        "tags": ["complex"],
        "instructions": "Your name is George Martinez, customer ID C1007, email george.martinez@gap.com. 1. Confirm identity. 2. Create a new order (say O1100) for item SKU111, shipping to '135 Elm St, Apt 7D, Boston, MA 02108', billing address the same, total 120. 3. Apply the coupon code 'GAP5' immediately to this new order. 4. Track this new order to see if it has a tracking number. 5. You realize the coupon was the wrong one, so remove it. 6. Finally, request a refund for an older delivered order O1007, reason 'Billing error'.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1007",
                    "verified_email": 'george.martinez@gap.com"',
                },
            },
            {
                "name": "create_order",
                "arguments": {
                    "order_id": "O1100",
                    "customer_id": "C1007",
                    "shipping_address": "135 Elm St, Apt 7D, Boston, MA 02108",
                    "billing_address": "135 Elm St, Apt 7D, Boston, MA 02108",
                    "items": "SKU111",
                    "order_status": "processing",
                    "total_amount": "120",
                    "coupon_code": "GAP5",
                },
            },
            {"name": "track_order", "arguments": {"order_id": "O1100"}},
            {"name": "remove_coupon", "arguments": {"order_id": "O1100"}},
            {
                "name": "request_refund",
                "arguments": {"order_id": "O1100", "refund_reason": "Billing error"},
            },
        ],
    },
    {
        "id": "entry_201",
        "tags": ["complex"],
        "instructions": "Your name is Laura Wilson, your customer ID is C1012, and your email is laura.wilson@gap.com. Ask the agent to list all your past orders. After that, track the order with ID O1032 to see its current status. Apply the coupon code 'LADEAL' to order O1032 if it has not yet been applied. Next, update the shipping address of O1032 to '1010 Beverly Blvd, Los Angeles, CA 90048' if the order has not yet shipped. ",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1012",
                    "verified_email": "laura.wilson@gap.com",
                },
            },
            {"name": "list_orders", "arguments": {"customer_id": "C1012"}},
            {"name": "track_order", "arguments": {"order_id": "O1032"}},
        ],
        "outputs": [
            "888 Park"
        ]
    },
    {
        "id": "entry_211",
        "tags": ["complex"],
        "instructions": "Your name is Julia Kim, customer ID C1010, email julia.kim@gap.com. Ask the agent to list all your orders. Retrieve details of order O1010 specifically. Check if there's any coupon code on O1010. If not, you remove a coupon from O1020 and apply it to O1010, if available. Finally, ask the agent to generate an order report for '2025-04-10' to verify shipping progress.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1010",
                    "verified_email": "julia.kim@gap.com",
                },
            },
            {"name": "list_orders", "arguments": {"customer_id": "C1010"}},
            {"name": "track_order", "arguments": {"order_id": "O1010"}},
            {
                "name": "generate_order_report",
                "arguments": {"report_date": "2025-04-10"},
            },
        ],
        "outputs": [
            "159 Poplar"
        ]
    },
    {
        "id": "entry_209",
        "tags": ["complex"],
        "instructions": "Your name is Hannah Rodriguez, customer ID C1008, email hannah.rodriguez@gap.com. 1. Confirm your identity and track order O1008 (currently shipped). 2. Update the shipping address mid-transit to '246 Spruce Ln, Suite 5, Denver, CO 80203'. 3. Also update the billing address to '111 Pine Rd, Denver, CO 80203'. 4. Then you decide to return the entire order, stating reason 'Ordered too many units.' ",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1008",
                    "verified_email": "hannah.rodriguez@gap.com",
                },
            },
            {"name": "get_order", "arguments": {"order_id": "O1008"}},
            {"name": "track_order", "arguments": {"order_id": "O1008"}},
            {
                "name": "update_shipping_address",
                "arguments": {
                    "order_id": "O1008",
                    "new_shipping_address": "246 Spruce Ln, Suite 5, Denver, CO 80203",
                },
            },
            {
                "name": "update_billing_address",
                "arguments": {
                    "order_id": "O1008",
                    "new_billing_address": "111 Pine Rd, Denver, CO 80203",
                },
            },
            {
                "name": "return_order",
                "arguments": {
                    "order_id": "O1008",
                    "return_reason": "Ordered too many units",
                },
            },
        ],
    },
    {
        "id": "entry_203",
        "tags": ["complex"],
        "instructions": "Your name is Bob Smith, customer ID C1002, email bob.smith@gap.com. You received a package with order ID O1002 early and want to mark it delivered. However, you discover an item is defective, so you initiate a return with the reason 'Defective item.' Request a refund for the defective product. ",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1002",
                    "verified_email": "bob.smith@gap.com",
                },
            },
            {"name": "track_order", "arguments": {"order_id": "O1002"}},
            {"name": "confirm_delivery", "arguments": {"order_id": "O1002"}},
            {
                "name": "return_order",
                "arguments": {"order_id": "O1002", "return_reason": "Defective item"},
            },
            {
                "name": "request_refund",
                "arguments": {"order_id": "O1002", "refund_reason": "Defective item"},
            },
        ],
    },
    {
        "id": "entry_220",
        "tags": ["complex"],
        "instructions": "Your name is Samuel Clark, customer ID C1019, email samuel.clark@gap.com.  Retrieve your full order history. Remove any coupons from your order O1039 if it has not yet been delivered. Order O1039 has been delivered, so you request a refund with the reason 'Delayed arrival'. Finally, generate a report for '2025-05-09' to see when it was created.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1019",
                    "verified_email": "samuel.clark@gap.com",
                },
            },
            {"name": "get_order_history", "arguments": {"customer_id": "C1019"}},
            {"name": "track_order", "arguments": {"order_id": "O1039"}},
            {
                "name": "request_refund",
                "arguments": {"order_id": "O1039", "refund_reason": "Delayed arrival"},
            },
            {
                "name": "generate_order_report",
                "arguments": {"report_date": "2025-05-09"},
            },
        ],
    },
    {
        "id": "entry_280",
        "tags": ["complex"],
        "instructions": "Your name is Diana Brown, customer ID C1004, email diana.brown@gap.com. Confirm your identity. Create a new order for item 'SKU505', shipping to '321 Cedar St, Unit 5, Houston, TX 77002', billing address the same, total amount 59.99. Apply 'GAP5' to this new order. Realizing you put the wrong shipping address, update it to '999 Cedar St, Unit 5, Houston, TX 77002'. You change your mind about using the coupon, so remove it from the order. Lastly, generate an order report for the date you created it, to verify the final amount.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1004",
                    "verified_email": "diana.brown@gap.com",
                },
            },
            {
                "name": "create_order",
                "arguments": {
                    "order_id": "O1047",
                    "customer_id": "C1004",
                    "shipping_address": "321 Cedar St, Unit 5, Houston, TX 77002",
                    "billing_address": "321 Cedar St, Unit 5, Houston, TX 77002",
                    "items": "SKU505",
                    "order_status": "processing",
                    "total_amount": "59.99",
                    "coupon_code": "GAP5",
                },
            },
            {
                "name": "update_shipping_address",
                "arguments": {
                    "order_id": "O1044",
                    "new_shipping_address": "999 Cedar St, Unit 5, Houston, TX 77002",
                },
            },
            {"name": "remove_coupon", "arguments": {"order_id": "O1044"}},
            {
                "name": "generate_order_report",
                "arguments": {"report_date": "2025-04-30"},
            },
        ],
    },
    {
        "id": "entry_217",
        "tags": ["complex"],
        "instructions": "Your name is Pamela Scott, customer ID C1016, email pamela.scott@gap.com. 1. Confirm identity and list all your orders. 2. Update the status of O1036 from 'processing' to 'delivered' since you received it early. 3. You decide to return O1036 with reason 'Not what I expected'. 4. Request a refund for the same order, reason 'Didn't meet my expectations'. 5. Also remove any coupon if it was applied. 6. Verify everything is recorded properly.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1016",
                    "verified_email": "pamela.scott@gap.com",
                },
            },
            {"name": "list_orders", "arguments": {"customer_id": "C1016"}},
            {
                "name": "update_order",
                "arguments": {"order_id": "O1036", "order_status": "delivered"},
            },
            {
                "name": "return_order",
                "arguments": {
                    "order_id": "O1036",
                    "return_reason": "Not what I expected",
                },
            },
            {
                "name": "request_refund",
                "arguments": {
                    "order_id": "O1036",
                    "refund_reason": "Didn't meet my expectations",
                },
            },
            {"name": "remove_coupon", "arguments": {"order_id": "O1036"}},
            {"name": "get_order", "arguments": {"order_id": "O1036"}},
        ],
    },
    {
        "id": "entry_212",
        "tags": ["complex"],
        "instructions": "Your name is Kevin Moore, customer ID C1011, email kevin.moore@gap.com. Confirm your identity. Track O1031. Update the billing address on O1031 to '888 Third Ave, New York, NY 10022'. Once O1031 arrives, return O1031 with reason 'Size does not fit'. Request a refund for O1031, reason 'Didn't fit me at all'. Finally, you want to apply a coupon code to your next order if possible.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1011",
                    "verified_email": "kevin.moore@gap.com",
                },
            },
            {"name": "track_order", "arguments": {"order_id": "O1031"}},
            {
                "name": "update_billing_address",
                "arguments": {
                    "order_id": "O1031",
                    "new_billing_address": "888 Third Ave, New York, NY 10022",
                },
            },
            {
                "name": "return_order",
                "arguments": {
                    "order_id": "O1031",
                    "return_reason": "Didn't fit me at all",
                },
            },
            {
                "name": "request_refund",
                "arguments": {
                    "order_id": "O1031",
                    "refund_reason": "Didn't fit me at all",
                },
            },
        ],
    },
    {
        "id": "entry_215",
        "tags": ["complex"],
        "instructions": "Your name is Nina Anderson, customer ID C1014, email nina.anderson@gap.com. Confirm your identity. You have order O1034 that was delivered; track it for a final status check. If there's a coupon code attached, remove it. A few days later, you decide to return O1034 with reason 'Color mismatch'. Then you request a refund for that returned order, same reason. Check that everything is processed.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1014",
                    "verified_email": "nina.anderson@gap.com",
                },
            },
            {"name": "track_order", "arguments": {"order_id": "O1034"}},
            {
                "name": "return_order",
                "arguments": {"order_id": "O1034", "return_reason": "Color mismatch"},
            },
            {
                "name": "request_refund",
                "arguments": {"order_id": "O1034", "refund_reason": "Color mismatch"},
            },
            {"name": "get_order", "arguments": {"order_id": "O1034"}},
        ],
    },
    {
        "id": "entry_204",
        "tags": ["complex"],
        "instructions": "Your name is Charlie Williams, customer ID C1003, email charlie.williams@gap.com. Confirm your identity. List all your orders. You see that order O1013 is still processing, so you want to cancel it now. Then update the billing address of order O1003 (which is delivered) to '202 Pinewood Dr, Chicago, IL 60605' for your records. Finally, generate an order report for the date '2025-04-13' to confirm your purchases.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1003",
                    "verified_email": "charlie.williams@gap.com",
                },
            },
            {"name": "list_orders", "arguments": {"customer_id": "C1003"}},
            {"name": "cancel_order", "arguments": {"order_id": "O1013"}},
            {
                "name": "update_billing_address",
                "arguments": {
                    "order_id": "O1003",
                    "new_billing_address": "202 Pinewood Dr, Chicago, IL 60605",
                },
            },
            {
                "name": "generate_order_report",
                "arguments": {"report_date": "2025-04-13"},
            },
        ],
    },
    {
        "id": "entry_219",
        "tags": ["complex"],
        "instructions": "Your name is Rachel Adams, customer ID C1018, email rachel.adams@gap.com. 1. Confirm identity, then list all your orders. 2. You see an order O1038 which is 'processing', so you try to apply the coupon code 'DENVER10' to it. 3. Track O1038 to see if it has shipped yet. 4. Suddenly, you decide to cancel O1038 before it can ship. 5. For any delivered order, you also want to initiate a return with reason 'Wrong size'.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1018",
                    "verified_email": "rachel.adams@gap.com",
                },
            },
            {"name": "list_orders", "arguments": {"customer_id": "C1018"}},
            {"name": "get_order", "arguments": {"order_id": "O1038"}},
            {
                "name": "apply_coupon",
                "arguments": {"order_id": "O1038", "coupon_code": "DENVER10"},
            },
            {"name": "track_order", "arguments": {"order_id": "O1038"}},
            {
                "name": "return_order",
                "arguments": {"order_id": "O1038", "return_reason": "Wrong size"},
            },
            {"name": "cancel_order", "arguments": {"order_id": "O1038"}},
        ],
    },
    {
        "id": "entry_214",
        "tags": ["complex"],
        "instructions": "Your name is Michael Thompson, customer ID C1013, email michael.thompson@gap.com. Confirm identity. Get your full order history. Also list just the IDs of your current orders. Generate an order report for '2025-05-03'.  You notice there was an overcharge for order O1033, so request a refund with reason 'Overcharge error'.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1013",
                    "verified_email": "michael.thompson@gap.com",
                },
            },
            {"name": "get_order_history", "arguments": {"customer_id": "C1013"}},
            {"name": "list_orders", "arguments": {"customer_id": "C1013"}},
            {
                "name": "generate_order_report",
                "arguments": {"report_date": "2025-05-03'"},
            },
            {
                "name": "request_refund",
                "arguments": {"order_id": "O1033", "refund_reason": "Overcharge error"},
            },
        ],
    },
    {
        "id": "entry_281",
        "tags": ["complex"],
        "instructions": "Your name is Quentin Brown, customer ID C1017, email quentin.brown@gap.com. 1. Confirm identity. 2. Create a new order O1103 for SKU155, total amount 130.75, shipping to '555 Fifth Ave, Apt 8, Boston, MA 02110', billing the same. 3. Get the details of O1103 to check addresses. 4. You realize a mistake and update the shipping address to '556 Fifth Ave, Apt 8, Boston, MA 02110'. 5. Also update the billing address to '557 Fifth Ave, Apt 8, Boston, MA 02110'.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1017",
                    "verified_email": "quentin.brown@gap.com",
                },
            },
            {
                "name": "create_order",
                "arguments": {
                    "order_id": "O1103 ",
                    "customer_id": "C1017",
                    "shipping_address": "555 Fifth Ave, Apt 8, Boston, MA 02110",
                    "billing_address": "555 Fifth Ave, Apt 8, Boston, MA 02110",
                    "items": "SKU155",
                    "order_status": "processing",
                    "total_amount": "130.75",
                    "coupon_code": "",
                },
            },
            {"name": "get_order", "arguments": {"order_id": "O1103 "}},
            {
                "name": "update_shipping_address",
                "arguments": {
                    "order_id": "O1103 ",
                    "new_shipping_address": "556 Fifth Ave, Apt 8, Boston, MA 02110",
                },
            },
            {
                "name": "update_billing_address",
                "arguments": {
                    "order_id": "O1103 ",
                    "new_billing_address": "557 Fifth Ave, Apt 8, Boston, MA 02110",
                },
            },
        ],
    },
    {
        "id": "entry_282",
        "tags": ["complex"],
        "instructions": "Your name is Oliver Garcia, customer ID C1015, email oliver.garcia@gap.com. 1. Confirm your identity. 2. Create a new order O1102 for items 'SKU151,SKU152' with shipping to '333 Market St, Suite 50, San Francisco, CA 94103' and billing the same, total 210. 3. Apply the coupon code 'SFDEAL'. 4. Realizing you needed a different coupon, you cancel this order. 5. You then confirm the delivery of your older order O1035. 6. Finally, generate an order report for '2025-05-05' to double-check the status.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1015",
                    "verified_email": "oliver.garcia@gap.com",
                },
            },
            {
                "name": "create_order",
                "arguments": {
                    "order_id": "O1102",
                    "customer_id": "C1015",
                    "shipping_address": "333 Market St, Suite 50, San Francisco, CA 94103",
                    "billing_address": "333 Market St, Suite 50, San Francisco, CA 94103",
                    "items": "SKU151,SKU152",
                    "order_status": "processing",
                    "total_amount": "210",
                    "coupon_code": "",
                },
            },
            {
                "name": "apply_coupon",
                "arguments": {"order_id": "O1102", "coupon_code": "SFDEAL"},
            },
            {"name": "cancel_order", "arguments": {"order_id": "O1102"}},
            {"name": "confirm_delivery", "arguments": {"order_id": "O1035"}},
            {
                "name": "generate_order_report",
                "arguments": {"report_date": "2025-05-05"},
            },
        ],
    },
    {
        "id": "entry_285",
        "tags": ["complex"],
        "instructions": "Your name is Laura Wilson, customer ID C1012, email laura.wilson@gap.com. Confirm identity. Create a new order O1101 for item SKU200, shipping to '888 Park Ave, Suite 300, Los Angeles, CA 90017', billing to '999 Market St, Suite 200, Los Angeles, CA 90015', total 75. You change your mind about the shipping address and update it to '1010 Park Ave, Suite 300'. Also update the billing address to '1011 Market St, Suite 200'. Finally, you decide to cancel the order entirely.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1012",
                    "verified_email": "laura.wilson@gap.com",
                },
            },
            {
                "name": "create_order",
                "arguments": {
                    "order_id": "O1101",
                    "customer_id": "C1012",
                    "shipping_address": "888 Park Ave, Suite 300, Los Angeles, CA 90017",
                    "billing_address": "999 Market St, Suite 200, Los Angeles, CA 90015",
                    "items": "SKU200",
                    "order_status": "Processing",
                    "total_amount": "75",
                    "coupon_code": "",
                },
            },
            {
                "name": "update_shipping_address",
                "arguments": {
                    "order_id": "O1101",
                    "new_shipping_address": "1010 Park Ave, Suite 300 Los Angeles, CA 90017",
                },
            },
            {
                "name": "update_billing_address",
                "arguments": {
                    "order_id": "O1101",
                    "new_billing_address": "1011 Market St, Suite 200, Los Angeles, CA 90015",
                },
            },
            {"name": "cancel_order", "arguments": {"order_id": "O1101"}},
        ],
        "outputs": [
            "1010 Park",
            "1011 Market"
        ]
    },
    {
        "id": "entry_286",
        "tags": ["complex"],
        "instructions": "Your name is Alice Johnson with customer ID C1001 and email alice.johnson@gap.com. First, confirm your identity. You want to create a brand-new order with items 'SKU123,SKU999', shipping to '123 Main St, Apt 4B, New York, NY 10001' and billing address the same, total amount 89.99. You realize that on your older order O1021, the coupon code 'GAP10' was still applied by mistake, so remove that coupon. Finally, get the details of this newly created order to confirm everything looks correct.",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1001",
                    "verified_email": "alice.johnson@gap.com",
                },
            },
            {
                "name": "create_order",
                "arguments": {
                    "order_id": "O1099",
                    "customer_id": "C1001",
                    "shipping_address": "123 Main St, Apt 4B, New York, NY 10001",
                    "billing_address": "123 Main St, Apt 4B, New York, NY 10001",
                    "items": "SKU123,SKU999",
                    "order_status": "Processing",
                    "total_amount": "89.99",
                    "coupon_code": "",
                },
            },
            {"name": "remove_coupon", "arguments": {"order_id": "O1021"}},
            {"name": "get_order", "arguments": {"order_id": "O1099"}},
        ],
    },
    {
        "id": "entry_287",
        "tags": ["complex"],
        "instructions": "Your name is Ian Lee, customer ID C1009, email ian.lee@gap.com. 1. Confirm your identity. 2. Create a new order with items 'SKU444', total amount 180, shipping to '369 Walnut St, Floor 1, San Francisco, CA 94102', billing the same. 3. Apply the coupon code 'WELCOME10'. 4. You used the wrong shipping address entirely, so you decide to cancel the new order. 5. Then you remember you want a refund on your older delivered order O1009 with reason 'Defective'. ",
        "actions": [
            {
                "name": "confirm_customer_identity",
                "arguments": {
                    "customer_id": "C1009",
                    "verified_email": "ian.lee@gap.com",
                },
            },
            {
                "name": "create_order",
                "arguments": {
                    "order_id": "O1210",
                    "customer_id": "C1009",
                    "shipping_address": "369 Walnut St, Floor 1, San Francisco, CA 94102",
                    "billing_address": "369 Walnut St, Floor 1, San Francisco, CA 94102",
                    "items": "SKU444",
                    "order_status": "processing",
                    "total_amount": "180",
                    "coupon_code": "WELCOME10",
                },
            },
            {"name": "cancel_order", "arguments": {"order_id": "O1210"}},
            {
                "name": "request_refund",
                "arguments": {"order_id": "O1009", "refund_reason": "Defective"},
            },
        ],
    },
]
