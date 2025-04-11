from typing import Any, Dict
from src.classes.function import Function
import json

class GenerateAppointmentReport(Function):
    @staticmethod
    def apply(data: Dict[str, Any], appointment_date: str) -> str:
        appointments = data.get('appointments', {})
        report = [appt for appt in appointments.values() if appt.get("appointment_date") == appointment_date]
        summary = {
            "appointment_date": appointment_date,
            "total_appointments": len(report),
            "report": report
        }
        return json.dumps(summary)
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_appointment_report",
                "description": "Generates a summary report of healthcare appointments for a given date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "appointment_date": {"type": "string", "description": "The date (ISO format) for the report."}
                    },
                    "required": ["appointment_date"]
                }
            }
        }