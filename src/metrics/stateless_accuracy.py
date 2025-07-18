import os
import json
import ast
import re
import pandas as pd
import numpy as np
import pdb
import sys

sys.path.insert(0, os.getcwd())

from src.classes.packet import EventType
from src.classes.helper import Helper

STATE_MAP = {
    r'\bcalifornia\b': 'ca',
    r'\bca\b': 'ca',
    r'\bnew york\b': 'ny',
    r'\bny\b': 'ny',
    r'\billinois\b': 'il',
    r'\bil\b': 'il',
    r'\bill\b': 'il',
    r'\bwashington,? d\.?c\.?\b': 'dc',
    r'\bdc\b': 'dc',
}

STREET_MAP = {
    r'\bstreet\b': 'st',
    r'\bst\.\b': 'st',
    r'\bavenue\b': 'ave',
    r'\bave\.\b': 'ave',
    r'\bdrive\b': 'dr',
    r'\bdr\.\b': 'dr',
    r'\broad\b': 'rd',
    r'\brd\.\b': 'rd',
    r'\bboulevard\b': 'blvd',
    r'\bblvd\.\b': 'blvd',
}


def normalize_address(addr: str) -> str:
    s = addr.strip().lower()
    s = re.sub(r'[.,]', '', s)
    for pattern, abbr in STATE_MAP.items():
        s = re.sub(pattern, abbr, s)
    for pattern, abbr in STREET_MAP.items():
        s = re.sub(pattern, abbr, s)
    return re.sub(r'\s+', ' ', s).strip()


def normalize_item(item):
    if isinstance(item, dict):
        clean = {}
        for k, v in item.items():
            if v == "*":
                continue
            if k.lower() == "address":
                clean[k] = normalize_address(str(v))
            else:
                clean[k] = str(v).strip().lower()
        return json.dumps(clean, sort_keys=True, ensure_ascii=False)
    else:
        return str(item).strip().lower()


def ensure_list(x):
    if isinstance(x, str):
        for loader in (json.loads, ast.literal_eval):
            try:
                parsed = loader(x)
                if isinstance(parsed, list):
                    return parsed
            except Exception:
                pass
    return x


def element_matches(sub, sup):
    if isinstance(sub, dict) and isinstance(sup, dict):
        # Get case insensitive args list from sub if it exists
        case_insensitive_args = sub.get("case_insensitive_args", [])
        
        # Compare name first
        if sub.get("name") != sup.get("name"):
            return False
            
        # Compare arguments
        sub_args = sub.get("arguments", {})
        sup_args = sup.get("arguments", {})
        
        for k, v in sub_args.items():
            if v == "*":
                continue
            if k not in sup_args:
                return False
            
            # Check if this argument should be compared case-insensitively
            if k in case_insensitive_args:
                if k.lower() == "address":
                    if normalize_address(str(v)) != normalize_address(str(sup_args[k])):
                        return False
                else:
                    # Case insensitive comparison for this argument
                    if str(v).strip().lower() != str(sup_args[k]).strip().lower():
                        return False
            else:
                # Default case sensitive comparison
                if k.lower() == "address":
                    if normalize_address(str(v)) != normalize_address(str(sup_args[k])):
                        return False
                else:
                    if normalize_item(v) != normalize_item(sup_args[k]):
                        return False
        return True
    if sub == "*":
        return True
    return normalize_item(sub) == normalize_item(sup)


def smart_list_contains(subset, superset):
    subset = ensure_list(subset)
    superset = ensure_list(superset)
    for sub in subset:
        if not any(element_matches(sub, sup) for sup in superset):
            return False
    return True


def smart_list_equal(list1, list2):
    norm1 = set(normalize_item(x) for x in list1)
    norm2 = set(normalize_item(x) for x in list2)
    return norm1 == norm2


def safe_avg(lst):
    arr = np.array(lst, dtype=float)
    arr = arr[~np.isnan(arr)]
    return int(np.mean(arr)) if arr.size > 0 else None


def safe_min(lst):
    arr = np.array(lst, dtype=float)
    arr = arr[~np.isnan(arr)]
    return int(np.min(arr)) if arr.size > 0 else None


def safe_max(lst):
    arr = np.array(lst, dtype=float)
    arr = arr[~np.isnan(arr)]
    return int(np.max(arr)) if arr.size > 0 else None


def is_tts_problematic(text) -> bool:
    if not isinstance(text, str) or not text:
        return False
    literal_punct = r"[()\[\]{}]"
    markup = r"[*_`~^]"
    bullet_start = r"^\s*([*\-•◦▪+]|\d+\.)\s+"
    bullet_mid = r"(?:\n|\r)\s*([*\-•◦▪+]|\d+\.)\s+"
    code_url = r"[<>|#\\$%]"
    excessive = r"([.?!])\1{2,}"
    hyphens = r"--+|(?<=\s)-(?=\s)"
    url_email = r"://|@"
    pattern = re.compile(
        f"(?:{literal_punct}|{markup}|{bullet_start}|{bullet_mid}|"
        f"{code_url}|{excessive}|{hyphens}|{url_email})",
        re.MULTILINE
    )
    return bool(pattern.search(text))


def avg(xs):
    return sum(xs) / len(xs) if xs else None


class StatelessAccuracy:
    @staticmethod
    def calculate(session_id: str, entry, **kwargs):
        transcript = Helper.read_transcript(session_id)
        turns = Helper.parse_turns(transcript, with_timestamp=True, with_functions=True)

        ground_truth_actions = entry.get("actions", [])

        conversation_actions = []

        for item in transcript:
            parsed = json.loads(item["message"])
            if parsed.get("event") == EventType.RESPONSE_FUNCTION_CALL:
                function_call = parsed.get("function_call")
                if function_call and isinstance(function_call.get("arguments"), str):
                    try:
                        function_call["arguments"] = json.loads(function_call["arguments"])
                    except json.JSONDecodeError:
                        pass
                conversation_actions.append(function_call)

       
        action_result = 1 if smart_list_contains(ground_truth_actions, conversation_actions) else 0
        
        #pdb.set_trace()
        return {
            "session_id": session_id,
            "actions": action_result,
            "final_score": action_result, #nessesary for dashboard
            "turns_count": len(turns),
            "turns": turns,
            "ground_truth_actions": ground_truth_actions,
            "conversation_actions": conversation_actions,
        }


    @staticmethod
    def aggregate(results):
        df = pd.DataFrame(results)

        total = len(df)
        passed = df["actions"].sum()
        accuracy = (passed / total) * 100 if total else 0

        summary_df = pd.DataFrame([{
            "Total Test Cases": total,
            "Accuracy": f"{accuracy:.2f}% ({passed}/{total})",

        }])

        json_result = {
            "summary": {
                "total": total,
                "accuracy": f"{accuracy:.2f}% ({passed}/{total})",
            },
            "sessions": results
        }

        return summary_df, json_result
    
