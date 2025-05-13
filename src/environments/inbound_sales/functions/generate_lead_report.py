import json
from typing import Any, Dict
from src.classes.function import Function


class GenerateLeadReport(Function):
    @staticmethod
    def apply(data: Dict[str, Any], report_period: str) -> str:
        leads = data.get('leads', {})
        report = [lead for lead in leads.values() if lead.get("created_date", "").startswith(report_period)]
        summary = {
            "report_period": report_period,
            "total_leads": len(report),
            "leads": report
        }
        return json.dumps(summary)
    
    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_lead_report",
                "description": "Generates a summary report of leads for a specified period (YYYY-MM).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_period": {"type": "string", "description": "The period for the report in YYYY-MM format."}
                    },
                    "required": ["report_period"]
                }
            }
        }