filter_schema = {
    "doctors": {
        "doctor_id": True,
        "name": True,
        "specialty": True,
        "department": True,
        "clinic": True,
    },
    "patients": {
        "patient_id": True,
        "name": True,
        "date_of_birth": True,
        "email": True,
        "phone": True,
    },
    "appointments": {
        "*": {  
            "confirmation_code": False,
            "appointment_id": False,
            "patient_id": True,
            "doctor_id": True,
            "appointment_date": True,
            "appointment_time": True,
            "status": True,
            "department": True,
            "clinic": True,
            "reason": False,
            "notes": False,
            "rating": False,
        }
    },
    "available_slots": True 
}
