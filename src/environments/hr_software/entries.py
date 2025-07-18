import os
import json

DUMP_PATH = os.path.join(os.path.dirname(__file__), "entries_dump.json")

DATA_FILES = {
    "organizations": os.path.join(os.path.dirname(__file__), "data_organizations.json"),
    "downtime_logs": os.path.join(os.path.dirname(__file__), "data_downtime_logs.json"),
    "subscriptions": os.path.join(os.path.dirname(__file__), "data_subscriptions.json"),
}

USERS_PARTS = [
    os.path.join(os.path.dirname(__file__), "data_users_part_1.json"),
    os.path.join(os.path.dirname(__file__), "data_users_part_2.json"),
    os.path.join(os.path.dirname(__file__), "data_users_part_3.json"),
    os.path.join(os.path.dirname(__file__), "data_users_part_4.json"),
    os.path.join(os.path.dirname(__file__), "data_users_part_5.json"),
    os.path.join(os.path.dirname(__file__), "data_users_part_6.json"),
]

deep_copied_data = {}

for key, file_path in DATA_FILES.items():
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            deep_copied_data[key] = json.load(f)
    except FileNotFoundError:
        deep_copied_data[key] = {}
    except Exception as e:
        deep_copied_data[key] = {}

deep_copied_data["users"] = {}

for file_path in USERS_PARTS:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            part_data = json.load(f)
            deep_copied_data["users"].update(part_data)
    except FileNotFoundError:
        pass
    except Exception as e:
        pass

with open(DUMP_PATH, "r", encoding="utf-8") as f:
    entries = json.load(f) 