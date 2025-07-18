filter_schema = {
    "type": "object",
    "properties": {
        "patient_id": {"type": "string"},
        "doctor_id": {"type": "string"},
        "department": {"type": "string"},
        "appointment_time": {"type": "string"},
        "medication": {"type": "string"},
        "lab_test": {"type": "string"},
        "contact_name": {"type": "string"},
        "contact_phone": {"type": "string"}
    },
    "additionalProperties": False
}