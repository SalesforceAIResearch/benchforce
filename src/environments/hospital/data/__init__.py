import os
import json

def load_json_files():
    directory = os.path.dirname(os.path.abspath(__file__))
    
    data = {}
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            file_path = os.path.join(directory, filename)
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    data[os.path.splitext(filename)[0]] = json.load(file)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading {filename}: {e}")
    return data
