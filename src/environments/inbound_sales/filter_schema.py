filter_schema = {
    "sales_reps": {"rep_id": True, "name": True, "email": True},
    "meetings": {
        "*": {
            "meeting_id": True,
            "lead_id": True,
            "rep_id": True,
            "meeting_date": True,
            "meeting_time": True,
        }
    },
    "leads": {
        "*": {
            "lead_id": True,
            "name": True,
            "contact_number": True,
            "email": True,
            "company": True,
            "industry": True,
            "source": True,
            "status": True,
            "notes": False,
            "created_date": True,
            "qualification_score": True,
        }
    },
    "lead_history": {
        "*": {"action": False, "date": True}
    },
    "calls": {
        "*": {
            "call_id": True,
            "lead_id": True,
            "rep_name": True,
            "call_outcome": False,
        }
    },
    "followups": {
        "*": {
            "followup_id": True,
            "lead_id": True,
            "followup_action": False,
        }
    },
}
