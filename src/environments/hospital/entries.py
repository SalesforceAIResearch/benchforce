entries = [
    {
        "id": "entry_1",
        "instructions": "Your name is Dr. Sarah Johnson. You need to schedule an appointment for patient Emily Davis for January 25, 2024 at 10:00 AM with yourself in Cardiology. Confirm the appointment details and ask if the patient needs any special instructions.",
        "actions": [
            {
                "name": "schedule_appointment",
                "arguments": {
                    "patient_identifier": "Emily Davis",
                    "doctor_identifier": "Dr. Sarah Johnson",
                    "appointment_time": "10:00 AM",
                    "appointment_date": "2024-01-25",
                    "department": "Cardiology"
                },
            },
        ],
    },
    {
        "id": "entry_2", 
        "instructions": "You are a nurse checking on patient Robert Wilson. He wants to know his current medication schedule and needs to update his emergency contact to his daughter Lisa Wilson at phone number 555-9876. Please retrieve his medication info and update his contact.",
        "actions": [
            {
                "name": "get_patient_medications",
                "arguments": {
                    "patient_identifier": "Robert Wilson"
                },
            },
            {
                "name": "update_emergency_contact",
                "arguments": {
                    "patient_identifier": "Robert Wilson",
                    "contact_name": "Lisa Wilson",
                    "contact_phone": "555-9876"
                },
            },
        ],
    },
    {
        "id": "entry_3",
        "instructions": "You are a hospital administrator. Patient Maria Rodriguez wants to check her recent lab results and schedule a follow-up appointment with Dr. Amanda Taylor in Internal Medicine for January 22, 2024 at 2:00 PM.",
        "actions": [
            {
                "name": "get_lab_results",
                "arguments": {
                    "patient_identifier": "Maria Rodriguez"
                },
            },
            {
                "name": "schedule_appointment", 
                "arguments": {
                    "patient_identifier": "Maria Rodriguez",
                    "doctor_identifier": "Dr. Amanda Taylor",
                    "appointment_time": "2:00 PM",
                    "appointment_date": "2024-01-22",
                    "department": "Internal Medicine"
                },
            },
        ],
    },
    {
        "id": "entry_4",
        "instructions": "You are a receptionist. Patient John Smith called to cancel his appointment with Dr. Sarah Johnson scheduled for January 15, 2024 at 9:00 AM. Process the cancellation and confirm it with the patient.",
        "actions": [
            {
                "name": "cancel_appointment",
                "arguments": {
                    "patient_identifier": "John Smith",
                    "doctor_identifier": "Dr. Sarah Johnson",
                    "appointment_date": "2024-01-15",
                    "appointment_time": "9:00 AM"
                },
            },
        ],
    },
    {
        "id": "entry_5",
        "instructions": "You are Dr. Robert Chen. You need to check the information for patient Jennifer Brown who has an appointment today, and review her current medications before the consultation.",
        "actions": [
            {
                "name": "get_patient_info",
                "arguments": {
                    "patient_identifier": "Jennifer Brown"
                },
            },
            {
                "name": "get_patient_medications",
                "arguments": {
                    "patient_identifier": "Jennifer Brown"
                },
            },
        ],
    },
    {
        "id": "entry_6",
        "instructions": "You are a care coordinator managing patient John Smith who is being transferred from Emergency to Cardiology. First, verify his patient information and emergency contact details. Then review his current medications to check for any cardiac-related prescriptions. Check his recent lab results to assess his cardiac status. Finally, get information about Dr. Sarah Johnson (his cardiologist) to confirm her availability and schedule a follow-up appointment for January 26, 2024 at 11:00 AM.",
        "actions": [
            {
                "name": "get_patient_info",
                "arguments": {
                    "patient_identifier": "John Smith"
                },
            },
            {
                "name": "get_patient_medications",
                "arguments": {
                    "patient_identifier": "John Smith"
                },
            },
            {
                "name": "get_lab_results",
                "arguments": {
                    "patient_identifier": "John Smith"
                },
            },
            {
                "name": "get_doctor_info",
                "arguments": {
                    "doctor_identifier": "Dr. Sarah Johnson"
                },
            },
            {
                "name": "schedule_appointment",
                "arguments": {
                    "patient_identifier": "John Smith",
                    "doctor_identifier": "Dr. Sarah Johnson",
                    "appointment_time": "11:00 AM",
                    "appointment_date": "2024-01-26",
                    "department": "Cardiology"
                },
            },
        ],
    },
    {
        "id": "entry_7",
        "instructions": "You are Dr. Amanda Taylor dealing with an appointment conflict. Patient Maria Rodriguez has a scheduled appointment with you on January 16, 2024 at 11:00 AM, but you have an emergency and need to reschedule. First, review her patient information and current medications to assess urgency. Check her lab results to determine if the appointment is time-sensitive. Then cancel her existing appointment and get information about Dr. Jennifer Martinez (Dermatology) to see if she can handle the follow-up. Finally, schedule a new appointment with Dr. Martinez for January 20, 2024 at 3:00 PM.",
        "actions": [
            {
                "name": "get_patient_info",
                "arguments": {
                    "patient_identifier": "Maria Rodriguez"
                },
            },
            {
                "name": "get_patient_medications",
                "arguments": {
                    "patient_identifier": "Maria Rodriguez"
                },
            },
            {
                "name": "get_lab_results",
                "arguments": {
                    "patient_identifier": "Maria Rodriguez"
                },
            },
            {
                "name": "cancel_appointment",
                "arguments": {
                    "patient_identifier": "Maria Rodriguez",
                    "doctor_identifier": "Dr. Amanda Taylor",
                    "appointment_date": "2024-01-16",
                    "appointment_time": "11:00 AM"
                },
            },
            {
                "name": "get_doctor_info",
                "arguments": {
                    "doctor_identifier": "Dr. Jennifer Martinez"
                },
            },
            {
                "name": "schedule_appointment",
                "arguments": {
                    "patient_identifier": "Maria Rodriguez",
                    "doctor_identifier": "Dr. Jennifer Martinez",
                    "appointment_time": "3:00 PM",
                    "appointment_date": "2024-01-20",
                    "department": "Dermatology"
                },
            },
        ],
    },
    {
        "id": "entry_8",
        "instructions": "You are a discharge nurse preparing patient Michael Davis for discharge after an orthopedic procedure. Start by getting his patient information to verify discharge readiness. Review his current medications to identify any post-surgical medications. Check his lab results to ensure he's medically stable. Get information about his surgeon Dr. Robert Chen to confirm post-op instructions. Schedule a follow-up appointment with Dr. Chen for January 28, 2024 at 1:00 PM. Finally, update his emergency contact to his wife Sarah Davis at phone number 555-3333 who will be caring for him during recovery.",
        "actions": [
            {
                "name": "get_patient_info",
                "arguments": {
                    "patient_identifier": "Michael Davis"
                },
            },
            {
                "name": "get_patient_medications",
                "arguments": {
                    "patient_identifier": "Michael Davis"
                },
            },
            {
                "name": "get_lab_results",
                "arguments": {
                    "patient_identifier": "Michael Davis"
                },
            },
            {
                "name": "get_doctor_info",
                "arguments": {
                    "doctor_identifier": "Dr. Robert Chen"
                },
            },
            {
                "name": "schedule_appointment",
                "arguments": {
                    "patient_identifier": "Michael Davis",
                    "doctor_identifier": "Dr. Robert Chen",
                    "appointment_time": "1:00 PM",
                    "appointment_date": "2024-01-28",
                    "department": "Orthopedics"
                },
            },
            {
                "name": "update_emergency_contact",
                "arguments": {
                    "patient_identifier": "Michael Davis",
                    "contact_name": "Sarah Davis",
                    "contact_phone": "555-3333"
                },
            },
        ],
    },
    {
        "id": "entry_9",
        "instructions": "You are a medical assistant supporting Dr. David Brown (Neurology) for a complex patient consultation. Patient Sarah Miller is being evaluated for neurological symptoms. First, get her patient information to review her demographics and contact details. Check her current medications to identify any neurological drugs. Review her lab results to look for any neurological markers. Get Dr. Brown's information to confirm his neurology specialty. Schedule her initial consultation for January 24, 2024 at 4:00 PM. Then immediately schedule a follow-up appointment for January 31, 2024 at 4:00 PM to review test results.",
        "actions": [
            {
                "name": "get_patient_info",
                "arguments": {
                    "patient_identifier": "Sarah Miller"
                },
            },
            {
                "name": "get_patient_medications",
                "arguments": {
                    "patient_identifier": "Sarah Miller"
                },
            },
            {
                "name": "get_lab_results",
                "arguments": {
                    "patient_identifier": "Sarah Miller"
                },
            },
            {
                "name": "get_doctor_info",
                "arguments": {
                    "doctor_identifier": "Dr. David Brown"
                },
            },
            {
                "name": "schedule_appointment",
                "arguments": {
                    "patient_identifier": "Sarah Miller",
                    "doctor_identifier": "Dr. David Brown",
                    "appointment_time": "4:00 PM",
                    "appointment_date": "2024-01-24",
                    "department": "Neurology"
                },
            },
            {
                "name": "schedule_appointment",
                "arguments": {
                    "patient_identifier": "Sarah Miller",
                    "doctor_identifier": "Dr. David Brown",
                    "appointment_time": "4:00 PM",
                    "appointment_date": "2024-01-31",
                    "department": "Neurology"
                },
            },
        ],
    },
    {
        "id": "entry_10",
        "instructions": "You are a quality assurance coordinator investigating a potential medication error. Patient Emily Taylor called with concerns about her prescription. Start by getting her patient information to verify her identity and contact details. Review her current medications to identify any potential issues. Check her lab results to see if there are any abnormal values that might indicate medication problems. Get information about Dr. William Davis (her psychiatrist) to verify his prescribing authority. If everything checks out, schedule a medication review appointment with Dr. Davis for January 23, 2024 at 10:00 AM. Finally, update her emergency contact to her brother Mark Taylor at phone number 555-4444.",
        "actions": [
            {
                "name": "get_patient_info",
                "arguments": {
                    "patient_identifier": "Emily Taylor"
                },
            },
            {
                "name": "get_patient_medications",
                "arguments": {
                    "patient_identifier": "Emily Taylor"
                },
            },
            {
                "name": "get_lab_results",
                "arguments": {
                    "patient_identifier": "Emily Taylor"
                },
            },
            {
                "name": "get_doctor_info",
                "arguments": {
                    "doctor_identifier": "Dr. William Davis"
                },
            },
            {
                "name": "schedule_appointment",
                "arguments": {
                    "patient_identifier": "Emily Taylor",
                    "doctor_identifier": "Dr. William Davis",
                    "appointment_time": "10:00 AM",
                    "appointment_date": "2024-01-23",
                    "department": "Psychiatry"
                },
            },
            {
                "name": "update_emergency_contact",
                "arguments": {
                    "patient_identifier": "Emily Taylor",
                    "contact_name": "Mark Taylor",
                    "contact_phone": "555-4444"
                },
            },
        ],
    },
    {
        "id": "entry_11",
        "instructions": "You are Dr. John Adams in the Emergency Department. Patient Alice Johnson came in with severe chest pain and abnormal EKG findings. After initial stabilization, you need to urgently refer her to Cardiology for immediate evaluation. First, get her patient information to verify her identity and medical history. Check her current medications for any cardiac drugs. Then create an urgent referral to Dr. Sarah Johnson in Cardiology for 'Acute coronary syndrome evaluation' with detailed clinical notes. Finally, schedule an emergency appointment for January 24, 2024 at 2:00 PM.",
        "actions": [
            {
                "name": "get_patient_info",
                "arguments": {
                    "patient_identifier": "Alice Johnson"
                },
            },
            {
                "name": "get_patient_medications",
                "arguments": {
                    "patient_identifier": "Alice Johnson"
                },
            },
            {
                "name": "create_referral",
                "arguments": {
                    "patient_identifier": "Alice Johnson",
                    "referring_doctor_identifier": "Dr. John Adams",
                    "referred_to_doctor_identifier": "Dr. Sarah Johnson",
                    "referred_to_department": "Cardiology",
                    "priority": "urgent"
                },
            },
            {
                "name": "schedule_appointment",
                "arguments": {
                    "patient_identifier": "Alice Johnson",
                    "doctor_identifier": "Dr. Sarah Johnson",
                    "appointment_time": "2:00 PM",
                    "appointment_date": "2024-01-24",
                    "department": "Cardiology"
                },
            },
        ],
    },
    {
        "id": "entry_12",
        "instructions": "You are Dr. Jennifer Martinez in Dermatology. You received a referral for patient Jennifer Brown from Dr. Robert Chen in Orthopedics regarding a suspicious skin lesion. First, get the patient's information and review her current medications. Check all referrals for this patient to understand the clinical context. Review her lab results for any relevant findings. After your evaluation, update the referral status to 'completed' with findings that the lesion is a benign seborrheic keratosis, and create a follow-up referral back to Orthopedics for continued care of her original orthopedic issue.",
        "actions": [
            {
                "name": "get_patient_info",
                "arguments": {
                    "patient_identifier": "Jennifer Brown"
                },
            },
            {
                "name": "get_patient_medications",
                "arguments": {
                    "patient_identifier": "Jennifer Brown"
                },
            },
            {
                "name": "get_patient_referrals",
                "arguments": {
                    "patient_identifier": "Jennifer Brown"
                },
            },
            {
                "name": "get_lab_results",
                "arguments": {
                    "patient_identifier": "Jennifer Brown"
                },
            },
            {
                "name": "update_referral_status",
                "arguments": {
                    "patient_identifier": "Jennifer Brown",
                    "referred_to_doctor_identifier": "Dr. Robert Chen",
                    "new_status": "completed"
                },
            },
            {
                "name": "create_referral",
                "arguments": {
                    "patient_identifier": "Jennifer Brown",
                    "referring_doctor_identifier": "Dr. Jennifer Martinez",
                    "referred_to_doctor_identifier": "Dr. Robert Chen",
                    "referred_to_department": "Orthopedics",
                    "priority": "routine"
                },
            },
        ],
    },
    {
        "id": "entry_13",
        "instructions": "You are Dr. William Davis in Psychiatry. You are managing several patients and need to review your referral workflow. First, get all your incoming referrals to see which patients need psychiatric evaluation. Review the patient information for Maria Rodriguez who was referred by Internal Medicine. Check her current medications and lab results to assess for any medical factors affecting mental health. Update her referral status to 'scheduled' since you've booked her appointment. Then create a new referral for her to Dr. Amanda Taylor in Internal Medicine for medical clearance before starting antidepressant therapy.",
        "actions": [
            {
                "name": "get_doctor_referrals",
                "arguments": {
                    "doctor_identifier": "Dr. William Davis",
                    "referral_type": "incoming"
                },
            },
            {
                "name": "get_patient_info",
                "arguments": {
                    "patient_identifier": "Maria Rodriguez"
                },
            },
            {
                "name": "get_patient_medications",
                "arguments": {
                    "patient_identifier": "Maria Rodriguez"
                },
            },
            {
                "name": "get_lab_results",
                "arguments": {
                    "patient_identifier": "Maria Rodriguez"
                },
            },
            {
                "name": "update_referral_status",
                "arguments": {
                    "patient_identifier": "Maria Rodriguez",
                    "referred_to_doctor_identifier": "Dr. William Davis",
                    "new_status": "scheduled"
                },
            },
            {
                "name": "create_referral",
                "arguments": {
                    "patient_identifier": "Maria Rodriguez",
                    "referring_doctor_identifier": "Dr. William Davis",
                    "referred_to_doctor_identifier": "Dr. Amanda Taylor",
                    "referred_to_department": "Internal Medicine",
                    "priority": "routine"
                },
            },
        ],
    },
    {
        "id": "entry_14",
        "instructions": "You are a care coordinator working with Dr. Maria Rodriguez in Obstetrics. Patient Lisa Garcia is 32 weeks pregnant and has developed complications requiring multidisciplinary care. First, get her patient information and current medications. Check her existing referrals to understand current care plan. Review her lab results for any concerning findings. Create an urgent referral to Dr. Sarah Johnson in Cardiology for pregnancy-related hypertension management. Then create another referral to Dr. David Brown in Neurology for evaluation of severe headaches that started recently. Finally, schedule a follow-up appointment with Dr. Rodriguez to coordinate care for January 29, 2024 at 10:00 AM.",
        "actions": [
            {
                "name": "get_patient_info",
                "arguments": {
                    "patient_identifier": "Lisa Garcia"
                },
            },
            {
                "name": "get_patient_medications",
                "arguments": {
                    "patient_identifier": "Lisa Garcia"
                },
            },
            {
                "name": "get_patient_referrals",
                "arguments": {
                    "patient_identifier": "Lisa Garcia"
                },
            },
            {
                "name": "get_lab_results",
                "arguments": {
                    "patient_identifier": "Lisa Garcia"
                },
            },
            {
                "name": "create_referral",
                "arguments": {
                    "patient_identifier": "Lisa Garcia",
                    "referring_doctor_identifier": "Dr. Maria Rodriguez",
                    "referred_to_doctor_identifier": "Dr. Sarah Johnson",
                    "referred_to_department": "Cardiology",
                    "priority": "urgent"
                },
            },
            {
                "name": "create_referral",
                "arguments": {
                    "patient_identifier": "Lisa Garcia",
                    "referring_doctor_identifier": "Dr. Maria Rodriguez",
                    "referred_to_doctor_identifier": "Dr. David Brown",
                    "referred_to_department": "Neurology",
                    "priority": "urgent"
                },
            },
            {
                "name": "schedule_appointment",
                "arguments": {
                    "patient_identifier": "Lisa Garcia",
                    "doctor_identifier": "Dr. Maria Rodriguez",
                    "appointment_time": "10:00 AM",
                    "appointment_date": "2024-01-29",
                    "department": "Obstetrics"
                },
            },
        ],
    },
    {
        "id": "entry_15",
        "instructions": "You are Dr. Robert Chen in Orthopedics conducting your end-of-week referral review. Check all your outgoing referrals to see their current status and follow up appropriately. Get detailed information about the referral you made for patient Jennifer Brown to Dermatology. If that referral is completed, review her patient information and current medications, else if it is pending then ask it to be marked as 'completed', then schedule a follow-up orthopedic appointment to continue her original treatment plan for February 1, 2024 at 3:00 PM. Also review any incoming referrals to your department and update the status of any you've evaluated.",
        "actions": [
            {
                "name": "get_doctor_referrals",
                "arguments": {
                    "doctor_identifier": "Dr. Robert Chen",
                    "referral_type": "outgoing"
                },
            },
            {
                "name": "get_patient_referrals",
                "arguments": {
                    "patient_identifier": "Jennifer Brown"
                },
            },
            {
                "name": "get_patient_info",
                "arguments": {
                    "patient_identifier": "Jennifer Brown"
                },
            },
            {
                "name": "get_patient_medications",
                "arguments": {
                    "patient_identifier": "Jennifer Brown"
                },
            },
            {
                "name": "schedule_appointment",
                "arguments": {
                    "patient_identifier": "Jennifer Brown",
                    "doctor_identifier": "Dr. Robert Chen",
                    "appointment_time": "3:00 PM",
                    "appointment_date": "2024-02-01",
                    "department": "Orthopedics"
                },
            },
            {
                "name": "get_doctor_referrals",
                "arguments": {
                    "doctor_identifier": "Dr. Robert Chen",
                    "referral_type": "incoming"
                },
            },
        ],
    },
    
    # Easy entries (1-2 function calls, clear instructions)
    {
        "id": "entry_16",
        "instructions": "You are a receptionist. Please retrieve the basic information for patient Emily Davis who just arrived for her appointment.",
        "actions": [
            {
                "name": "get_patient_info",
                "arguments": {
                    "patient_identifier": "Emily Davis"
                },
            },
        ],
    },
    {
        "id": "entry_17",
        "instructions": "You are working at the information desk. A patient wants to know about Dr. Michael Chen's specialty and department. Please provide this information.",
        "actions": [
            {
                "name": "get_doctor_info",
                "arguments": {
                    "doctor_identifier": "Dr. Michael Chen"
                },
            },
        ],
    },
    {
        "id": "entry_18",
        "instructions": "You are a lab technician. Patient David Wilson is here to discuss his lab results. Please retrieve his recent lab results for review.",
        "actions": [
            {
                "name": "get_lab_results",
                "arguments": {
                    "patient_identifier": "David Wilson"
                },
            },
        ],
    },
    {
        "id": "entry_19",
        "instructions": "You are a pharmacy assistant. Patient Sarah Miller needs her current medication list. Please retrieve her medication information.",
        "actions": [
            {
                "name": "get_patient_medications",
                "arguments": {
                    "patient_identifier": "Sarah Miller"
                },
            },
        ],
    },
    {
        "id": "entry_20",
        "instructions": "You are a scheduling coordinator. Please book an appointment for patient James Anderson with Dr. Lisa Wilson in Pediatrics for January 30, 2024 at 3:00 PM.",
        "actions": [
            {
                "name": "schedule_appointment",
                "arguments": {
                    "patient_identifier": "James Anderson",
                    "doctor_identifier": "Dr. Lisa Wilson",
                    "appointment_time": "3:00 PM",
                    "appointment_date": "2024-01-30",
                    "department": "Pediatrics"
                },
            },
        ],
    },
    {
        "id": "entry_21",
        "instructions": "You are at the front desk. Patient Michael Davis called to cancel his appointment with Dr. Robert Chen on January 28, 2024 at 1:00 PM. Please process this cancellation.",
        "actions": [
            {
                "name": "cancel_appointment",
                "arguments": {
                    "patient_identifier": "Michael Davis",
                    "doctor_identifier": "Dr. Robert Chen",
                    "appointment_date": "2024-01-28",
                    "appointment_time": "1:00 PM"
                },
            },
        ],
    },
    {
        "id": "entry_22",
        "instructions": "You are a patient services representative. Patient Lisa Garcia needs to update her emergency contact to her husband Pedro Garcia at 555-1022. Please make this update.",
        "actions": [
            {
                "name": "update_emergency_contact",
                "arguments": {
                    "patient_identifier": "Lisa Garcia",
                    "contact_name": "Pedro Garcia",
                    "contact_phone": "555-1022"
                },
            },
        ],
    },
    {
        "id": "entry_23",
        "instructions": "You are a referral coordinator. Patient Jennifer Brown wants to check all her referrals. Please retrieve her referral history.",
        "actions": [
            {
                "name": "get_patient_referrals",
                "arguments": {
                    "patient_identifier": "Jennifer Brown"
                },
            },
        ],
    },
    {
        "id": "entry_24",
        "instructions": "You are helping Dr. David Brown check his incoming referrals. Please retrieve all incoming referrals for Dr. Brown.",
        "actions": [
            {
                "name": "get_doctor_referrals",
                "arguments": {
                    "doctor_identifier": "Dr. David Brown",
                    "referral_type": "incoming"
                },
            },
        ],
    },
    {
        "id": "entry_25",
        "instructions": "You are a scheduling assistant. Please schedule an appointment for patient William Martinez with Dr. Jennifer Martinez in Dermatology for February 1, 2024 at 9:00 AM.",
        "actions": [
            {
                "name": "schedule_appointment",
                "arguments": {
                    "patient_identifier": "William Martinez",
                    "doctor_identifier": "Dr. Jennifer Martinez",
                    "appointment_time": "9:00 AM",
                    "appointment_date": "2024-02-01",
                    "department": "Dermatology"
                },
            },
        ],
    },
    
    # Medium entries (2-3 function calls, moderate complexity)
    {
        "id": "entry_26",
        "instructions": "You are a nurse preparing for patient Alice Johnson's appointment. Please get her basic information and current medications to prepare for the consultation.",
        "actions": [
            {
                "name": "get_patient_info",
                "arguments": {
                    "patient_identifier": "Alice Johnson"
                },
            },
            {
                "name": "get_patient_medications",
                "arguments": {
                    "patient_identifier": "Alice Johnson"
                },
            },
        ],
    },
    {
        "id": "entry_27",
        "instructions": "You are a medical assistant. Patient Robert Wilson wants to schedule an appointment with Dr. Amanda Taylor in Internal Medicine for February 5, 2024 at 10:00 AM. First, confirm Dr. Taylor's department and specialty, then book the appointment.",
        "actions": [
            {
                "name": "get_doctor_info",
                "arguments": {
                    "doctor_identifier": "Dr. Amanda Taylor"
                },
            },
            {
                "name": "schedule_appointment",
                "arguments": {
                    "patient_identifier": "Robert Wilson",
                    "doctor_identifier": "Dr. Amanda Taylor",
                    "appointment_time": "10:00 AM",
                    "appointment_date": "2024-02-05",
                    "department": "Internal Medicine"
                },
            },
        ],
    },
    {
        "id": "entry_28",
        "instructions": "You are helping patient Emily Taylor who needs a comprehensive medication and lab review. Please retrieve both her current medications and recent lab results.",
        "actions": [
            {
                "name": "get_patient_medications",
                "arguments": {
                    "patient_identifier": "Emily Taylor"
                },
            },
            {
                "name": "get_lab_results",
                "arguments": {
                    "patient_identifier": "Emily Taylor"
                },
            },
        ],
    },
    {
        "id": "entry_29",
        "instructions": "You are a receptionist. Patient John Smith needs to cancel his appointment with Dr. Sarah Johnson on February 10, 2024 at 2:00 PM and immediately reschedule for February 15, 2024 at the same time.",
        "actions": [
            {
                "name": "cancel_appointment",
                "arguments": {
                    "patient_identifier": "John Smith",
                    "doctor_identifier": "Dr. Sarah Johnson",
                    "appointment_date": "2024-02-10",
                    "appointment_time": "2:00 PM"
                },
            },
            {
                "name": "schedule_appointment",
                "arguments": {
                    "patient_identifier": "John Smith",
                    "doctor_identifier": "Dr. Sarah Johnson",
                    "appointment_time": "2:00 PM",
                    "appointment_date": "2024-02-15",
                    "department": "Cardiology"
                },
            },
        ],
    },
    {
        "id": "entry_30",
        "instructions": "You are updating patient records. For patient Maria Rodriguez, first verify her current information, then update her emergency contact to her son Carlos Rodriguez at 555-1006.",
        "actions": [
            {
                "name": "get_patient_info",
                "arguments": {
                    "patient_identifier": "Maria Rodriguez"
                },
            },
            {
                "name": "update_emergency_contact",
                "arguments": {
                    "patient_identifier": "Maria Rodriguez",
                    "contact_name": "Carlos Rodriguez",
                    "contact_phone": "555-1006"
                },
            },
        ],
    },
    {
        "id": "entry_31",
        "instructions": "You are processing a referral. First check Dr. William Davis's specialty in Psychiatry, then create a routine referral from Dr. John Adams to Dr. Davis for patient Sarah Miller.",
        "actions": [
            {
                "name": "get_doctor_info",
                "arguments": {
                    "doctor_identifier": "Dr. William Davis"
                },
            },
            {
                "name": "create_referral",
                "arguments": {
                    "patient_identifier": "Sarah Miller",
                    "referring_doctor_identifier": "Dr. John Adams",
                    "referred_to_doctor_identifier": "Dr. William Davis",
                    "referred_to_department": "Psychiatry",
                    "priority": "routine"
                },
            },
        ],
    },
    {
        "id": "entry_32",
        "instructions": "You are a referral manager. Check all referrals for patient Emily Davis, then update her referral to Dr. Amanda Taylor to 'scheduled' status.",
        "actions": [
            {
                "name": "get_patient_referrals",
                "arguments": {
                    "patient_identifier": "Emily Davis"
                },
            },
            {
                "name": "update_referral_status",
                "arguments": {
                    "patient_identifier": "Emily Davis",
                    "referred_to_doctor_identifier": "Dr. Amanda Taylor",
                    "new_status": "scheduled"
                },
            },
        ],
    },
    {
        "id": "entry_33",
        "instructions": "You are preparing for a patient visit. Get both the patient information and lab results for Michael Davis to prepare for his orthopedic consultation.",
        "actions": [
            {
                "name": "get_patient_info",
                "arguments": {
                    "patient_identifier": "Michael Davis"
                },
            },
            {
                "name": "get_lab_results",
                "arguments": {
                    "patient_identifier": "Michael Davis"
                },
            },
        ],
    },
    {
        "id": "entry_34",
        "instructions": "You are coordinating care for patient Lisa Garcia. Create an urgent referral from Dr. Maria Rodriguez in Obstetrics to Dr. Michael Chen in Cardiology, then schedule an appointment with Dr. Chen for February 20, 2024 at 11:00 AM.",
        "actions": [
            {
                "name": "create_referral",
                "arguments": {
                    "patient_identifier": "Lisa Garcia",
                    "referring_doctor_identifier": "Dr. Maria Rodriguez",
                    "referred_to_doctor_identifier": "Dr. Michael Chen",
                    "referred_to_department": "Cardiology",
                    "priority": "urgent"
                },
            },
            {
                "name": "schedule_appointment",
                "arguments": {
                    "patient_identifier": "Lisa Garcia",
                    "doctor_identifier": "Dr. Michael Chen",
                    "appointment_time": "11:00 AM",
                    "appointment_date": "2024-02-20",
                    "department": "Cardiology"
                },
            },
        ],
    },
    {
        "id": "entry_35",
        "instructions": "You are helping Dr. Jennifer Martinez review her referral workload. First check all her incoming referrals, then get information about one of her referring doctors, Dr. Robert Chen.",
        "actions": [
            {
                "name": "get_doctor_referrals",
                "arguments": {
                    "doctor_identifier": "Dr. Jennifer Martinez",
                    "referral_type": "incoming"
                },
            },
            {
                "name": "get_doctor_info",
                "arguments": {
                    "doctor_identifier": "Dr. Robert Chen"
                },
            },
        ],
    },
    
    # Hard entries (4+ function calls, complex workflows)
    {
        "id": "entry_36",
        "instructions": "You are admitting a new emergency patient, James Anderson. First get his patient information, then check his medications and lab results. Create an urgent referral from Dr. John Adams in Emergency to Dr. Sarah Johnson in Cardiology. Schedule an immediate consultation for January 24, 2024 at 4:00 PM. Finally, update his emergency contact to Amy Anderson at 555-1020.",
        "actions": [
            {
                "name": "get_patient_info",
                "arguments": {
                    "patient_identifier": "James Anderson"
                },
            },
            {
                "name": "get_patient_medications",
                "arguments": {
                    "patient_identifier": "James Anderson"
                },
            },
            {
                "name": "get_lab_results",
                "arguments": {
                    "patient_identifier": "James Anderson"
                },
            },
            {
                "name": "create_referral",
                "arguments": {
                    "patient_identifier": "James Anderson",
                    "referring_doctor_identifier": "Dr. John Adams",
                    "referred_to_doctor_identifier": "Dr. Sarah Johnson",
                    "referred_to_department": "Cardiology",
                    "priority": "urgent"
                },
            },
            {
                "name": "schedule_appointment",
                "arguments": {
                    "patient_identifier": "James Anderson",
                    "doctor_identifier": "Dr. Sarah Johnson",
                    "appointment_time": "4:00 PM",
                    "appointment_date": "2024-01-24",
                    "department": "Cardiology"
                },
            },
            {
                "name": "update_emergency_contact",
                "arguments": {
                    "patient_identifier": "James Anderson",
                    "contact_name": "Amy Anderson",
                    "contact_phone": "555-1020"
                },
            },
        ],
    },
    {
        "id": "entry_37",
        "instructions": "You are coordinating a multi-specialist consultation for patient William Martinez. Get his complete information including demographics, medications, and lab results. Check the information of Dr. David Brown's availability in Neurology and Dr. Amanda Taylor's in Internal Medicine. Create referrals from Dr. Robert Chen to both specialists with urgent priority. Schedule appointments with both doctors for February 1, 2024 at 10:00 AM and February 2, 2024 at 2:00 PM respectively.",
        "actions": [
            {
                "name": "get_patient_info",
                "arguments": {
                    "patient_identifier": "William Martinez"
                },
            },
            {
                "name": "get_patient_medications",
                "arguments": {
                    "patient_identifier": "William Martinez"
                },
            },
            {
                "name": "get_lab_results",
                "arguments": {
                    "patient_identifier": "William Martinez"
                },
            },
            {
                "name": "get_doctor_info",
                "arguments": {
                    "doctor_identifier": "Dr. David Brown"
                },
            },
            {
                "name": "get_doctor_info",
                "arguments": {
                    "doctor_identifier": "Dr. Amanda Taylor"
                },
            },
            {
                "name": "create_referral",
                "arguments": {
                    "patient_identifier": "William Martinez",
                    "referring_doctor_identifier": "Dr. Robert Chen",
                    "referred_to_doctor_identifier": "Dr. David Brown",
                    "referred_to_department": "Neurology",
                    "priority": "urgent"
                },
            },
            {
                "name": "create_referral",
                "arguments": {
                    "patient_identifier": "William Martinez",
                    "referring_doctor_identifier": "Dr. Robert Chen",
                    "referred_to_doctor_identifier": "Dr. Amanda Taylor",
                    "referred_to_department": "Internal Medicine",
                    "priority": "urgent"
                },
            },
            {
                "name": "schedule_appointment",
                "arguments": {
                    "patient_identifier": "William Martinez",
                    "doctor_identifier": "Dr. David Brown",
                    "appointment_time": "10:00 AM",
                    "appointment_date": "2024-02-01",
                    "department": "Neurology"
                },
            },
            {
                "name": "schedule_appointment",
                "arguments": {
                    "patient_identifier": "William Martinez",
                    "doctor_identifier": "Dr. Amanda Taylor",
                    "appointment_time": "2:00 PM",
                    "appointment_date": "2024-02-02",
                    "department": "Internal Medicine"
                },
            },
        ],
    },
    {
        "id": "entry_38",
        "instructions": "You are managing an emergency transfer for patient Emily Taylor from Emergency to Psychiatry. Get her complete medical profile including info, medications, and labs. Check her existing referrals. Create an urgent referral from Dr. John Adams to Dr. William Davis. Update the referral status to scheduled. Book an immediate appointment for January 24, 2024 at 5:00 PM. Update her emergency contact to Mark Taylor at 555-4444.",
        "actions": [
            {
                "name": "get_patient_info",
                "arguments": {
                    "patient_identifier": "Emily Taylor"
                },
            },
            {
                "name": "get_patient_medications",
                "arguments": {
                    "patient_identifier": "Emily Taylor"
                },
            },
            {
                "name": "get_lab_results",
                "arguments": {
                    "patient_identifier": "Emily Taylor"
                },
            },
            {
                "name": "get_patient_referrals",
                "arguments": {
                    "patient_identifier": "Emily Taylor"
                },
            },
            {
                "name": "create_referral",
                "arguments": {
                    "patient_identifier": "Emily Taylor",
                    "referring_doctor_identifier": "Dr. John Adams",
                    "referred_to_doctor_identifier": "Dr. William Davis",
                    "referred_to_department": "Psychiatry",
                    "priority": "urgent"
                },
            },
            {
                "name": "update_referral_status",
                "arguments": {
                    "patient_identifier": "Emily Taylor",
                    "referred_to_doctor_identifier": "Dr. William Davis",
                    "new_status": "scheduled"
                },
            },
            {
                "name": "schedule_appointment",
                "arguments": {
                    "patient_identifier": "Emily Taylor",
                    "doctor_identifier": "Dr. William Davis",
                    "appointment_time": "5:00 PM",
                    "appointment_date": "2024-01-24",
                    "department": "Psychiatry"
                },
            },
            {
                "name": "update_emergency_contact",
                "arguments": {
                    "patient_identifier": "Emily Taylor",
                    "contact_name": "Mark Taylor",
                    "contact_phone": "555-4444"
                },
            },
        ],
    },
    {
        "id": "entry_39",
        "instructions": "You are managing a complex referral chain for patient Alice Johnson. Check all her existing referrals first. She needs evaluation by multiple specialists: create referrals from Dr. Amanda Taylor to Dr. Sarah Johnson (Cardiology), Dr. David Brown (Neurology), and Dr. William Davis (Psychiatry), all with urgent priority. Update her first referral to 'completed' status. Schedule appointments with all three specialists on February 5, 2024, at 9:00 AM, February 6, 2024 at 11:00 AM, and February 7, 2024 at 2:00 PM respectively.",
        "actions": [
            {
                "name": "get_patient_referrals",
                "arguments": {
                    "patient_identifier": "Alice Johnson"
                },
            },
            {
                "name": "create_referral",
                "arguments": {
                    "patient_identifier": "Alice Johnson",
                    "referring_doctor_identifier": "Dr. Amanda Taylor",
                    "referred_to_doctor_identifier": "Dr. Sarah Johnson",
                    "referred_to_department": "Cardiology",
                    "priority": "urgent"
                },
            },
            {
                "name": "create_referral",
                "arguments": {
                    "patient_identifier": "Alice Johnson",
                    "referring_doctor_identifier": "Dr. Amanda Taylor",
                    "referred_to_doctor_identifier": "Dr. David Brown",
                    "referred_to_department": "Neurology",
                    "priority": "urgent"
                },
            },
            {
                "name": "create_referral",
                "arguments": {
                    "patient_identifier": "Alice Johnson",
                    "referring_doctor_identifier": "Dr. Amanda Taylor",
                    "referred_to_doctor_identifier": "Dr. William Davis",
                    "referred_to_department": "Psychiatry",
                    "priority": "urgent"
                },
            },
            {
                "name": "update_referral_status",
                "arguments": {
                    "patient_identifier": "Alice Johnson",
                    "referred_to_doctor_identifier": "Dr. Sarah Johnson",
                    "new_status": "completed"
                },
            },
            {
                "name": "schedule_appointment",
                "arguments": {
                    "patient_identifier": "Alice Johnson",
                    "doctor_identifier": "Dr. Sarah Johnson",
                    "appointment_time": "9:00 AM",
                    "appointment_date": "2024-02-05",
                    "department": "Cardiology"
                },
            },
            {
                "name": "schedule_appointment",
                "arguments": {
                    "patient_identifier": "Alice Johnson",
                    "doctor_identifier": "Dr. David Brown",
                    "appointment_time": "11:00 AM",
                    "appointment_date": "2024-02-06",
                    "department": "Neurology"
                },
            },
            {
                "name": "schedule_appointment",
                "arguments": {
                    "patient_identifier": "Alice Johnson",
                    "doctor_identifier": "Dr. William Davis",
                    "appointment_time": "2:00 PM",
                    "appointment_date": "2024-02-07",
                    "department": "Psychiatry"
                },
            },
        ],
    },
    {
        "id": "entry_40",
        "instructions": "You are handling a comprehensive discharge for patient Robert Wilson. First, get his complete medical profile (info, medications, lab results). Check all his referrals and update any pending ones to 'cancelled'. Cancel his follow-up appointment with Dr. Amanda Taylor on February 5, 2024 at 10:00 AM. Create a new referral to Dr. Lisa Wilson in Pediatrics for home care coordination. Update his emergency contact to Jane Wilson at 555-1016.",
        "actions": [
            {
                "name": "get_patient_info",
                "arguments": {
                    "patient_identifier": "Robert Wilson"
                },
            },
            {
                "name": "get_patient_medications",
                "arguments": {
                    "patient_identifier": "Robert Wilson"
                },
            },
            {
                "name": "get_lab_results",
                "arguments": {
                    "patient_identifier": "Robert Wilson"
                },
            },
            {
                "name": "get_patient_referrals",
                "arguments": {
                    "patient_identifier": "Robert Wilson"
                },
            },
            {
                "name": "cancel_appointment",
                "arguments": {
                    "patient_identifier": "Robert Wilson",
                    "doctor_identifier": "Dr. Amanda Taylor",
                    "appointment_date": "2024-02-05",
                    "appointment_time": "10:00 AM"
                },
            },
            {
                "name": "create_referral",
                "arguments": {
                    "patient_identifier": "Robert Wilson",
                    "referring_doctor_identifier": "Dr. Amanda Taylor",
                    "referred_to_doctor_identifier": "Dr. Lisa Wilson",
                    "referred_to_department": "Pediatrics",
                    "priority": "routine"
                },
            },
            {
                "name": "update_emergency_contact",
                "arguments": {
                    "patient_identifier": "Robert Wilson",
                    "contact_name": "Jane Wilson",
                    "contact_phone": "555-1016"
                },
            },
        ],
    },
    
    # Additional easy entries to reach 50
    {
        "id": "entry_41",
        "instructions": "You are at the information desk. Please check what department Dr. John Adams works in.",
        "actions": [
            {
                "name": "get_doctor_info",
                "arguments": {
                    "doctor_identifier": "Dr. John Adams"
                },
            },
        ],
    },
    {
        "id": "entry_42",
        "instructions": "A patient is asking about their upcoming appointments. Please check all referrals for patient David Wilson.",
        "actions": [
            {
                "name": "get_patient_referrals",
                "arguments": {
                    "patient_identifier": "David Wilson"
                },
            },
        ],
    },
    {
        "id": "entry_43",
        "instructions": "You need to verify patient contact information. Please retrieve the basic information for patient Emily Davis.",
        "actions": [
            {
                "name": "get_patient_info",
                "arguments": {
                    "patient_identifier": "Emily Davis"
                },
            },
        ],
    },
    {
        "id": "entry_44",
        "instructions": "A doctor wants to review their outgoing referrals. Please get all outgoing referrals for Dr. Robert Chen.",
        "actions": [
            {
                "name": "get_doctor_referrals",
                "arguments": {
                    "doctor_identifier": "Dr. Robert Chen",
                    "referral_type": "outgoing"
                },
            },
        ],
    },
    {
        "id": "entry_45",
        "instructions": "You are helping at the pharmacy. Please retrieve the current medication list for patient Jennifer Brown.",
        "actions": [
            {
                "name": "get_patient_medications",
                "arguments": {
                    "patient_identifier": "Jennifer Brown"
                },
            },
        ],
    },
    
    # Additional medium entries
    {
        "id": "entry_46",
        "instructions": "You are preparing for patient Sarah Miller's neurology consultation. Get her patient information and check if she has any existing referrals to neurology.",
        "actions": [
            {
                "name": "get_patient_info",
                "arguments": {
                    "patient_identifier": "Sarah Miller"
                },
            },
            {
                "name": "get_patient_referrals",
                "arguments": {
                    "patient_identifier": "Sarah Miller"
                },
            },
        ],
    },
    {
        "id": "entry_47",
        "instructions": "Patient Maria Rodriguez needs to see a specialist. First verify Dr. Jennifer Martinez is in Dermatology, then create a routine referral from Dr. Amanda Taylor to Dr. Martinez.",
        "actions": [
            {
                "name": "get_doctor_info",
                "arguments": {
                    "doctor_identifier": "Dr. Jennifer Martinez"
                },
            },
            {
                "name": "create_referral",
                "arguments": {
                    "patient_identifier": "Maria Rodriguez",
                    "referring_doctor_identifier": "Dr. Amanda Taylor",
                    "referred_to_doctor_identifier": "Dr. Jennifer Martinez",
                    "referred_to_department": "Dermatology",
                    "priority": "routine"
                },
            },
        ],
    },
    {
        "id": "entry_48",
        "instructions": "You are doing a pre-surgery check for patient Michael Davis. Get his current medications and recent lab results to ensure he's ready for surgery.",
        "actions": [
            {
                "name": "get_patient_medications",
                "arguments": {
                    "patient_identifier": "Michael Davis"
                },
            },
            {
                "name": "get_lab_results",
                "arguments": {
                    "patient_identifier": "Michael Davis"
                },
            },
        ],
    },
    {
        "id": "entry_49",
        "instructions": "Patient John Smith's referral to cardiology has been completed. Update his referral status to Dr. Sarah Johnson to 'completed', then schedule a follow-up appointment for March 1, 2024 at 10:00 AM.",
        "actions": [
            {
                "name": "update_referral_status",
                "arguments": {
                    "patient_identifier": "John Smith",
                    "referred_to_doctor_identifier": "Dr. Sarah Johnson",
                    "new_status": "completed"
                },
            },
            {
                "name": "schedule_appointment",
                "arguments": {
                    "patient_identifier": "John Smith",
                    "doctor_identifier": "Dr. Sarah Johnson",
                    "appointment_time": "10:00 AM",
                    "appointment_date": "2024-03-01",
                    "department": "Cardiology"
                },
            },
        ],
    },
    {
        "id": "entry_50",
        "instructions": "You are verifying patient Emily Taylor's information before her psychiatric appointment. Get her basic information and update her emergency contact to her mother Susan Taylor at 555-9999.",
        "actions": [
            {
                "name": "get_patient_info",
                "arguments": {
                    "patient_identifier": "Emily Taylor"
                },
            },
            {
                "name": "update_emergency_contact",
                "arguments": {
                    "patient_identifier": "Emily Taylor",
                    "contact_name": "Susan Taylor",
                    "contact_phone": "555-9999"
                },
            },
        ],
    },

    # Complex entries with obfuscated instructions
    {
        "id": "entry_51",
        "instructions": "The pharmacy safety committee has flagged a complex case involving polypharmacy concerns. This patient was referred from internal medicine to neurology for specialist evaluation. The referring physician from internal medicine has multiple outgoing referrals - identify which patient was sent to neurology, then conduct a comprehensive medication reconciliation and review their recent diagnostic imaging. The neurological consultation phase has concluded and requires workflow closure.",
        "actions": [
            {
                "name": "get_doctor_referrals",
                "arguments": {
                    "doctor_identifier": "Dr. Amanda Taylor",
                    "referral_type": "outgoing"
                },
            },
            {
                "name": "get_patient_medications",
                "arguments": {
                    "patient_identifier": "Sarah Miller"
                },
            },
            {
                "name": "get_lab_results",
                "arguments": {
                    "patient_identifier": "Sarah Miller"
                },
            },
            {
                "name": "update_referral_status",
                "arguments": {
                    "patient_identifier": "Sarah Miller",
                    "referred_to_doctor_identifier": "Dr. David Brown",
                    "new_status": "completed"
                },
            },
        ],
    },
    {
        "id": "entry_52",
        "instructions": "Emily Davis recently got married and needs her records updated. Her emergency contact should be changed to her new husband Mark Davis at 555-2222. Additionally, she has some lab results that need review and follow-up care scheduled with her referring physician (from her records) based on those results on 12th Feb 2024 at 2pm.",
        "actions": [
            {
                "name": "update_emergency_contact",
                "arguments": {
                    "patient_identifier": "Emily Davis",
                    "contact_name": "Mark Davis",
                    "contact_phone": "555-2222"
                },
            },
            {
                "name": "get_lab_results",
                "arguments": {
                    "patient_identifier": "Emily Davis"
                },
            },
            {
                "name": "get_patient_referrals",
                "arguments": {
                    "patient_identifier": "Emily Davis"
                },
            },
            {
                "name": "schedule_appointment",
                "arguments": {
                    "patient_identifier": "Emily Davis",
                    "doctor_identifier": "Dr. Sarah Johnson",
                    "appointment_date": "2024-02-12",
                    "appointment_time": "2:00 PM",
                    "department": "Cardiology"
                },
            },
        ],
    },
    {
        "id": "entry_53",
        "instructions": "Jennifer Brown is a complex case requiring coordination between multiple specialists. Her current referral ( from the existing records) needs to be updated to show it's completed, and based on her existing medication profile, she may need an additional referral to endocrinology to Dr. Michael Johnson with routine urgency with scheduled status.",# Verify her current status and arrange appropriate follow-up.",
        "actions": [
            {
                "name": "get_patient_referrals",
                "arguments": {
                    "patient_identifier": "Jennifer Brown"
                },
            },
            {
                "name": "get_patient_medications", 
                "arguments": {
                    "patient_identifier": "Jennifer Brown"
                },
            },
            {
                "name": "update_referral_status",
                "arguments": {
                    "patient_identifier": "Jennifer Brown",
                    "referred_to_doctor_identifier": "Dr. Jennifer Martinez",
                    "new_status": "completed"
                },
            },
            {
                "name": "create_referral",
                "arguments": {
                    "patient_identifier": "Jennifer Brown",
                    "referring_doctor_identifier": "Dr. Robert Chen",
                    "referred_to_doctor_identifier": "Dr. Michael Johnson",
                    "priority": "routine",
                },
            },
        ],
    },
    {
        "id": "entry_54",
        "instructions": "Michael Davis has been having scheduling conflicts and needs his appointment rescheduled. First check his current information (from the records) and any lab results he might have. Then cancel his existing appointment if any and, if not then schedule a new one with Dr. Sarah Johnson for better coordination of his care on 14th Feb 2024 at 11am.",
        "actions": [
            {
                "name": "get_patient_info",
                "arguments": {
                    "patient_identifier": "Michael Davis"
                },
            },
            {
                "name": "get_lab_results",
                "arguments": {
                    "patient_identifier": "Michael Davis"
                },
            },
            {
                "name": "get_appointment",
                "arguments": {
                    "patient_identifier": "Michael Davis"
                },
            },
            {
                "name": "schedule_appointment",
                "arguments": {
                    "patient_identifier": "Michael Davis",
                    "doctor_identifier": "Dr. Sarah Johnson",
                    "appointment_date": "2024-02-14",
                    "appointment_time": "11:00 AM",
                    "department": "Cardiology",
                },
            },
        ],
    },
    {
        "id": "entry_55",
        "instructions": "You're managing Dr. Jennifer Martinez's referral workflow. She has several patients referred to her, and you need to verify if William Martinez (no relation) has his appointment scheduled with her. Check what referrals Dr. Martinez has received and based on the information, ensure William gets proper scheduling with her on February 15th at 10am in the Psychiatry department.",
        "actions": [
            {
                "name": "get_doctor_referrals",
                "arguments": {
                    "doctor_identifier": "Dr. Jennifer Martinez",
                    "referral_type": "incoming"
                },
            },
            {
                "name": "get_patient_referrals",
                "arguments": {
                    "patient_identifier": "William Martinez"
                },
            },
            {
                "name": "schedule_appointment",
                "arguments": {
                    "patient_identifier": "William Martinez",
                    "doctor_identifier": "Dr. Jennifer Martinez",
                    "appointment_date": "2024-02-15",
                    "appointment_time": "10:00 AM",
                    "department": "Psychiatry"
                },
            },
        ],
    },
    {
        "id": "entry_56",
        "instructions": "Alice Johnson needs comprehensive care coordination. Her emergency contact information needs verification and potential updating to her sister Linda Johnson at 555-1234. Additionally, check if she has any pending lab work and whether her referral to neurology has been properly processed. If the referral exists and is still pending, move it to scheduled status. If not then create a new referral to neurology from Dr. William Davis to Dr. David Brown with routine urgency and scheduled as status.",
        "actions": [
            {
                "name": "get_patient_info",
                "arguments": {
                    "patient_identifier": "Alice Johnson"
                },
            },
            {
                "name": "update_emergency_contact",
                "arguments": {
                    "patient_identifier": "Alice Johnson",
                    "contact_name": "Linda Johnson",
                    "contact_phone": "555-1234"
                },
            },
            {
                "name": "get_lab_results",
                "arguments": {
                    "patient_identifier": "Alice Johnson"
                },
            },
            {
                "name": "get_patient_referrals",
                "arguments": {
                    "patient_identifier": "Alice Johnson"
                },
            },
            {
                "name": "create_referral",
                "arguments": {
                    "patient_identifier": "Alice Johnson",
                    "referring_doctor_identifier": "Dr. William Davis",
                    "referred_to_doctor_identifier": "Dr. David Brown",
                    "priority": "routine",

                },
            },
        ],
    },
    {
        "id": "entry_57",
        "instructions": "As part of the medication reconciliation process, John Smith's care team needs a comprehensive review. Look into his current medication list and any recent lab work that might indicate necessary adjustments. His orthopedic surgeon Dr. Shaunak Joshi mentioned he might need a referral to pain management with Dr. Amanda Taylor, so create that referral with urgent priority if his medications contain Lisinopril.",
        "actions": [
            {
                "name": "get_patient_medications",
                "arguments": {
                    "patient_identifier": "John Smith"
                },
            },
            {
                "name": "get_lab_results",
                "arguments": {
                    "patient_identifier": "John Smith"
                },
            },
            {
                "name": "create_referral",
                "arguments": {
                    "patient_identifier": "John Smith",
                    "referring_doctor_identifier": "Dr. Shaunak Joshi",
                    "referred_to_doctor_identifier": "Dr. Amanda Taylor",
                    "priority": "urgent",
                },
            },
        ],
    },
    {
        "id": "entry_58",
        "instructions": "Maria Rodriguez has multiple specialists involved in her care. Review her existing referral patterns to understand her care network. Her cardiologist mentioned that her psychiatry referral should be marked as completed since she finished that consultation series. Also, verify if she has any scheduled appointments that might conflict with her upcoming travel plans which are on 17th Feb 2024.",
        "actions": [
            {
                "name": "get_patient_referrals",
                "arguments": {
                    "patient_identifier": "Maria Rodriguez"
                },
            },
            {
                "name": "update_referral_status",
                "arguments": {
                    "patient_identifier": "Maria Rodriguez",
                    "referred_to_doctor_identifier": "Dr. William Davis",
                    "new_status": "completed"
                },
            },
            {
                "name": "get_appointment",
                "arguments": {
                    "patient_identifier": "Maria Rodriguez"
                },
            },
        ],
    },
    {
        "id": "entry_59",
        "instructions": "Dr. Robert Chen has been managing several complex cardiac cases and wants to review his outgoing referral patterns. Check which patients he has referred to other specialists. For David Wilson specifically, he mentioned the patient needs follow-up lab work reviewed and potentially needs his existing appointment cancelled if the labs show improvement. The new scheduling would be determined after lab review.",
        "actions": [
            {
                "name": "get_doctor_referrals",
                "arguments": {
                    "doctor_identifier": "Dr. Robert Chen",
                    "referral_type": "outgoing"
                },
            },
            {
                "name": "get_lab_results",
                "arguments": {
                    "patient_identifier": "David Wilson"
                },
            },
            {
                "name": "get_appointment",
                "arguments": {
                    "patient_identifier": "David Wilson"
                },
            },
            {
                "name": "cancel_appointment",
                "arguments": {
                    "patient_identifier": "David Wilson",
                    "doctor_identifier": "Dr. Robert Chen",
                    "appointment_date": "2024-02-20",
                    "appointment_time": "3:00 PM"
                },
            },
        ],
    },
    {
        "id": "entry_60",
        "instructions": "Dr. Sarah Johnson needs to review her cardiac referral pipeline. The obstetric team has sent her a male patient with cardiovascular concerns, and she needs to assess the case. Check her current referral queue, then evaluate this patient's medication interactions and recent cardiac workup. The case has progressed beyond initial consultation, so update the workflow accordingly. His contact information also needs updating - his wife Amy Anderson at 555-2050 should be the primary contact now.",
        "actions": [
            {
                "name": "get_doctor_referrals",
                "arguments": {
                    "doctor_identifier": "Dr. Sarah Johnson",
                    "referral_type": "incoming"
                },
            },
            {
                "name": "get_patient_medications",
                "arguments": {
                    "patient_identifier": "James Anderson"
                },
            },
            {
                "name": "get_lab_results",
                "arguments": {
                    "patient_identifier": "James Anderson"
                },
            },
            {
                "name": "update_referral_status",
                "arguments": {
                    "patient_identifier": "James Anderson",
                    "referred_to_doctor_identifier": "Dr. Sarah Johnson",
                    "new_status": "scheduled"
                },
            },
            {
                "name": "update_emergency_contact",
                "arguments": {
                    "patient_identifier": "James Anderson",
                    "contact_name": "Amy Anderson",
                    "contact_phone": "555-2050"
                },
            },
        ],
    },
    {
        "id": "entry_61",
        "instructions": "Dr. Amanda Taylor is tracking her specialist referral outcomes. She has multiple patients out for consultation, and her psychiatric referral case needs closure - the patient has completed treatment. Check Amanda's referral portfolio, identify which patient was sent to psychiatry, then close that case appropriately. Review the patient's medication coordination needs and schedule her return visit on February 28th at 3pm for ongoing internal medicine management.",
        "actions": [
            {
                "name": "get_doctor_referrals",
                "arguments": {
                    "doctor_identifier": "Dr. Amanda Taylor",
                    "referral_type": "outgoing"
                },
            },
            {
                "name": "update_referral_status",
                "arguments": {
                    "patient_identifier": "Maria Rodriguez",
                    "referred_to_doctor_identifier": "Dr. William Davis",
                    "new_status": "completed"
                },
            },
            {
                "name": "get_patient_medications",
                "arguments": {
                    "patient_identifier": "Maria Rodriguez"
                },
            },
            {
                "name": "schedule_appointment",
                "arguments": {
                    "patient_identifier": "Maria Rodriguez",
                    "doctor_identifier": "Dr. Amanda Taylor",
                    "appointment_date": "2024-02-28",
                    "appointment_time": "3:00 PM",
                    "department": "Internal Medicine"
                },
            },
        ],
    },
    {
        "id": "entry_62",
        "instructions": "Dr. David Brown is coordinating with referring physicians about his neurology consultations. He has several active cases, and one patient from internal medicine has finished her consultation series. Check his incoming referral workload, identify which patient came from internal medicine, then update that case status. The patient may need medication review and appointment coordination - verify her current medications, scheduled visits, and contact information for proper care transition.",
        "actions": [
            {
                "name": "get_doctor_referrals",
                "arguments": {
                    "doctor_identifier": "Dr. David Brown",
                    "referral_type": "incoming"
                },
            },
            {
                "name": "update_referral_status",
                "arguments": {
                    "patient_identifier": "Sarah Miller",
                    "referred_to_doctor_identifier": "Dr. David Brown",
                    "new_status": "completed"
                },
            },
            {
                "name": "get_patient_medications",
                "arguments": {
                    "patient_identifier": "Sarah Miller"
                },
            },
            {
                "name": "get_appointment",
                "arguments": {
                    "patient_identifier": "Sarah Miller"
                },
            },
            {
                "name": "get_patient_info",
                "arguments": {
                    "patient_identifier": "Sarah Miller"
                },
            },
        ],
    },
    {
        "id": "entry_63",
        "instructions": "Dr. William Davis is concerned about medication interactions in his psychiatric patients. He needs to review his current referral caseload and create an urgent referral for one patient - Emily Taylor - to emergency medicine due to drug interaction concerns. Before making the referral, assess Emily's current psychiatric medications and liver function monitoring to document the clinical situation properly.",
        "actions": [
            {
                "name": "get_doctor_referrals",
                "arguments": {
                    "doctor_identifier": "Dr. William Davis",
                    "referral_type": "incoming"
                },
            },
            {
                "name": "get_patient_medications",
                "arguments": {
                    "patient_identifier": "Emily Taylor"
                },
            },
            {
                "name": "get_lab_results",
                "arguments": {
                    "patient_identifier": "Emily Taylor"
                },
            },
            {
                "name": "create_referral",
                "arguments": {
                    "patient_identifier": "Emily Taylor",
                    "referring_doctor_identifier": "Dr. William Davis",
                    "referred_to_doctor_identifier": "Dr. John Adams",
                    "referred_to_department": "Emergency",
                    "priority": "urgent"
                },
            },
        ],
    },
    {
        "id": "entry_64",
        "instructions": "Dr. Jennifer Martinez is reviewing her dermatology consultations for medication-related skin reactions. She has referrals from orthopedic surgeons, and one case involving pain medication side effects needs closure. Check her incoming referral queue, identify which patient came from orthopedics, then close that case. Review the patient's current medications for skin-related concerns, and create a follow-up referral to pediatrics for specialized medication management with Dr. Lisa Wilson.",
        "actions": [
            {
                "name": "get_doctor_referrals",
                "arguments": {
                    "doctor_identifier": "Dr. Jennifer Martinez",
                    "referral_type": "incoming"
                },
            },
            {
                "name": "update_referral_status",
                "arguments": {
                    "patient_identifier": "Jennifer Brown",
                    "referred_to_doctor_identifier": "Dr. Jennifer Martinez",
                    "new_status": "completed"
                },
            },
            {
                "name": "get_patient_medications",
                "arguments": {
                    "patient_identifier": "Jennifer Brown"
                },
            },
            {
                "name": "create_referral",
                "arguments": {
                    "patient_identifier": "Jennifer Brown",
                    "referring_doctor_identifier": "Dr. Jennifer Martinez",
                    "referred_to_doctor_identifier": "Dr. Lisa Wilson",
                    "referred_to_department": "Pediatrics",
                    "priority": "routine"
                },
            },
        ],
    },
]