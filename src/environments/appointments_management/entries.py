entries = [
    {
        "id": "entry_136",
        "instructions": "Your name is Kevin Moore. You want to check available slots to reschedule your pending endocrinology appointment on 2025-04-08 at 9:30 a.m. (confirmation code HC1016) to 2025-04-12 at 10:00 a.m.. Provide your confirmation code only if requested.",
        "actions": [
            {
                "name": "check_appointment_status",
                "arguments": {"confirmation_code": "HC1016"},
            },
            {
                "name": "get_available_slots",
                "arguments": {"appointment_date": "2025-04-12"},
            },
            {
                "name": "reschedule_appointment",
                "arguments": {
                    "confirmation_code": "HC1016",
                    "new_date": "2025-04-12",
                    "new_time": "10:00",
                },
            },
        ],
    },
    {
        "id": "entry_120",
        "instructions": "Your name is Yvonne Roberts. You have a confirmed emergency appointment on 2025-04-10 at 12:15 p.m. (confirmation code HC1030) and want to check its summary. Only reveal your confirmation code on explicit request.",
        "actions": [
            {"name": "get_appointment", "arguments": {"confirmation_code": "HC1030"}},
            {
                "name": "generate_appointment_report",
                "arguments": {"appointment_date": "2025-04-10"},
            },
        ],
        "outputs": [
            "City Hospital",
            "Accident",
            "Emergency"
        ]
    },
    {
        "id": "entry_28",
        "instructions": "Your name is William Green. You have a confirmed post-operative surgery check-up on 2025-04-09 at 10:45 a.m. (confirmation code HC1028) and want to verify the follow-up details. Provide your confirmation code only if the agent asks.",
        "actions": [
            {"name": "get_appointment", "arguments": {"confirmation_code": "HC1028"}},
            {
                "name": "generate_appointment_report",
                "arguments": {"appointment_date": "2025-04-09"},
            },
        ],
        "outputs": [
            "10:45",
            "Sutures"
        ]
    },
    {
        "id": "entry_52",
        "instructions": "Your name is Quincy Scott. You want to check the status of your pending psychiatry appointment on 2025-04-11 at 11:15 a.m. (confirmation code HC1022) without giving additional details. Provide your confirmation code only on request.",
        "actions": [
            {
                "name": "check_appointment_status",
                "arguments": {"confirmation_code": "HC1022"},
            }
        ],
        "outputs": [
            "Pending",
            "HC1022",
        ]
    },
    {
        "id": "entry_37",
        "instructions": "Your name is Bob Smith. You have a cancelled pediatrics appointment on 2025-04-08 at 9:15 a.m. (confirmation code HC1037) and need help rescheduling to 2025-04-11 at 1:00 p.m. Provide your confirmation code only if requested by the agent.",
        "actions": [
            {
                "name": "check_appointment_status",
                "arguments": {"confirmation_code": "HC1037"},
            },
            {
                "name": "get_available_slots",
                "arguments": {"appointment_date": "2025-04-11"},
            },
            {
                "name": "reschedule_appointment",
                "arguments": {
                    "confirmation_code": "HC1037",
                    "new_date": "2025-04-11",
                    "new_time": "13:00",
                },
            },
        ],
    },
    {
        "id": "entry_12",
        "instructions": "Your name is Charlie Williams. You have a general consultation appointment on 2025-04-07 (confirmation code HC1012) and wish to check the scheduled time. Provide your confirmation code only when asked.",
        "actions": [
            {"name": "get_appointment", "arguments": {"confirmation_code": "HC1012"}}
        ],
        "outputs": [
            "12:30"
        ]
    },
    {
        "id": "entry_129",
        "instructions": "Your name is Diana Brown. You want to check the status of your general medicine appointment (confirmation code HC1039). Do not reveal your confirmation code until explicitly requested.",
        "actions": [
            {
                "name": "check_appointment_status",
                "arguments": {"confirmation_code": "HC1039"},
            }
        ],
        "outputs": [
            "pending"
        ]
    },
    {
        "id": "entry_44",
        "instructions": "Your name is Ian Lee. You have a confirmed dentistry appointment on 2025-04-12 at 2:30 p.m. (confirmation code HC1044) and wish to check your appointment details. Only provide your confirmation code if explicitly requested.",
        "actions": [
            {"name": "get_appointment", "arguments": {"confirmation_code": "HC1044"}}
        ],
         "outputs": [
            "Smile Dental Center",
            "cleaning"
        ]
    },
    {
        "id": "entry_92",
        "instructions": "Your name is Amanda Hill. You want to retrieve all details for your confirmed family medicine appointment on 2025-04-11 at 3:15 p.m. (confirmation code HC1032). Reveal your confirmation code only if the agent asks for it.",
        "actions": [
            {"name": "get_appointment", "arguments": {"confirmation_code": "HC1032"}}
        ],
        "outputs": [
            "Community Health Center",
            "General"
        ]
    },
    {
        "id": "entry_104",
        "instructions": "Your name is Ian Lee. You want to review the details of your confirmed dentistry appointment on 2025-04-12 at 2:30 p.m. (confirmation code HC1044). Provide your confirmation code only when asked by the agent.",
        "actions": [
            {"name": "get_appointment", "arguments": {"confirmation_code": "HC1044"}}
        ],
        "outputs": [
            "Smile Dental Center",
            "cleaning"
        ]
    },
    {
        "id": "entry_72",
        "instructions": "Your name is George Martinez. You have a confirmed neurology appointment on 2025-04-11 at 1:00 p.m. (confirmation code HC1042) and want to verify the details. Provide your confirmation code only when prompted by the agent.",
        "actions": [
            {"name": "get_appointment", "arguments": {"confirmation_code": "HC1042"}},
            {
                "name": "generate_appointment_report",
                "arguments": {"appointment_date": "2025-04-11"},
            },
        ],
        "outputs": [
            "Neurology",
            "Westside Medical Center",
            "Migraine"
        ]
    },
    {
        "id": "entry_7",
        "instructions": "Your name is George Martinez. You have a Gastroenterology appointment on 2025-04-04 at 1:00 p.m. (confirmation code HC1007) and would like to know if you can reschedule it to 2025-04-11 at 1:00 p.m.. Do not reveal your confirmation code until the agent explicitly asks for it.",
        "actions": [
            {
                "name": "check_appointment_status",
                "arguments": {"confirmation_code": "HC1007"},
            },
            {
                "name": "get_available_slots",
                "arguments": {"appointment_date": "2025-04-11"},
            },
            {
                "name": "reschedule_appointment",
                "arguments": {
                    "confirmation_code": "HC1007",
                    "new_date": "2025-04-11",
                    "new_time": "13:00",
                },
            },
        ],
    },
    {
        "id": "entry_69",
        "instructions": "Your name is Diana Brown. You have a pending general medicine appointment on 2025-04-09 at 10:45 a.m. (confirmation code HC1039) and wish to know its status and confirm the appointment if needed. Provide your confirmation code only upon request.",
        "actions": [
            {
                "name": "check_appointment_status",
                "arguments": {"confirmation_code": "HC1039"},
            },
            {
                "name": "confirm_appointment",
                "arguments": {"confirmation_code": "HC1039"},
            },
        ],
    },
    {
        "id": "entry_45",
        "instructions": "Your name is Julia Kim. You have a ENT appointment on 2025-04-12 at 3:15 p.m. (confirmation code HC1045) and need to verify its status. Provide your confirmation code only upon the agent’s request.",
        "actions": [
            {
                "name": "check_appointment_status",
                "arguments": {"confirmation_code": "HC1045"},
            }
        ],
        "outputs": [
            "pending"
        ]
    },
    {
        "id": "entry_142",
        "instructions": "Your name is Quincy Scott. You have a psychiatry appointment on 2025-04-11 at 11:15 a.m. (confirmation code HC1022) and want to verify the current status. Provide your confirmation code only when explicitly requested.",
        "actions": [
            {
                "name": "check_appointment_status",
                "arguments": {"confirmation_code": "HC1022"},
            }
        ],
        "outputs": [
            "pending"
        ]
    },
    {
        "id": "entry_11",
        "instructions": "Your name is Alice Johnson. You recall a pending appointment on 2025-04-07 (confirmation code HC1011) for a child wellness check. You want to verify if it is still scheduled.",
        "actions": [
            {"name": "get_appointment", "arguments": {"confirmation_code": "HC1011"}},
            {
                "name": "check_appointment_status",
                "arguments": {"confirmation_code": "HC1011"},
            },
        ],
        "outputs": [
            "pending"
        ]
    },
    {
        "id": "entry_106",
        "instructions": "Your name is Kevin Moore. You want to check available appointment slots for 2025-04-09 at 9:30 a.m. to potentially reschedule your pending endocrinology appointment on 2025-04-08 at 9:30 a.m. (confirmation code HC1016). Provide your confirmation code only if the agent asks.",
        "actions": [
            {
                "name": "check_appointment_status",
                "arguments": {"confirmation_code": "HC1016"},
            },
            {
                "name": "get_available_slots",
                "arguments": {"appointment_date": "2025-04-09"},
            },
            {
                "name": "reschedule_appointment",
                "arguments": {
                    "confirmation_code": "HC1016",
                    "new_date": "2025-04-09",
                    "new_time": "09:30",
                },
            },
        ],
    },
    {
        "id": "entry_18",
        "instructions": "Your name is Mark Lewis. You have an oncology follow-up appointment on 2025-04-10 at 11:00 a.m. (confirmation code HC1018). You are checking if the next session details are correct. Reveal your confirmation code only when prompted.",
        "actions": [
            {"name": "get_appointment", "arguments": {"confirmation_code": "HC1018"}}
        ],
        "outputs": [
            "11:00",
            "confirmed",
            "Oncology",
            "Central Health Clinic",
            "chemotherapy"        
        ]
    },
    {
        "id": "entry_77",
        "instructions": "Your name is Laura Clark. You want to update the time for your confirmed rheumatology appointment on 2025-04-09 at 10:00 a.m.(confirmation code HC1017) to a new time slot at 11:00 a.m with Dr. Henry Roberts. Only provide your confirmation code when explicitly requested by the agent.",
        "actions": [
            {"name": "get_appointment", "arguments": {"confirmation_code": "HC1017"}},
            {
                "name": "get_available_slots",
                "arguments": {"appointment_date": "2025-04-09"},
            },
            {
                "name": "update_appointment",
                "arguments": {
                    "confirmation_code": "HC1017",
                    "appointment_date": "2025-04-09",
                    "appointment_time": "11:00"
                },
            },
        ],
    },
    {
        "id": "entry_139",
        "instructions": "Your name is Nancy Hall. You need to cancel your pending urology appointment on 2025-04-10 at 2:00 p.m.(confirmation code HC1019). Only share your confirmation code if the agent specifically requests it.",
        "actions": [
            {
                "name": "check_appointment_status",
                "arguments": {"confirmation_code": "HC1019"},
            },
            {
                "name": "cancel_appointment",
                "arguments": {"confirmation_code": "HC1019"},
            },
        ],
    },
    {
        "id": "entry_137",
        "instructions": "Your name is Laura Clark. You wish to reschedule your confirmed rheumatology appointment on 2025-04-09 at 10:00 a.m. (confirmation code HC1017) to 2025-04-12 at 10:00 a.m. due to a conflict. Only reveal your confirmation code on explicit request.",
        "actions": [
            {
                "name": "reschedule_appointment",
                "arguments": {
                    "confirmation_code": "HC1017",
                    "new_date": "2025-04-12",
                    "new_time": "10:00",
                },
            }
        ],
    },
    {
        "id": "entry_57",
        "instructions": "Your name is Victoria Wright. You want to check the status of your surgery evaluation appointment on 2025-04-09 at 9:15 a.m. (confirmation code HC1027). Provide your confirmation code only if the agent explicitly asks for it.",
        "actions": [
            {
                "name": "check_appointment_status",
                "arguments": {"confirmation_code": "HC1027"},
            }
        ],
        "outputs": [
            "pending"
        ]
    },
    {
        "id": "entry_97",
        "instructions": "Your name is Bob Smith. You need assistance rescheduling your cancelled pediatrics appointment (confirmation code HC1037) on 2025-04-08 at 09:15 a.m. to 2025-04-11 at 3:30 p.m. Provide your confirmation code only if the agent requests it.",
        "actions": [
            {"name": "get_appointment", "arguments": {"confirmation_code": "HC1037"}},
            {
                "name": "get_available_slots",
                "arguments": {"appointment_date": "2025-04-08"},
            },
            {
                "name": "reschedule_appointment",
                "arguments": {
                    "confirmation_code": "HC1037",
                    "new_date": "2025-04-11",
                    "new_time": "15:30",
                },
            },
        ],
    },
    {
        "id": "entry_1",
        "instructions": "Your name is Alice Johnson. You have an appointment on 2025-04-01 at 9:30 a.m. with confirmation code HC1001. You want to check the status of your appointment. Do not provide the confirmation code until asked. If the agent confirms your appointment, you want to cancel it.",
        "actions": [
            {
                "name": "check_appointment_status",
                "arguments": {"confirmation_code": "HC1001"},
            },
            {
                "name": "cancel_appointment",
                "arguments": {"confirmation_code": "HC1001"},
            },
        ],
    },
    {
        "id": "entry_95",
        "instructions": "Your name is Daniel Price. You want to check the status of your pending cardiology appointment on 2024-04-12 at 11:15 a.m. (confirmation code HC1035) and possibly update it. Provide your confirmation code only when asked by the agent.",
        "actions": [
            {"name": "get_appointment", "arguments": {"confirmation_code": "HC1035"}},
            {
                "name": "check_appointment_status",
                "arguments": {"confirmation_code": "HC1035"},
            },
        ],
    },
    {
        "id": "entry_99",
        "instructions": "Your name is Diana Brown. You want to check the status of your general medicine appointment on 2025-04-09 at 10:45 a.m.(confirmation code HC1039) without providing extra details. Reveal your confirmation code only on request by the agent.",
        "actions": [
            {"name": "get_appointment", "arguments": {"confirmation_code": "HC1039"}},
            {
                "name": "check_appointment_status",
                "arguments": {"confirmation_code": "HC1039"},
            },
        ],
        "outputs": [
            "10:45",
            "pending"
        ]
    },
    {
        "id": "entry_85",
        "instructions": "Your name is Tina Nelson. You have a pending infectious diseases appointment on 2025-4-12 at 3:00 p.m. (confirmation code HC1025). You need to check if there is an available time slot on 2025-04-11 at 3:00 p.m. for possible rescheduling. Only provide your confirmation code when prompted.",
        "actions": [
            {"name": "get_appointment", "arguments": {"confirmation_code": "HC1025"}},
            {
                "name": "get_available_slots",
                "arguments": {"appointment_date": "2025-04-11"},
            },
            {
                "name": "reschedule_appointment",
                "arguments": {
                    "confirmation_code": "HC1025",
                    "new_date": "2025-04-11",
                    "new_time": "15:00",
                },
            },
        ],
    },
    {
        "id": "entry_30",
        "instructions": "Your name is Yvonne Roberts. You have a confirmed emergency appointment (confirmation code HC1030) on 2025-04-10 at 12:15 p.m. and wish to review the appointment summary. Provide your confirmation code only if requested by the agent.",
        "actions": [
            {"name": "get_appointment", "arguments": {"confirmation_code": "HC1030"}},
            {
                "name": "generate_appointment_report",
                "arguments": {"appointment_date": "2025-04-10"},
            },
        ],
        "outputs": [
            "City Hospital",
            "Accident",
            "Emergency"
        ]
    },
    {
        "id": "entry_75",
        "instructions": "Your name is Julia Kim. You have a pending ENT appointment (confirmation code HC1045) on 2025-04-12 at 3:15 p.m. and want to know its current status. Reveal your confirmation code only upon request by the agent.",
        "actions": [
            {"name": "get_appointment", "arguments": {"confirmation_code": "HC1045"}},
            {
                "name": "check_appointment_status",
                "arguments": {"confirmation_code": "HC1045"},
            },
        ],
        "outputs": [
            "Pending"
        ]
    },
    {
        "id": "entry_46",
        "instructions": "Your name is Kevin Moore. You want to reschedule your pending endocrinology appointment (confirmation code HC1016) on 2025-04-08 at 9:30 a.m. to 2025-04-12 at 11:30 a.m. Wait for the agent to ask for your confirmation code before providing it.",
        "actions": [
            {"name": "get_appointment", "arguments": {"confirmation_code": "HC1016"}},
            {
                "name": "get_available_slots",
                "arguments": {"appointment_date": "2025-04-08"},
            },
            {
                "name": "reschedule_appointment",
                "arguments": {
                    "confirmation_code": "HC1016",
                    "new_date": "2025-04-12",
                    "new_time": "11:30",
                },
            },
        ],
    },
    {
        "id": "entry_112",
        "instructions": "Your name is Quincy Scott. You have a pending psychiatry appointment (confirmation code HC1022) on 2025-04-11 at 11:15 a.m. and wish to verify its status. Provide your confirmation code only if requested by the agent.",
        "actions": [
            {"name": "get_appointment", "arguments": {"confirmation_code": "HC1022"}},
            {
                "name": "check_appointment_status",
                "arguments": {"confirmation_code": "HC1022"},
            },
        ],
        "outputs": [
            "Pending"
        ]
    },
    {
        "id": "entry_16",
        "instructions": "Your name is Kevin Moore. You have a pending endocrinology appointment on 2025-04-08 at 9:30 a.m. (confirmation code HC1016). You would like to know more about the test requirements. Provide your confirmation code only when asked.",
        "actions": [
            {"name": "get_appointment", "arguments": {"confirmation_code": "HC1016"}}
        ],
        "outputs": [
            "Fasting"
        ]
    },
    {
        "id": "entry_103",
        "instructions": "Your name is Hannah Rodriguez. You have a pending ophthalmology appointment on 2025-04-11 at 1:45 p.m. (confirmation code HC1043) and wish to confirm its status. Only reveal your confirmation code if the agent explicitly asks.",
        "actions": [
            {
                "name": "check_appointment_status",
                "arguments": {"confirmation_code": "HC1043"},
            }
        ],
        "outputs": [
            "Pending"
        ]
    },
    {
        "id": "entry_67",
        "instructions": "Your name is Bob Smith. You need help rescheduling your cancelled pediatrics appointment that was on 2025-04-08 at 9:15 a.m. (confirmation code HC1037) to 2025-04-12 at 10:00 a.m. Wait for the agent to ask for your confirmation code before providing it.",
        "actions": [
            {
                "name": "check_appointment_status",
                "arguments": {"confirmation_code": "HC1037"},
            },
            {
                "name": "reschedule_appointment",
                "arguments": {
                    "confirmation_code": "HC1037",
                    "new_date": "2025-04-12",
                    "new_time": "10:00",
                },
            },
        ],
    },
    {
        "id": "entry_119",
        "instructions": "Your name is Xavier Evans. You need help rescheduling your cancelled radiology appointment (confirmation code HC1029) on 2025-04-10 at 11:30 a.m. You want to set up a new appointment with Dr. Lucas Baker at North Health Clinic on 2025-04-12 at 10:00 a.m. Share your confirmation code only if the agent explicitly asks for it.",
        "actions": [
            {"name": "get_appointment", "arguments": {"confirmation_code": "HC1029"}},
            {
                "name": "get_available_slots",
                "arguments": {"appointment_date": "2025-04-10"},
            },
            {"name": "list_doctors", "arguments": {}},
            {
                "name": "search_doctor_by_name",
                "arguments": {"doctor_name": "Dr. Lucas Baker"},
            },
            {
                "name": "reschedule_appointment",
                "arguments": {
                    "confirmation_code": "HC1029",
                    "new_date": "2025-04-12",
                    "new_time": "10:00",
                },
            },
        ],
    },
    {
        "id": "entry_17",
        "instructions": "Your name is Laura Clark. You have a confirmed rheumatology appointment on 2025-04-09 (confirmation code HC1017) and want to verify the scheduled time. Only provide your confirmation code if the agent specifically requests it.",
        "actions": [
            {
                "name": "get_appointment",
                "arguments": {"confirmation_code": "HC1017"},
            }
        ],
        "outputs": [
            "10:00"
        ]
    },
    {
        "id": "entry_50",
        "instructions": "Your name is Oliver Allen. You have a confirmed gynecology appointment on 2025-04-11 at 9:45 a.m. (confirmation code HC1020) and wish to reschedule your appointment to 2025-04-12 at 10:00 a.m. Reveal your confirmation code only when the agent requests it.",
        "actions": [
            {
                "name": "check_appointment_status",
                "arguments": {"confirmation_code": "HC1020"},
            },
            {
                "name": "reschedule_appointment",
                "arguments": {
                    "confirmation_code": "HC1020",
                    "new_date": "2025-04-12",
                    "new_time": "10:00",
                },
            },
        ],
    },
    {
        "id": "entry_87",
        "instructions": "Your name is Victoria Wright. You want to check the status of your pending surgery evaluation appointment on 2025-04-09 at 9:15 a.m. (confirmation code HC1027) before proceeding. If the appointment is still pending, you would like to confirm it. Provide your confirmation code only on request.",
        "actions": [
            {
                "name": "check_appointment_status",
                "arguments": {"confirmation_code": "HC1027"},
            },
            {
                "name": "confirm_appointment",
                "arguments": {"confirmation_code": "HC1027"},
            },
        ],
    },
    {
        "id": "entry_107",
        "instructions": "Your name is Laura Clark. You wish to reschedule your confirmed rheumatology appointment on 2025-04-09 at 10:00 a.m. (confirmation code HC1017) to 2025-04-10 at 8:30 a.m. Only reveal your confirmation code when explicitly requested by the agent.",
        "actions": [
            {"name": "get_appointment", "arguments": {"confirmation_code": "HC1017"}},
            {
                "name": "get_available_slots",
                "arguments": {"appointment_date": "2025-04-10"},
            },
            {
                "name": "reschedule_appointment",
                "arguments": {
                    "confirmation_code": "HC1017",
                    "new_date": "2025-04-10",
                    "new_time": "08:30",
                },
            },
        ],
    },
    {
        "id": "entry_49",
        "instructions": "Your name is Nancy Hall. You want to cancel your pending urology appointment (confirmation code HC1019) on 2025-04-10 at 2:00 p.m. Provide your confirmation code only if the agent specifically asks.",
        "actions": [
            {"name": "get_appointment", "arguments": {"confirmation_code": "HC1019"}},
            {
                "name": "cancel_appointment",
                "arguments": {"confirmation_code": "HC1019"},
            },
        ],
    },
    {
        "id": "entry_66",
        "instructions": "Your name is Alice Johnson. You wish to update your confirmed dermatology follow-up on 2025-04-08 at 8:30 a.m. (confirmation code HC1036) by changing the appointment time to 9:00 a.m. Provide your confirmation code only when prompted.",
        "actions": [
            {"name": "get_appointment", "arguments": {"confirmation_code": "HC1036"}},
            {
                "name": "get_available_slots",
                "arguments": {"appointment_date": "2025-04-08"},
            },
            {
                "name": "reschedule_appointment",
                "arguments": {
                    "confirmation_code": "HC1036",
                    "new_date": "2025-04-08",
                    "new_time": "09:00",
                },
            },
        ],
    },
    {
        "id": "entry_14",
        "instructions": "Your name is George Martinez. You have a neurology appointment on 2025-04-08 at 3:30 p.m. (confirmation code HC1014) that is pending. You want to know if it can be confirmed. Provide your confirmation code only if the agent requests it.",
        "actions": [
            {
                "name": "check_appointment_status",
                "arguments": {"confirmation_code": "HC1014"},
            },
            {
                "name": "confirm_appointment",
                "arguments": {"confirmation_code": "HC1014"},
            },
        ],
    },
    {
        "id": "entry_218",
        "tags": ["complex"],
        "instructions": "You are Rachel Adams. Check your recent nephrology appointment (HC1023) and review the history of all your previous visits (your DOB is 1986-09-19) to ensure nothing is missed. Review Dr. Logan Wright's details if he is assigned for your next appointment. If the appointment (HC1023) remains open, rate the visit and confirm it if it has not yet been finalized.",
        "actions": [
            {
                "name": "search_patient_by_name",
                "arguments": {"patient_name": "Rachel Adams"},
            },
            {"name": "get_appointment", "arguments": {"confirmation_code": "HC1023"}},
            {
                "name": "get_appointment_history",
                "arguments": {
                    "patient_name": "Rachel Adams"                
                },
            },
            {
                "name": "search_doctor_by_name",
                "arguments": {"doctor_name": "Dr. Logan Wright"},
            },
            {
                "name": "check_appointment_status",
                "arguments": {"confirmation_code": "HC1023"},
            },
        ],
        "outputs": [
            "Logan Wright",
            "North Health Clinic"
        ]
    },
    {
        "id": "entry_217",
        "tags": ["complex"],
        "instructions": "You are Quincy Scott. Confirm that your psychiatry session (HC1022) is scheduled with Dr. Isabella King, ensuring she is the correct specialist. Check the current status of your appointment, update the reason for your visit if your symptoms have changed, and receive a brief summary notification of the changes. Also verify that the new information is recorded in the schedule.",
        "actions": [
            {
                "name": "check_appointment_status",
                "arguments": {"confirmation_code": "HC1022"},
            },
            {"name": "list_doctors", "arguments": {}},
            {
                "name": "notify_patient",
                "arguments": {
                    "confirmation_code": "HC1022",
                    "message": 'Appointment HC1022 "Reason" updated to "experiencing more symptoms related to depression"',
                },
            },
            {"name": "get_appointment", "arguments": {"confirmation_code": "HC1022"}},
        ],
        "outputs": [
            "Central Mental Health Clinic",
            "Isabella King"
        ]
    },
    {
        "id": "entry_208",
        "tags": ["complex"],
        "instructions": "You are Hannah Rodriguez. Verify that everything is in order with your ophthalmology appointment (HC1008) on 2025-04-05 at 10:30 a.m. Check how busy the clinic is on 2025-04-11. If you decide you need an additional consultation with Dr. Robert Brown, book a new appointment with him on 2025-04-11 at 1:45 p.m. for a routine eye exam (HC1843), and confirm the extra visit.",
        "actions": [
            {
                "name": "search_patient_by_name",
                "arguments": {"patient_name": "Hannah Rodriguez"},
            },
            {"name": "get_appointment", "arguments": {"confirmation_code": "HC1008"}},
            {
                "name": "get_available_slots",
                "arguments": {"appointment_date": "2025-04-11"},
            },
            {
                "name": "search_doctor_by_name",
                "arguments": {"doctor_name": "Dr. Robert Brown"},
            },
            {
                "name": "create_appointment",
                "arguments": {
                    "confirmation_code": "HC1843",
                    "appointment_id": "A1043",
                    "patient_name": "Hannah Rodriguez",
                    "doctor_name": "Dr. Robert Brown",
                    "appointment_date": "2025-04-11",
                    "appointment_time": "13:45",
                    "status": "pending",
                    "department": "Ophthalmology",
                    "clinic": "Central Health clinic",
                    "reason": "Routine Eye Exam",
                    "notes": "",
                },
            },
            {
                "name": "confirm_appointment",
                "arguments": {"confirmation_code": "HC1843"},
            },
        ],
    },
    {
        "id": "entry_289",
        "tags": ["complex"],
        "instructions": "You are Charlie Williams, planning a neurology consultation with Dr. Laura Martinez. Before scheduling, verify that Dr. Martinez is indeed a neurologist. Check which time slots are available on 2025-04-06. Book any available slot on that day and immediately confirm the appointment. Finally, receive a brief notification confirming your new appointment.",
        "actions": [
            {
                "name": "search_doctor_by_name",
                "arguments": {"doctor_name": "Dr. Laura Martinez"},
            },
            {
                "name": "search_patient_by_name",
                "arguments": {"patient_name": "Charlie Williams"},
            },
            {
                "name": "get_available_slots",
                "arguments": {"appointment_date": "2025-04-06"},
            },
            {
                "name": "create_appointment",
                "arguments": {
                    "confirmation_code": "HC20250406-1000",
                    "appointment_id": "A1001",
                    "patient_name": "Charlie Williams",
                    "doctor_name": "Dr. Laura Martinez",
                    "appointment_date": "2025-04-06",
                    "appointment_time": "09:00",
                    "status": "",
                    "department": "Neurology",
                    "clinic": "Westside Medical Center",
                    "reason": "Neurology consultation",
                    "notes": "",
                },
            }
        ],
    },
    {
        "id": "entry_220",
        "tags": ["complex"],
        "instructions": "You are Tina Nelson. Review the details of your infectious disease appointment (HC1025) on 2025-04-12 at 3:00 p.m. and ensure that the system has you registered under your name. Then, if you're curious, look up the list of other registered patients and all the appointments in the clinic. After that, the process is complete.",
        "actions": [
            {
                "name": "search_patient_by_name",
                "arguments": {"patient_name": "Tina Nelson"},
            },
            {"name": "get_appointment", "arguments": {"confirmation_code": "HC1025"}},
        ],
        "outputs": [
            "15:00",
            "pending",
            "Tina Nelson"
        ]
    },
    {
        "id": "entry_219",
        "tags": ["complex"],
        "instructions": "You are Samuel Baker. Check the details of your immunology check (HC1024) and reschedule it to 2025-04-07 at 10:00, update the notes with a new concern, and determine how busy the clinic is on the chosen day. After making the changes, receive a notification.",
        "actions": [
            {
                "name": "search_patient_by_name",
                "arguments": {"patient_name": "Samuel Baker"},
            },
            {"name": "get_appointment", "arguments": {"confirmation_code": "HC1024"}},
            {
                "name": "reschedule_appointment",
                "arguments": {
                    "confirmation_code": "HC1024",
                    "new_date": "2025-04-07",
                    "new_time": "10:00",
                },
            },
            {
                "name": "update_appointment",
                "arguments": {
                    "confirmation_code": "HC1024",
                    "appointment_date": "2025-04-07",
                    "appointment_time": "10:00",
                    "status": "",
                    "doctor_name": "",
                    "department": "",
                    "clinic": "",
                    "reason": "",
                    "notes": "New concern",
                },
            },
            {
                "name": "notify_patient",
                "arguments": {
                    "confirmation_code": "HC1024",
                    "message": "Immunology appointment has been rescheduled to 2025-04-07 at 10:00 a.m. with new concerns noted",
                },
            },
        ],
        "outputs": [
            "rescheduled",
            "10:00",
        ]
    },
    {
        "id": "entry_290",
        "tags": ["complex"],
        "instructions": "You are Edward Davis. Ensure that the system has your information. Look up the details of your general check-up appointment (HC1005) and verify its status. Then, receive a brief update or reminder to keep track of it, and view all upcoming clinic visits.",
        "actions": [
            {
                "name": "search_patient_by_name",
                "arguments": {"patient_name": "Edward Davis"},
            },
            {"name": "get_appointment", "arguments": {"confirmation_code": "HC1005"}},
            {
                "name": "check_appointment_status",
                "arguments": {"confirmation_code": "HC1005"},
            },
            {
                "name": "notify_patient",
                "arguments": {
                    "confirmation_code": "HC1005",
                    "message": "Keep track of General Medicine appointment on 2025-04-03 at 3:30 p.m. at Central Health Clinic",
                },
            },
            {"name": "list_appointments", "arguments": {}},
        ],
    },
    {
        "id": "entry_211",
        "tags": ["complex"],
        "instructions": "You are Kevin Moore. Ensure that the system recognizes your information, and then check the status of your pending pediatric appointment (HC1011) on 2025-04-07 at 11:00 a.m. If necessary, reschedule the appointment from 11:00 a.m. to 11:30 a.m. Once confirmed, receive a notification, and after the visit, provide feedback.",
        "actions": [
            {
                "name": "search_patient_by_name",
                "arguments": {"patient_name": "Kevin Moore"},
            },
            {
                "name": "check_appointment_status",
                "arguments": {"confirmation_code": "HC1011"},
            },
            {
                "name": "reschedule_appointment",
                "arguments": {
                    "confirmation_code": "HC1011",
                    "new_date": "2025-04-07 ",
                    "new_time": "11:30",
                },
            },
            {
                "name": "notify_patient",
                "arguments": {
                    "confirmation_code": "HC1011",
                    "message": "You are confirmed for an appointment on 2025-04-07 at 11:30 a.m. with Dr. Michael Thompson",
                },
            },
            {
                "name": "rate_appointment",
                "arguments": {"confirmation_code": "HC1011", "rating": "4"},
            },
        ],
        "outputs": [
            "rescheduled",
            "11:30",
        ]
    },
    {
        "id": "entry_215",
        "tags": ["complex"],
        "instructions": "You are Oliver Allen. Check the details of your gynecology appointment (HC1020) on 2025-04-11 at 9:45 a.m. and determine how busy the clinic is on 2025-04-11. Then reschedule your appointment to 2025-04-12 at 12:30 p.m. and confirm the change, receiving a notification.",
        "actions": [
            {
                "name": "search_patient_by_name",
                "arguments": {"patient_name": "Oliver Allen"},
            },
            {"name": "get_appointment", "arguments": {"confirmation_code": "HC1020"}},
            {
                "name": "generate_appointment_report",
                "arguments": {"appointment_date": "2025-04-11"},
            },
            {
                "name": "reschedule_appointment",
                "arguments": {
                    "confirmation_code": "HC1020",
                    "new_date": "2025-04-12",
                    "new_time": "12:30",
                },
            },
        ],
        "outputs": [
            "rescheduled",
            "12:30",
        ]
    },
    {
        "id": "entry_210",
        "tags": ["complex"],
        "instructions": "You are Julia Kim. Verify the date and status of your ENT appointment (HC1010). Also, review your entire appointment history (your DOB is 1979-01-10) to identify any patterns, and check how busy the clinic is on 2025-04-06.",
        "actions": [
            {
                "name": "search_patient_by_name",
                "arguments": {"patient_name": "Julia Kim"},
            },
            {
                "name": "check_appointment_status",
                "arguments": {"confirmation_code": "HC1010"},
            },
            {
                "name": "get_appointment_history",
                "arguments": {
                    "patient_name": "Julia Kim"                
                },
            },
            {
                "name": "generate_appointment_report",
                "arguments": {"appointment_date": "1979-01-10"},
            },
        ],
        "outputs": [
            "09:00",
            "15:15"
        ]
    },
    {
        "id": "entry_209",
        "tags": ["complex"],
        "instructions": "You are Ian Lee. Check the status of your dentistry visit (HC1009); if it is pending confirmation, verify it. Also, confirm whether Dr. Linda Davis is working at the clinic. After that, finalize your appointment and review the list of other registered patients at the clinic.",
        "actions": [
            {
                "name": "search_patient_by_name",
                "arguments": {"patient_name": "Ian Lee"},
            },
            {
                "name": "check_appointment_status",
                "arguments": {"confirmation_code": "HC1009"},
            },
            {
                "name": "confirm_appointment",
                "arguments": {"confirmation_code": "HC1009"},
            },
            {
                "name": "search_doctor_by_name",
                "arguments": {"doctor_name": "Dr. Linda Davis"},
            },
        ],
    },
    {
        "id": "entry_212",
        "tags": ["complex"],
        "instructions": "You are Laura Clark. Check the status of your general check-up appointment (HC1012) on 2025-04-07 at 12:30 p.m. in the system. If it is not confirmed, update the notes with your new symptoms of an aching back, and then confirm the appointment. Afterwards, leave a rating of 4 for the consultation and review the list of upcoming clinic visits.",
        "actions": [
            {
                "name": "search_patient_by_name",
                "arguments": {"patient_name": "Laura Clark"},
            },
            {
                "name": "check_appointment_status",
                "arguments": {"confirmation_code": "HC1012"},
            },
            {
                "name": "update_appointment",
                "arguments": {
                    "confirmation_code": "HC1012",
                    "appointment_date": "",
                    "appointment_time": "",
                    "status": "",
                    "doctor_name": "",
                    "department": "",
                    "clinic": "",
                    "reason": "",
                    "notes": "Back ache",
                },
            },
            {
                "name": "confirm_appointment",
                "arguments": {"confirmation_code": "HC1012"},
            },
            {
                "name": "rate_appointment",
                "arguments": {"confirmation_code": "HC1012", "rating": "4"},
            },
            {"name": "list_appointments", "arguments": {}},
        ],
    },
    {
        "id": "entry_214",
        "tags": ["complex"],
        "instructions": "You are Nancy Hall. Verify that the system recognizes your information for your urology appointment (HC1019) and receive an update on its status. Clarify your reason for the visit or add a note, then confirm the final booking and receive a notification.",
        "actions": [
            {
                "name": "search_patient_by_name",
                "arguments": {"patient_name": "Nancy Hall"},
            },
            {
                "name": "check_appointment_status",
                "arguments": {"confirmation_code": "HC1019"},
            },
            {
                "name": "update_appointment",
                "arguments": {
                    "confirmation_code": "HC1019",
                    "appointment_date": "",
                    "appointment_time": "",
                    "status": "",
                    "doctor_name": "",
                    "department": "",
                    "clinic": "",
                    "reason": "",
                    "notes": "UTI",
                },
            },
            {
                "name": "confirm_appointment",
                "arguments": {"confirmation_code": "HC1019"},
            },
            {
                "name": "notify_patient",
                "arguments": {
                    "confirmation_code": "HC1019",
                    "message": "Urology Appointment on 2025-04-10 at 2:00 p.m. at Downtown Medical Clinic is confirmed",
                },
            },
        ],
    },
    {
        "id": "entry_291",
        "tags": ["complex"],
        "instructions": "You are George Martinez. Your gastroenterology appointment (HC1007) is confirmed, but you want an earlier time on the same day. Check if a morning slot is available, and if so, move your appointment to 08:00 slot. Update the reason for your visit if your symptoms have changed, then confirm the booking and receive a notification.",
        "actions": [
            {
                "name": "search_patient_by_name",
                "arguments": {"patient_name": "George Martinez"},
            },
            {"name": "get_appointment", "arguments": {"confirmation_code": "HC1007"}},
            {
                "name": "get_available_slots",
                "arguments": {"appointment_date": "2025-04-04"},
            },
            {
                "name": "reschedule_appointment",
                "arguments": {
                    "confirmation_code": "HC1007",
                    "new_date": "2025-04-04",
                    "new_time": "08:00",
                },
            },
            {
                "name": "confirm_appointment",
                "arguments": {"confirmation_code": "HC1007"},
            },
            {
                "name": "notify_patient",
                "arguments": {
                    "confirmation_code": "HC1007",
                    "message": "Gastroenterology appointment at Downtown Clinic has been rescheduled to 2025-04-04 at 8:00 a.m.",
                },
            },
        ],
    },
    {
        "id": "entry_292",
        "tags": ["complex"],
        "instructions": "You are Edward Davis. Check the status of your gastroenterology appointment (HC1013). If the appointment is active, cancel it to remove it from your schedule. Then, search for an available slot on 2025-04-08, book a new appointment with Dr. James Wilson, and confirm it to avoid any confusion.",
        "actions": [
            {
                "name": "search_patient_by_name",
                "arguments": {"patient_name": "Edward Davis"},
            },
            {
                "name": "check_appointment_status",
                "arguments": {"confirmation_code": "HC1013"},
            },
            {
                "name": "cancel_appointment",
                "arguments": {"confirmation_code": "HC1013"},
            },
            {
                "name": "get_available_slots",
                "arguments": {"appointment_date": "2025-04-08"},
            },
            {
                "name": "create_appointment",
                "arguments": {
                    "confirmation_code": "HC9999",
                    "appointment_id": "",
                    "patient_name": "Edward Davis",
                    "doctor_name": "Dr. James Wilson",
                    "appointment_date": "2025-04-08",
                    "appointment_time": "09:00",
                    "status": "",
                    "department": "Gastroenterology",
                    "clinic": "Downtown Clinic",
                    "reason": "",
                    "notes": "",
                },
            },
            {
                "name": "confirm_appointment",
                "arguments": {"confirmation_code": "HC9999"},
            },
        ],
        "outputs": [
            "canceled",
            "scheduled",
            "confirmed",
        ]
    },
    {
        "id": "entry_294",
        "tags": ["complex"],
        "instructions": "You are Alice Johnson and suspect you have an upcoming cardiology appointment (HC1001) but don’t remember the details. First, ensure that the system recognizes you by name. Then look up the appointment details and check if it is still active. Add a note about your blood pressure readings. Finally, confirm the appointment and request a brief reminder of the date.",
        "actions": [
            {
                "name": "search_patient_by_name",
                "arguments": {"patient_name": "Alice Johnson"},
            },
            {
                "name": "check_appointment_status",
                "arguments": {"confirmation_code": "HC1001"},
            },
            {
                "name": "confirm_appointment",
                "arguments": {"confirmation_code": "HC1001"},
            },
            {
                "name": "notify_patient",
                "arguments": {
                    "confirmation_code": "HC1001",
                    "message": "Cardiology appointment on 2025-04-01",
                },
            },
        ],
    },
    {
        "id": "entry_295",
        "tags": ["complex"],
        "instructions": "You are Diana Brown. If you are not entirely sure about your appointment details (HC1004) on 2025-04-03 at 2:00 p.m., first check them. Then review your history of past clinic visits (your DOB is 1985-02-28). After reviewing, rate your current pediatric appointment and add a minor update to its notes to include lab test results.",
        "actions": [
            {
                "name": "search_patient_by_name",
                "arguments": {"patient_name": "Diana Brown"},
            },
            {"name": "get_appointment", "arguments": {"confirmation_code": "HC1004"}},
            {
                "name": "get_appointment_history",
                "arguments": {
                    "patient_name": "Diana Brown"                
                },
            },
            {
                "name": "rate_appointment",
                "arguments": {"confirmation_code": "HC1004", "rating": "4"},
            },
            {
                "name": "update_appointment",
                "arguments": {
                    "confirmation_code": "HC1004",
                    "appointment_date": "",
                    "appointment_time": "",
                    "status": "",
                    "doctor_name": "",
                    "department": "",
                    "clinic": "",
                    "reason": "",
                    "notes": "Bring vaccination records and lab test results.",
                },
            },
        ],
        "outputs": [
            "updated",
            "results",
        ]
    },
]
