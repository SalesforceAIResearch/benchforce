import os
import logging
from datetime import datetime
from .functions import FUNCTIONS_MAP
from .entries import entries, deep_copied_data
from .filter_schema import filter_schema

CURRENT_PATH = os.path.dirname(__file__)

with open(os.path.join(CURRENT_PATH, "instructions.md"), "r", encoding="utf-8") as f:
    INSTRUCTIONS = f.read()

# Add current date to instructions
current_date = datetime.now().strftime("%Y-%m-%d")
INSTRUCTIONS = f"{INSTRUCTIONS}\n\nCurrent date: {current_date}"

config = {
    "functions": FUNCTIONS_MAP,
    "entries": entries,
    "filter_schema": filter_schema,
    "data": deep_copied_data,
    "instructions": INSTRUCTIONS,
}

__all__ = ["config"]