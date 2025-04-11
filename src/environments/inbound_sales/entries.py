entries = [
    {
        "id": "entry_144",
        "instructions": "Your name is Daniel Martinez. You wish to follow up on your inquiry after you received a cold call from a sales representative and update your details. Do not provide your lead ID until prompted by the agent.",
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Daniel Martinez"}},
            {
                "name": "follow_up_lead",
                "arguments": {"lead_id": "L1009", "followup_action": "Update details"},
            },
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1009",
                    "name": "",
                    "contact_number": "",
                    "email": "",
                    "company": "",
                    "industry": "",
                    "source": "",
                    "status": "",
                    "notes": "",
                },
            },
        ],
        "output": [
            "updated"
        ]
    },
    {
        "id": "entry_37",
        "instructions": "You are Michael Reed from Tech Solutions. You want to know more about cloud storage options and qualify your lead. Provide your details only when requested by the agent.",
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Michael Reed"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1037"}},
            {
                "name": "qualify_lead",
                "arguments": {"lead_id": "L1037", "qualification_score": "0"},
            },
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1037",
                    "name": "",
                    "contact_number": "",
                    "email": "",
                    "company": "",
                    "industry": "",
                    "source": "",
                    "status": "",
                    "notes": "needs review",
                },
            },
            {
                "name": "follow_up_lead",
                "arguments": {
                    "lead_id": "L1037",
                    "followup_action": "Wants more information about cloud storage options",
                },
            },
        ]
    },
    {
        "id": "entry_93",
        "instructions": "You are Michael Johnson. You wish to requalify your lead L1003 regarding renewable energy projects and request a follow-up call with Oliver King to discuss potential scope and timeline for renewable energy projects and address any questions or concerns. Do not reveal your lead ID until prompted by the agent.",
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Michael Johnson"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1003 "}},
            {
                "name": "qualify_lead",
                "arguments": {"lead_id": "L1003 ", "qualification_score": "0"},
            },
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "",
                    "name": "",
                    "contact_number": "",
                    "email": "",
                    "company": "",
                    "industry": "",
                    "source": "",
                    "status": "needs review",
                    "notes": "",
                },
            },
            {
                "name": "follow_up_lead",
                "arguments": {
                    "lead_id": "L1003",
                    "followup_action": "Discuss potential scope and timeline for renewable energy projects and address any questions or concerns",
                },
            },
        ],
        "outputs": [
            "scheduled"
        ]
    },
    {
        "id": "entry_59",
        "instructions": 'Your name is Ava Harris. You want to update your lead record regarding interest in ERP solutions and change the status to "In Progress." Wait for the agent to ask for your lead ID before sharing any additional details.',
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Ava Harris"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1014"}},
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1014",
                    "name": "",
                    "contact_number": "",
                    "email": "",
                    "company": "",
                    "industry": "",
                    "source": "",
                    "status": "In Progress",
                    "notes": "interested in ERP solutions",
                },
            },
        ],
    },
    {
        "id": "entry_67",
        "instructions": "You are Evelyn Carter. You want to requalify your lead L022 regarding sustainable energy consultations to a qualification score of 85. Wait for the agent to ask for your lead ID.",
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Evelyn Carter"}},
            {"name": "get_lead", "arguments": {"lead_id": "L022"}},
            {
                "name": "qualify_lead",
                "arguments": {"lead_id": "L022", "qualification_score": "85"},
            },
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L022",
                    "name": "",
                    "contact_number": "",
                    "email": "",
                    "company": "",
                    "industry": "",
                    "source": "",
                    "status": "Qualified",
                    "notes": "",
                },
            },
        ],
        "outputs": [
            "Evelyn Carter",
            "Qualified"
        ]
    },
    {
        "id": "entry_142",
        "instructions": "Your name is James Miller. You want to requalify your lead with lead ID L1007 regarding supply chain software to a qualification score of 75 and request a callback. Wait for the agent to ask for your lead ID.",
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "James Miller"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1007"}},
            {
                "name": "qualify_lead",
                "arguments": {"lead_id": "L1007", "qualification_score": "75"},
            },
            {
                "name": "follow_up_lead",
                "arguments": {
                    "lead_id": "L1007",
                    "followup_action": "schedule callback",
                },
            },
        ],
    },
    {
        "id": "entry_77",
        "instructions": "Your name is Aria Collins. You want to update your lead details regarding SEO services for lead ID L1032. The updated contact number is 555-0123 and you are interested in exploring advanced SEO strategies and would like a follow-up call next week. Provide your lead ID only when the agent explicitly requests it.",
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Aria Collins"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1032"}},
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1032",
                    "name": "",
                    "contact_number": "555-0123",
                    "email": "",
                    "company": "",
                    "industry": "",
                    "source": "",
                    "status": "",
                    "notes": "interested in exploring advanced SEO strategies",
                },
            },
            {
                "name": "follow_up_lead",
                "arguments": {
                    "lead_id": "L1032",
                    "followup_action": "Requests follow-up call next week",
                },
            },
        ],
    },
    {
        "id": "entry_135",
        "instructions": "Your name is Matthew Cox. You want to requalify your lead L1045 regarding fleet management software with a score of 75 and update your details with a note that you had an initial conversation with them about integrating GPS tracking capabilities. Wait for the agent to ask for your lead ID before proceeding.",
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Matthew Cox"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1045"}},
            {
                "name": "qualify_lead",
                "arguments": {"lead_id": "L1045", "qualification_score": "0"},
            },
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1045",
                    "name": "",
                    "contact_number": "",
                    "email": "",
                    "company": "",
                    "industry": "",
                    "source": "",
                    "status": "",
                    "notes": "Inquired about fleet management software. Had an initial conversation about integrating GPS tracking capabilities",
                },
            },
        ],
        "outputs": [
            "requalified",
        ]
    },
    {
        "id": "entry_143",
        "instructions": 'Your name is Sophia Garcia. You want to update your lead record from EduTech Worldwide for lead ID L1008, update the status to "Engaged," and inquire about pricing for the enterprise package. Provide your lead ID only when the agent explicitly asks.',
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Sophia Garcia"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1008"}},
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1008",
                    "name": "",
                    "contact_number": "",
                    "email": "",
                    "company": "",
                    "industry": "",
                    "source": "",
                    "status": "Engaged",
                    "notes": "interested in pricing for the enterprise package",
                },
            },
        ],
    },
    {
        "id": "entry_61",
        "instructions": "Your name is Isabella Allen. You wish to confirm your interest in cloud solutions and update your lead (L016) record. Provide your lead ID only when asked.",
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Isabella Allen"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1016"}},
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1016",
                    "name": "",
                    "contact_number": "",
                    "email": "",
                    "company": "",
                    "industry": "",
                    "source": "",
                    "status": "",
                    "notes": "Confirmed interest in cloud solutions",
                },
            },
        ],
        "outputs": [
            "updated"
        ]
    },
    {
        "id": "entry_129",
        "instructions": "Your name is David Morgan. You want to requalify your lead for lead ID L1039 regarding supply chain analytics and request a callback. Do not reveal your lead ID until prompted. Your sales rep is Isabella Brooks",
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "David Morgan"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1039"}},
            {
                "name": "qualify_lead",
                "arguments": {"lead_id": "L1039", "qualification_score": "0"},
            },
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1039",
                    "name": "",
                    "contact_number": "",
                    "email": "",
                    "company": "",
                    "industry": "",
                    "source": "",
                    "status": "Needs review",
                    "notes": "",
                },
            },
            {
                "name": "follow_up_lead",
                "arguments": {
                    "lead_id": "L1039",
                    "followup_action": "Callback requested",
                },
            },
        ],
        "outputs": [
            "successfully"
        ]
    },
    {
        "id": "entry_80",
        "instructions": 'You are Alexander Morris. You wish to update your lead details regarding financial advisory services by updating the contact number to 555-6789 and changing the status from "New" to "Contacted." Provide your lead ID only when explicitly asked by the agent.',
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Alexander Morris"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1035"}},
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1035",
                    "name": "",
                    "contact_number": "555-6789",
                    "email": "",
                    "company": "",
                    "industry": "",
                    "source": "",
                    "status": "Contacted",
                    "notes": "",
                },
            },
        ],
    },
    {
        "id": "entry_31",
        "instructions": "You are Sebastian Edwards from Innovatech. You want to explore AI-powered analytics and qualify your lead for lead ID L1031 and shedule a meeting with sales representative. Provide your details only when the agent explicitly asks for them.",
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Sebastian Edwards"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1031"}},
            {
                "name": "qualify_lead",
                "arguments": {"lead_id": "L1031", "qualification_score": "0"},
            },
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1031",
                    "name": "",
                    "contact_number": "",
                    "email": "",
                    "company": "",
                    "industry": "",
                    "source": "",
                    "status": "",
                    "notes": "interested in exploring AI-powered analytics for company, specifically how it can enhance sales processes and improve lead management",
                },
            },
        ],
        "outputs": [
            "scheduled"
        ]
    },
    {
        "id": "entry_117",
        "instructions": "Your name is Benjamin Ward. You wish to update your lead record for Aiden Phillips with lead ID L1027 regarding IT integration solutions to indicate potential interest in streamlining processes and enhancing efficiency, and qualify your lead with a score of 85. Provide your details only when explicitly requested by the agent.",
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Aiden Phillips"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1027"}},
            {
                "name": "qualify_lead",
                "arguments": {"lead_id": "L1027", "qualification_score": "85"},
            },
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1027",
                    "name": "",
                    "contact_number": "",
                    "email": "",
                    "company": "",
                    "industry": "",
                    "source": "",
                    "status": "",
                    "notes": "Looking for IT integration solutions with potential interest in streamlining processes and enhancing efficiency",
                },
            },
        ],
    },
    {
        "id": "entry_50",
        "instructions": "You are William Brown. You want to request a callback regarding investment advisory services for lead ID L1005. Do not reveal your lead ID until the agent specifically asks.",
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "William Brown"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1005"}},
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1005",
                    "name": "",
                    "contact_number": "",
                    "email": "",
                    "company": "",
                    "industry": "",
                    "source": "",
                    "status": "",
                    "notes": "interested in investment advisory services",
                },
            },
            {
                "name": "follow_up_lead",
                "arguments": {
                    "lead_id": "L1005",
                    "followup_action": "callback requested",
                },
            },
        ],
    },
    {
        "id": "entry_139",
        "instructions": "Your name is Lucas Turner. You wish to requalify your lead with Lead ID L1004 for Emily Davis regarding CRM solutions to a score of 85, and send a follow-up email. Provide your lead ID only when prompted.",
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Emily Davis"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1004"}},
            {
                "name": "qualify_lead",
                "arguments": {"lead_id": "L1004", "qualification_score": "85"},
            },
            {
                "name": "follow_up_lead",
                "arguments": {
                    "lead_id": "L1004",
                    "followup_action": "Send follow-up email",
                },
            },
        ],
        "outputs": [
            "85"
        ]
    },
    {
        "id": "entry_84",
        "instructions": "You are David Morgan. You wish to requalify your lead with lead ID L1039 with score of 90 regarding supply chain analytics. Wait for the agent to ask for your lead ID before sharing additional details.",
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "David Morgan"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1039"}},
            {
                "name": "qualify_lead",
                "arguments": {"lead_id": "L1039", "qualification_score": "90"},
            }
        ],
    },
    {
        "id": "entry_79",
        "instructions": "Your name is Lily Sanchez. You want to requalify your lead with lead ID L1034 regarding event planning software to a score of 85 and update status to - Qualified. Wait for the agent to ask for your lead ID before proceeding.",
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Lily Sanchez"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1034"}},
            {
                "name": "qualify_lead",
                "arguments": {"lead_id": "L1034", "qualification_score": "85"},
            },
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1034",
                    "name": "",
                    "contact_number": "",
                    "email": "",
                    "company": "",
                    "industry": "",
                    "source": "",
                    "status": "Qualified",
                    "notes": "",
                },
            },
        ],
    },
    {
        "id": "entry_18",
        "instructions": "Your name is Mia Wright from Creative Edge. You received an email campaign and are interested in design solutions. Ask for a follow-up call at 10:00 a.m. and provide your details only when prompted.",
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Mia Wright"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1018"}},
            {
                "name": "follow_up_lead",
                "arguments": {
                    "lead_id": "L1018",
                    "followup_action": "Callback requested",
                },
            },
        ],
        "outputs": [
            "10",
            "scheduled"
        ]
    },
    {
        "id": "entry_66",
        "instructions": "Your name is Liam Rivera. You want to schedule a follow-up email for a lead with lead ID L1021 for Logan Nelson who has inquired about POS solutions. Do not share your lead ID until the agent explicitly asks.",
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Logan Nelson"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1021"}},
            {
                "name": "follow_up_lead",
                "arguments": {
                    "lead_id": "L1021",
                    "followup_action": "Send follow-up email",
                },
            },
        ],
        "outputs": [
            "scheduled",
            "L1021"
        ]
    },
    {
        "id": "entry_86",
        "instructions": 'You are Benjamin Ward. You want to update your lead record with lead ID L1041 regarding risk management software for Samuel Murphy, update the status to "Contacted," and note that they are looking for software with advanced analytics capabilities. Do not reveal your lead ID until the agent explicitly asks for it.',
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Samuel Murphy"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1041"}},
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1041",
                    "name": "",
                    "contact_number": "",
                    "email": "",
                    "company": "",
                    "industry": "",
                    "source": "",
                    "status": "Contacted",
                    "notes": "looking for software with advanced analytics capabilities",
                },
            },
        ],
    },
    {
        "id": "entry_147",
        "instructions": "Your name is Ava Bennett. You want to follow up on an inquiry from Chloe Robinson at Event Horizon, requalify your lead with lead ID L1012, and schedule a follow-up meeting at 11 AM. Do not reveal your lead ID until the agent explicitly asks for it.",
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Chloe Robinson"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1012"}},
            {
                "name": "qualify_lead",
                "arguments": {"lead_id": "L1012", "qualification_score": "0"},
            },
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1012",
                    "name": "",
                    "contact_number": "",
                    "email": "",
                    "company": "",
                    "industry": "",
                    "source": "",
                    "status": "",
                    "notes": "Needs review",
                },
            },
            {
                "name": "follow_up_lead",
                "arguments": {
                    "lead_id": "L1012",
                    "followup_action": "each out to Chloe to propose a few time slots and confirm her availability for a follow-up meeting",
                },
            },
        ],
        "outputs": [
            "scheduled",
            "11"
        ]
    },
    {
        "id": "entry_15",
        "instructions": "You are Noah Young from MediaWorks. You are interested in digital ad services and would like pricing information. You would also like to update your contact number to (555) 123-4567 and the email to noah.young@mediaworks.com. After the information is updated, you want to schedule a meeting with Mia Adams on 2025-04-21 at 10:00 AM. Do not reveal your lead ID until the agent specifically requests it.",
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Noah Young"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1015"}},
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1015",
                    "contact_number": "(555) 123-4567",
                    "email": "noah.young@mediaworks.com"
                },
            },
            {
                "name": "schedule_meeting",
                "arguments": {
                    "meeting_id": "M1099",
                    "lead_id": "L1015",
                    "rep_name": "Mia Adams",
                    "meeting_date": "2025-04-21",
                    "meeting_time": "10:00",
                },
            },
        ],
        "outputs": [
            "noah.young@mediaworks.com",
            "10:00",
            "4567",
        ]
    },
    {
        "id": "entry_35",
        "instructions": "You are Alexander Morris from Finance Experts. You want to inquire about financial advisory services and update your lead details for lead ID L1035 with the contact number to (555) 111-0123 and the email to alex.morris@financeexperts.com. Provide your lead ID only when the agent explicitly asks.",
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Alexander Morris"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1035"}},
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1035",
                    "contact_number": "(555) 111-0123",
                    "email": "alex.morris@financeexperts.com",
                },
            },
        ],
        "outputs": [
            "alex.morris@financeexperts.com",
            "0123",
        ]
    },
    {
        "id": "entry_78",
        "instructions": "You are Henry Stewart. You want to inquire about property investment tools and schedule a follow-up call with Oliver King between 2:00 p.m and 4:00 p.m. Do not reveal your lead ID until prompted.",
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Henry Stewart"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1033"}},
            {
                "name": "follow_up_lead",
                "arguments": {
                    "lead_id": "L1033",
                    "followup_action": '"Schedule follow-up call between 14:00 and 16:00"',
                },
            },
        ],
        "outputs": [
            "scheduled",
            "Oliver King",
        ]
    },
    {
        "id": "entry_44",
        "instructions": "Your name is Ruby Richardson from Creative Minds. Your lead ID is L1044 and you are interested in social media marketing solutions and would like a follow-up call at 11:25 AM. Provide your lead ID only when requested.",
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Ruby Richardson"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1044"}},
            {
                "name": "follow_up_lead",
                "arguments": {
                    "lead_id": "L1044",
                    "followup_action": "Follow-up call requested",
                },
            },
        ],
        "outputs": [
            "scheduled",
            "11:25",
        ]
    },
    {
        "id": "entry_70",
        "instructions": "You are Jackson Roberts. You want to update the status of your lead details for Lead ID L1025 regarding investment advisory to 'Active', and note: 'Scheduled a meeting for next week to discuss investment strategies.' Provide your lead ID only when asked by the agent.",
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Jackson Roberts"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1025"}},
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1025",
                    "status": "Active",
                    "notes": "Scheduled a meeting for next week to discuss investment strategies.",
                },
            },
        ],
    },
    {
        "id": "entry_22",
        "instructions": "Your name is Evelyn Carter from Eco Energy. You are interested in sustainable energy consultations and want to update your lead (L1022) details. You'd like to update the status to \"In Progress\" and add a note that you're particularly interested in solar energy solutions. Provide your lead ID only when the agent asks for it.",
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Evelyn Carter"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1022"}},
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1022",
                    "name": "",
                    "contact_number": "",
                    "email": "",
                    "company": "",
                    "industry": "",
                    "source": "",
                    "status": "In Progress",
                    "notes": "Needs consultation on sustainable energy. Interested in solar energy solutions.",
                },
            },
        ],
    },
    {
        "id": "entry_65",
        "instructions": 'Your name is Harper Adams. You want to update your lead details for lead ID L1020 for inventory management solutions. Update the contact number to (555) 555-6789 and change the status to "In Progress." Provide your lead ID only when prompted by the agent.',
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Harper Adams"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1020"}},
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1020",
                    "name": "",
                    "contact_number": "(555) 555-6789",
                    "email": "",
                    "company": "",
                    "industry": "",
                    "source": "",
                    "status": "In Progress",
                    "notes": "",
                },
            },
        ],
    },
    {
        "id": "entry_114",
        "instructions": "Your name is Ella Perez. You wish to add a follow-up action to your lead L1024 regarding your inquiry on branding services. Wait for the agent to prompt you for your lead ID.",
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Ella Perez"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1024"}},
            {
                "name": "follow_up_lead",
                "arguments": {
                    "lead_id": "L1024",
                    "followup_action": "Follow up on branding services inquiry",
                },
            },
        ],
    },
    {
        "id": "entry_73",
        "instructions": 'Your name is Victoria Campbell. You want to update the status of your lead L1028 to "In Progress" and add a note that you\'re particularly interested in features related to appointment scheduling and patient data security.. Wait for the agent to request your lead ID before providing more details.',
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Victoria Campbell"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1028"}},
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1028",
                    "name": "",
                    "contact_number": "",
                    "email": "",
                    "company": "",
                    "industry": "",
                    "source": "",
                    "status": "In Progress",
                    "notes": "Interested in patient management software, particularly in features related to appointment scheduling and patient data security",
                },
            },
        ],
    },
    {
        "id": "entry_95",
        "instructions": "Your name is William Brown. You want to inquire about investment advisory services, update your lead details for lead ID L1005 with the contact number 555-0123, and request a follow-up call. Wait for the agent’s prompt before giving your lead ID.",
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "William Brown"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1005"}},
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1005",
                    "name": "",
                    "contact_number": "555-0123",
                    "email": "",
                    "company": "",
                    "industry": "",
                    "source": "",
                    "status": "",
                    "notes": "Wants to inquire about investment advisory services",
                },
            },
            {
                "name": "follow_up_lead",
                "arguments": {
                    "lead_id": "L1005",
                    "followup_action": "Schedule follow-up call",
                },
            },
        ],
    },
    {
        "id": "entry_102",
        "instructions": "Your name is Chloe Robinson. You want to qualify your lead L1012 from Event Horizon further. Do not share your lead ID until prompted.",
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Chloe Robinson"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1012"}},
            {
                "name": "qualify_lead",
                "arguments": {"lead_id": "L1012", "qualification_score": "85"},
            },
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1012",
                    "status": "Qualified",
                },
            },
            {
                "name": "follow_up_lead",
                "arguments": {
                    "lead_id": "L1012",
                    "followup_action": "Arrange a callback to discuss potential marketing automation solutions.",
                },
            },
        ]
    },
    {
        "id": "entry_109",
        "instructions": "Your name is Elijah Scott. You wish to requalify your lead with lead ID L1019 regarding project management software to a score of 85. Provide your lead ID only when explicitly requested.",
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Elijah Scott"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1019"}},
            {
                "name": "qualify_lead",
                "arguments": {"lead_id": "L1019", "qualification_score": "85"},
            },
        ],
    },
    {
        "id": "entry_72",
        "instructions": "You are Aiden Phillips. You want to requalify your lead L1027 regarding IT integration solutions with a qualification score of 75. Provide your details only when the agent prompts you for your lead ID.",
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Aiden Phillips"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1027"}},
            {
                "name": "qualify_lead",
                "arguments": {"lead_id": "L1027", "qualification_score": "75"},
            },
        ],
    },
    {
        "id": "entry_88",
        "instructions": "You are Joseph Cooper. You want to requalify your lead with lead ID L1043 regarding software development services to a score of 85. Provide your lead ID only when the agent requests it.",
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Joseph Cooper"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1043"}},
            {
                "name": "qualify_lead",
                "arguments": {"lead_id": "L1043", "qualification_score": "85"},
            },
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1043",
                    "name": "",
                    "contact_number": "",
                    "email": "",
                    "company": "",
                    "industry": "",
                    "source": "",
                    "status": "",
                    "notes": "Qualified",
                },
            },
        ],
    },
    {
        "id": "entry_63",
        "instructions": "You are Mia Wright. You want to request a follow up call with Oliver King for your inquiry regarding creative design solutions with lead ID L1018. Provide your lead ID only when explicitly requested.",
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Mia Wright"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1018"}},
            {
                "name": "follow_up_lead",
                "arguments": {
                    "lead_id": "L1018",
                    "followup_action": "Follow-up call requested",
                },
            },
        ],
        "outputs": [
            "scheduled",
            "Oliver King",
        ]
    },
    {
        "id": "entry_121",
        "instructions": "Your name is Sebastian Edwards. You want to requalify your lead with lead ID L1031 regarding AI-powered analytics. Provide your lead ID only when prompted.",
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Sebastian Edwards"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1031"}},
            {
                "name": "qualify_lead",
                "arguments": {"lead_id": "L1031", "qualification_score": "0"},
            },
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1031",
                    "name": "",
                    "contact_number": "",
                    "email": "",
                    "company": "",
                    "industry": "",
                    "source": "",
                    "status": "",
                    "notes": "Needs review",
                },
            },
        ],
    },
    {
        "id": "entry_116",
        "instructions": "Your name is Scarlett Turner. You want to requalify your lead with lead ID L1026 regarding digital marketing services and request a follow-up call. Do not provide your lead ID until prompted.",
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Scarlett Turner"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1026"}},
            {
                "name": "qualify_lead",
                "arguments": {"lead_id": "L1026", "qualification_score": "0"},
            },
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1026",
                    "name": "",
                    "contact_number": "",
                    "email": "",
                    "company": "",
                    "industry": "",
                    "source": "",
                    "status": "",
                    "notes": "Needs review",
                },
            },
            {
                "name": "follow_up_lead",
                "arguments": {
                    "lead_id": "L1026",
                    "followup_action": "Follow-up call requested",
                },
            },
        ],
    },
    {
        "id": "entry_146",
        "instructions": 'Your name is Benjamin Clark. You wish to update your lead record (L1011) status to "In Progress" and add a note that you are interested in receiving more detailed information about the software features and pricing. Provide your lead ID only when the agent asks.',
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Benjamin Clark"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1011"}},
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1011",
                    "name": "",
                    "contact_number": "",
                    "email": "",
                    "company": "",
                    "industry": "",
                    "source": "",
                    "status": "In Progress",
                    "notes": "Looking for property management solutions. Interested in more detailed information about software features and pricing.",
                },
            },
        ],
    },
    {
        "id": "entry_101",
        "instructions": 'Your name is Benjamin Clark. You want to update your lead details for lead ID L1011 regarding property management solutions. Update the contact number to (555) 123-4567, the email to benjamin.clark@email.com, the company name to "Clark Property Solutions," and the industry to "Real Estate." Provide your lead ID only when the agent requests it.',
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Benjamin Clark"}},
            {"name": "get_lead", "arguments": {"lead_id": "L1011"}},
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1011",
                    "name": "",
                    "contact_number": "(555) 123-4567",
                    "email": "benjamin.clark@email.com",
                    "company": "Clark Property Solutions",
                    "industry": "Real Estate",
                    "source": "",
                    "status": "",
                    "notes": "",
                },
            },
        ],
    },
    {
        "id": "entry_290",
        "tags": ["complex"],
        "instructions": 'You are Isabella Brooks. Start by listing all leads to ensure your records are correctly registered, then search for your lead Harper Adams by name to double-check its details. Update their company information to "Adams Consulting", follow up with an inquiry (such as sending a check-in email), and generate a lead report for the current month of April.',
        "actions": [
            {"name": "list_leads", "arguments": {}},
            {"name": "search_lead_by_name", "arguments": {"name": "Harper Adams"}},
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1020",
                    "name": "",
                    "contact_number": "",
                    "email": "",
                    "company": "Adams Consulting",
                    "industry": "",
                    "source": "",
                    "status": "",
                    "notes": "",
                },
            },
            {
                "name": "follow_up_lead",
                "arguments": {
                    "lead_id": "L1020",
                    "followup_action": "Send a check-in email",
                },
            },
            {"name": "generate_lead_report", "arguments": {"report_period": "2025-04"}},
        ],
    },
    {
        "id": "entry_207",
        "tags": ["complex"],
        "instructions": "You are Liam Walker. As a returning customer, you want to search for your lead record by name, update your email and phone number, transfer your lead to a specialist for technical support, create a follow up with a callback action to address further queries, and generate a report summarizing your recent interactions.",
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Liam Walker"}},
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1013",
                    "name": "",
                    "contact_number": "734-8921",
                    "email": "liam.walker@logixsystems.com",
                    "company": "",
                    "industry": "",
                    "source": "",
                    "status": "",
                    "notes": "",
                },
            },
            {
                "name": "transfer_lead",
                "arguments": {"lead_id": "L1013", "new_rep_name": "Jackson Murphy"},
            },
            {
                "name": "follow_up_lead",
                "arguments": {
                    "lead_id": "L1013",
                    "followup_action": "Callback for assistance with updating contact information and technical support for systems",
                },
            },
            {"name": "generate_lead_report", "arguments": {"report_period": "2025-04"}},
        ],
    },
    {
        "id": "entry_291",
        "tags": ["complex"],
        "instructions": "You are Benjamin Clark. You recently had a call with sales rep Ava Bennett and want to update your profile to include your new requirements of a system with strong data analytics and reporting features. The solution must be scalable to accommodate future growth. You are interested in exploring cloud-based options for flexibility and cost-effectiveness. Schedule an in-depth product demo. Your lead ID is L1011. Do not provide your lead ID unless explicitly asked for it.",
        "actions": [
            {"name": "get_lead", "arguments": {"lead_id": "L1011"}},
            {
                "name": "qualify_lead",
                "arguments": {"lead_id": "L1011", "qualification_score": "80"},
            },
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1011",
                    "name": "",
                    "contact_number": "",
                    "email": "",
                    "company": "",
                    "industry": "",
                    "source": "",
                    "status": "Needs review",
                    "notes": "The client is interested in a comprehensive solution that integrates CRM and ERP capabilities. - They require a system with strong data analytics and reporting features. - The solution must be scalable to accommodate future growth. - They are interested in exploring cloud-based options for flexibility and cost-effectiveness. ",
                },
            },
            {
                "name": "assign_lead_to_rep",
                "arguments": {"lead_id": "L1011", "rep_name": "Ava Bennett"},
            },
            {
                "name": "schedule_meeting",
                "arguments": {
                    "meeting_id": "M1099",
                    "lead_id": "L1011",
                    "rep_name": "Ava Bennett",
                    "meeting_date": "2025-06-21",
                    "meeting_time": "10:30",
                },
            },
        ],
    },
    {
        "id": "entry_216",
        "tags": ["complex"],
        "instructions": "You are Charlotte Jackson. You're interested in creating a new lead, and want to update the email with your latest information, assign your lead to a specialist rep for further discussion, record the outcome of your recent call, and get a follow-up email with a specific action to maintain engagement.",
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Charlotte Jackson"}},
            {
                "name": "create_lead",
                "arguments": {
                    "lead_id": "L1046",
                    "name": "Charlotte Jackson",
                    "contact_number": "(555) 123-4567",
                    "email": "charlotte.jackson@email.com",
                    "company": "Jackson Innovations",
                    "industry": "Technology",
                    "source": "Website",
                    "status": "new",
                    "notes": "",
                },
            },
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1046",
                    "name": "",
                    "contact_number": "",
                    "email": "charlotte.j@jacksoninnovations.com",
                    "company": "",
                    "industry": "",
                    "source": "",
                    "status": "",
                    "notes": "",
                },
            },
            {
                "name": "assign_lead_to_rep",
                "arguments": {"lead_id": "L1046", "rep_name": "Noah Griffin"},
            },
            {
                "name": "record_call_outcome",
                "arguments": {
                    "lead_id": "L1046",
                    "rep_name": "Noah Griffin",
                    "call_outcome": "Interested in learning more about cloud solutions",
                },
            },
            {
                "name": "follow_up_lead",
                "arguments": {
                    "lead_id": "L1046",
                    "followup_action": "Send an introductory email about our services",
                },
            },
        ],
    },
    {
        "id": "entry_292",
        "tags": ["complex"],
        "instructions": "You are James Miller. After an initial conversation with a sales representative you are interested in scheduling a meeting to dive deeper into your requirements. Your lead ID is L1007. Do not provide your lead ID unless explicitly asked for it.\n\nAfter an initial conversation with a sales representative, retrieve your lead details, qualify your lead by assigning a score based on your interest, assign your lead to a specific rep for further discussion, record the outcome of your follow-up call, and then schedule another meeting to dive deeper into your requirements.",
        "actions": [
            {"name": "get_lead", "arguments": {"lead_id": "L1007"}},
            {
                "name": "qualify_lead",
                "arguments": {"lead_id": "L1007", "qualification_score": "80"},
            },
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1007",
                    "name": "",
                    "contact_number": "",
                    "email": "",
                    "company": "",
                    "industry": "",
                    "source": "",
                    "status": "",
                    "notes": "Needs review",
                },
            },
            {
                "name": "assign_lead_to_rep",
                "arguments": {"lead_id": "L1007", "rep_name": "Mia Adams"},
            },
            {
                "name": "schedule_meeting",
                "arguments": {
                    "meeting_id": "M1088",
                    "lead_id": "L1007",
                    "rep_name": "Mia Adams",
                    "meeting_date": "2025-06-19",
                    "meeting_time": "9:00",
                },
            },
            {
                "name": "record_call_outcome",
                "arguments": {
                    "lead_id": "L1007",
                    "rep_name": "Mia Adams",
                    "call_outcome": "meeting scheduled to to dive deeper into requirements",
                },
            },
        ],
    },
    {
        "id": "entry_206",
        "tags": ["complex"],
        "instructions": "You are Olivia Wilson. You want to retrieve your lead history to review past interactions, update your contact information with a new email, record a callback outcome from your recent call with Jackson Murphy, schedule a meeting for a product demonstration on May 31st at 1:00 p.m., and follow up with an email action to request additional information.",
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Olivia Wilson"}},
            {"name": "get_lead_history", "arguments": {"lead_id": "L1006"}},
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1006",
                    "name": "",
                    "contact_number": "",
                    "email": "olivia.wilson@creativeminds.com",
                    "company": "",
                    "industry": "",
                    "source": "",
                    "status": "",
                    "notes": "",
                },
            },
            {
                "name": "record_call_outcome",
                "arguments": {
                    "lead_id": "L1006",
                    "rep_name": "Jackson Murphy",
                    "call_outcome": "Interested",
                },
            },
            {
                "name": "schedule_meeting",
                "arguments": {
                    "meeting_id": "M1016",
                    "lead_id": "L1006",
                    "rep_name": "Jackson Murphy",
                    "meeting_date": "2025-05-31",
                    "meeting_time": "13:00",
                },
            },
            {
                "name": "follow_up_lead",
                "arguments": {
                    "lead_id": "L1006",
                    "followup_action": "request additional information",
                },
            },
        ],
    },
    {
        "id": "entry_208",
        "tags": ["complex"],
        "instructions": "You are Sophia Garcia. After receiving a call that did not meet your expectations, you wish to update your lead information with the latest details, record the call outcome as 'not interested', disqualify your lead by providing a specific reason, and review your lead history to ensure the changes are logged.",
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Sophia Garcia"}},
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1008",
                    "name": "",
                    "contact_number": "(555) 123-4567",
                    "email": "",
                    "company": "",
                    "industry": "",
                    "source": "",
                    "status": "",
                    "notes": "Received call on October 15, 2023, at 2:30 PM. Lead expressed no interest in our services at this time.",
                },
            },
            {
                "name": "record_call_outcome",
                "arguments": {
                    "lead_id": "L1008",
                    "rep_name": "Sophia Carter",
                    "call_outcome": "Not interested",
                },
            },
            {
                "name": "disqualify_lead",
                "arguments": {
                    "lead_id": "L1008",
                    "disqualify_reason": "Pricing did not meet expectations",
                },
            },
            {"name": "get_lead_history", "arguments": {"lead_id": "L1008"}},
        ],
    },
    {
        "id": "entry_293",
        "tags": ["complex"],
        "instructions": "You are David Lee. Give the agent your complete details. You are interested in exploring solutions that can enhance your company's technology infrastructure. You are particularly interested in innovative software solutions. Schedule a meeting to explore potential business opportunities.",
        "actions": [
            {
                "name": "create_lead",
                "arguments": {
                    "lead_id": "L1099",
                    "name": "David Lee",
                    "contact_number": "(555) 123-4567",
                    "email": "david.lee@example.com",
                    "company": "Lee Enterprises",
                    "industry": "Technology",
                    "source": "introductory call",
                    "status": "New",
                    "notes": "He expressed interest in exploring solutions that can enhance his company's technology infrastructure. He is particularly interested in innovative software solutions.",
                },
            },
            {
                "name": "assign_lead_to_rep",
                "arguments": {"lead_id": "L1099", "rep_name": "Lucas Turner"},
            },
            {
                "name": "schedule_meeting",
                "arguments": {
                    "meeting_id": "M1099",
                    "lead_id": "L1099",
                    "rep_name": "Lucas Turner",
                    "meeting_date": "2025-06-17",
                    "meeting_time": "14:30",
                },
            },
            {
                "name": "qualify_lead",
                "arguments": {"lead_id": "L1099", "qualification_score": "90"},
            },
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1099",
                    "name": "",
                    "contact_number": "",
                    "email": "",
                    "company": "",
                    "industry": "",
                    "source": "",
                    "status": "",
                    "notes": "Needs review",
                },
            },
            {
                "name": "record_call_outcome",
                "arguments": {
                    "lead_id": "L1099",
                    "rep_name": "Lucas Turner",
                    "call_outcome": "The introductory call with David Lee went well. He expressed interest in exploring solutions that can enhance his company's technology infrastructure. He is particularly interested in innovative software solutions. Meeting scheduled.",
                },
            },
        ],
    },
    {
        "id": "entry_203",
        "tags": ["complex"],
        "instructions": "You are Mark Wilson. Start by searching for your lead record by name. If not found, create new lead, then update to a new email address and add notes regarding your requirements. Then, transfer your lead to a specialist representative and rate your overall experience with the initial interaction.",
        "actions": [
            {"name": "search_lead_by_name", "arguments": {"name": "Mark Wilson"}},
            {
                "name": "create_lead",
                "arguments": {
                    "lead_id": "L1046",
                    "name": "Mark Wilson",
                    "contact_number": "+1 (555) 123-4567",
                    "email": "mark.wilson@example.com",
                    "company": "Wilson Enterprises",
                    "industry": "Technology",
                    "source": "Referral",
                    "status": "new",
                    "notes": "",
                },
            },
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1046",
                    "name": "",
                    "contact_number": "",
                    "email": "mark.wilson@wilsonenterprises.com",
                    "company": "",
                    "industry": "",
                    "source": "",
                    "status": "",
                    "notes": "Interested in exploring cloud solutions and cybersecurity services",
                },
            },
            {
                "name": "transfer_lead",
                "arguments": {"lead_id": "L1046", "new_rep_name": "Harper Ross"},
            },
            {"name": "rate_lead", "arguments": {"lead_id": "L1046", "rating": "5"}},
        ],
    },
    {
        "id": "entry_294",
        "tags": ["complex"],
        "instructions": "You are Ethan Garcia. Give the agent all of your information. You are very interested in finding a scalable and efficient IT management software to streamline operations and improve productivity. Schedule a meeting for a product demo. \n\nAs a new prospect, create your lead with all required information, qualify your lead with a strong score reflecting your interest, assign your lead to your preferred sales representative, schedule a meeting for a product demo, and record the outcome of your initial call.",
        "actions": [
            {
                "name": "create_lead",
                "arguments": {
                    "lead_id": "L1088",
                    "name": "Ethan Garcia",
                    "contact_number": "(555) 123-4567",
                    "email": "ethan.garcia@garciasolutions.com",
                    "company": "Garcia Solutions",
                    "industry": "Information Technology",
                    "source": "inbound",
                    "status": "New",
                    "notes": "",
                },
            },
            {
                "name": "qualify_lead",
                "arguments": {"lead_id": "L1088", "qualification_score": "85"},
            },
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1088",
                    "name": "",
                    "contact_number": "",
                    "email": "",
                    "company": "",
                    "industry": "",
                    "source": "",
                    "status": "",
                    "notes": "Needs review",
                },
            },
            {
                "name": "assign_lead_to_rep",
                "arguments": {"lead_id": "L1088", "rep_name": "Charlotte Bell"},
            },
            {
                "name": "schedule_meeting",
                "arguments": {
                    "meeting_id": "M1088",
                    "lead_id": "L1088",
                    "rep_name": "Charlotte Bell",
                    "meeting_date": "2025-06-28",
                    "meeting_time": "10:15",
                },
            },
            {
                "name": "record_call_outcome",
                "arguments": {
                    "lead_id": "L1088",
                    "rep_name": "Charlotte Bell",
                    "call_outcome": "During the initial call, I expressed a strong interest in the IT management software due to its potential to enhance operational efficiency. Charlotte Bell will conduct a detailed product demo to showcase the software's capabilities and discuss how it aligns with our company's needs. The call went well, and I'm optimistic about the software's fit for Garcia Solutions. I look forward to the upcoming demo and further discussions.",
                },
            },
        ],
    },
    {
        "id": "entry_295",
        "tags": ["complex"],
        "instructions": "You are Olivia Wilson. After attending a recent webinar, you wish to update your lead ID L1006 with a new email and contact number. Do not give your lead ID unless explicitly asked. assign your lead to a knowledgeable sales rep for a detailed discussion, record the outcome of your follow-up call, and exit the conversation after confirming that all steps are completed.",
        "actions": [
            {"name": "get_lead", "arguments": {"lead_id": "L1006"}},
            {
                "name": "update_lead",
                "arguments": {
                    "lead_id": "L1006",
                    "contact_number": "(555) 019-8765",
                    "email": "olivia.wilson@example.com",
                },
            },
            {
                "name": "assign_lead_to_rep",
                "arguments": {"lead_id": "L1006", "rep_name": "Emma Scott"},
            },
            {
                "name": "follow_up_lead",
                "arguments": {
                    "lead_id": "L1006",
                    "followup_action": "Wants a detailed discussion",
                },
            },
            {
                "name": "record_call_outcome",
                "arguments": {
                    "lead_id": "L1006",
                    "rep_name": "Emma Scott",
                    "call_outcome": "Lead assigned to rep. Interested in having a detailed discussion.",
                },
            },
        ],
    },
]
