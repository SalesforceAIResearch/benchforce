import json
from typing import Any, Dict
from src.classes.function import Function

class ScheduleMeeting(Function):
    @staticmethod
    def apply(
        data: Dict[str, Any],
        meeting_id: str,
        lead_id: str,
        rep_name: str,
        meeting_date: str,
        meeting_time: str
    ) -> str:
        meetings = data.get('meetings', {})
        sales_reps = data.get('sales_reps', [])

        rep_id = None
        for rep in sales_reps:
            if rep.get("name") == rep_name:
                rep_id = rep.get("rep_id")
                break
        if rep_id is None:
            return f"Error: sales representative '{rep_name}' not found"
        meeting = {
            "meeting_id": meeting_id,
            "lead_id": lead_id,
            "rep_id": rep_id,
            "meeting_date": meeting_date,
            "meeting_time": meeting_time
        }
        meetings[meeting_id] = meeting
        data['meetings'] = meetings
        return json.dumps({"message": "Meeting scheduled", "meeting": meeting})
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "schedule_meeting",
                "description": "Schedules a meeting between a lead and a sales representative.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "meeting_id": {"type": "string", "description": "Unique meeting identifier (e.g., 'M1001')."},
                        "lead_id": {"type": "string", "description": "The unique identifier of the lead."},
                        "rep_name": {"type": "string", "description": "Full name of the sales representative."},
                        "meeting_date": {"type": "string", "description": "Date of the meeting (ISO format)."},
                        "meeting_time": {"type": "string", "description": "Time of the meeting (HH:MM)."}
                    },
                    "required": ["meeting_id", "lead_id", "rep_name", "meeting_date", "meeting_time"]
                }
            }
        }