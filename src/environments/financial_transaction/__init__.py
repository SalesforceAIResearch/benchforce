import os

from .functions import FUNCTIONS_MAP
from .entries import entries
from .filter_schema import filter_schema
from .data import load_json_files

CURRENT_PATH = os.path.dirname(__file__)

with open(os.path.join(CURRENT_PATH, "instructions.md"), "r", encoding="utf-8") as f:
    INSTRUCTIONS = f.read()

config = {
    "functions": FUNCTIONS_MAP,
    "entries": entries,
     "filter_schema": filter_schema,
    "data": load_json_files(),
    "instructions": INSTRUCTIONS,
}

__all__ = ["config"]