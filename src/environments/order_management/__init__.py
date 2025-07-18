import os

from .functions import FUNCTIONS_MAP
from .entries import entries
from .filter_schema import filter_schema
from .data import load_json_files

CURRENT_PATH = os.path.dirname(__file__)

with open(os.path.join(CURRENT_PATH, "instructions.md"), "r", encoding="utf-8") as f:
    INSTRUCTIONS = f.read()

# Add entry_num to each entry
entries_with_num = []
for index, entry in enumerate(entries, start=1):
    entry_with_num = entry.copy()
    entry_with_num["entry_num"] = index
    entries_with_num.append(entry_with_num)

config = {
    "functions": FUNCTIONS_MAP,
    "entries": entries_with_num,
    "filter_schema": filter_schema,
    "data": load_json_files(),
    "instructions": INSTRUCTIONS,
}

__all__ = ["config"]
