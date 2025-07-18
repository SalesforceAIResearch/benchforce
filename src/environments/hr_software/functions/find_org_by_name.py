import json
from typing import Any, Dict
from src.classes.function import Function


class FindOrgByName(Function):
    @staticmethod
    def apply(data: Dict[str, Any], query: str) -> str:
        """
        Find organizations where the name contains the given query string (case-insensitive).
        
        Args:
            data (Dict[str, Any]): The data containing organizations
            query (str): The search string to look for in organization names
            
        Returns:
            str: JSON string containing the search results
        """
        query = query.lower()
        matching_orgs = [
            org for org in data["organizations"].values()
            if query in org["name"].lower()
        ][:10]
        
        if matching_orgs:
            return json.dumps({"found": True, "organizations": matching_orgs})
        return json.dumps({"found": False, "error": "No organizations found matching the query"})

    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_org_by_name",
                "description": "Find organizations where the name contains the given query string (case-insensitive).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "The search string to look for in organization names",
                        },
                    },
                    "required": ["query"],
                },
            },
        }