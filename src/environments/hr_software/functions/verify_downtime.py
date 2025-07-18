# Copyright Sierra

import json
from typing import Any, Dict
from src.classes.function import Function
from datetime import datetime


class VerifyDowntime(Function):
    @staticmethod
    def apply(data: Dict[str, Any], subscription_id: str, incident_timestamp: str) -> str:
        subscription = data["subscriptions"][subscription_id]
        downtime_logs = data["downtime_logs"]

        # make sure the sub has tier at 'professional' or 'enterprise'
        if subscription["tier"] not in ["professional", "enterprise"]:
            return json.dumps({"error": "Subscription tier is not professional or enterprise. No downtime logs available."})

        try:
            incident_time = datetime.fromisoformat(incident_timestamp.replace('Z', '+00:00'))
        except ValueError:
            return json.dumps({"error": "Invalid timestamp format. Use ISO format (e.g., 2024-05-15T15:00:00Z)"})
            
        # Check if incident is within last 30 days
        now = datetime.fromisoformat("2024-05-15T15:00:00+00:00")  # Current time from wiki
        days_diff = (now - incident_time).days
        if days_diff > 30:
            return json.dumps({
                "error": "Incident logs must be requested within 30 days"
            })
            
        # Check if there was actual downtime
        downtime_found = False
        duration_minutes = 0
        
        for log in downtime_logs:
            if log["start_time"] <= incident_timestamp <= log["end_time"]:
                downtime_found = True
                # Calculate duration in minutes
                start = datetime.fromisoformat(log["start_time"].replace('Z', '+00:00'))
                end = datetime.fromisoformat(log["end_time"].replace('Z', '+00:00'))
                duration_minutes = int((end - start).total_seconds() / 60)
                break
                
        if not downtime_found:
            return json.dumps({
                "verified": False,
                "message": "No downtime found at the specified time"
            })
            
        # Check if it's an excluded event
        if any(exclusion["type"] in ["maintenance", "force_majeure", "customer_caused", "third_party"]
               for exclusion in log.get("exclusions", [])):
            return json.dumps({
                "verified": False,
                "message": "Downtime was due to an excluded event"
            })
            
        return json.dumps({
            "verified": True,
            "duration_minutes": duration_minutes,
            "tier": subscription["tier"]
        })

    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "verify_downtime",
                "description": "Verify if there was actual service downtime at the specified time.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subscription_id": {
                            "type": "string",
                            "description": "The subscription ID in format SUB-XXXXX.",
                        },
                        "incident_timestamp": {
                            "type": "string",
                            "description": "The timestamp of the incident in ISO format (e.g., 2024-05-15T15:00:00Z).",
                        },
                    },
                    "required": ["subscription_id", "incident_timestamp"],
                },
            },
        } 