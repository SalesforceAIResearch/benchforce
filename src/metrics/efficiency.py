import json
import pandas as pd
import numpy as np

from src.classes.helper import Helper


class Efficiency:
    @staticmethod
    def calculate(session_id: str, entry, **kwargs):
        transcript = Helper.read_transcript(session_id)
        turns = Helper.parse_turns(transcript)

        total_tokens = 0
        for item in transcript:
            try:
                message = json.loads(item["message"])
                tokens = message.get("tokens")
                if tokens is not None:
                    total_tokens += tokens
            except Exception:
                continue

        result = {
            "tokens": total_tokens,
            "turns": len(turns)
        }

        return result

    @staticmethod
    def aggregate(results):
        token_values = []
        turn_values = []

        for result in results:
            try:
                if result.get("tokens") is not None:
                    token_values.append(result["tokens"])
                if result.get("turns") is not None:
                    turn_values.append(result["turns"])
            except Exception:
                continue

        tokens_average = np.mean(token_values) if token_values else None
        tokens_median = np.median(token_values) if token_values else None
        turns_average = np.mean(turn_values) if turn_values else None
        turns_median = np.median(turn_values) if turn_values else None

        aggregated_data = {
            "tokens_average": tokens_average,
            "tokens_median": tokens_median,
            "turns_average": turns_average,
            "turns_median": turns_median,
        }

        json_results = {
            "tokens_average": float(tokens_average) if tokens_average is not None else None,
            "tokens_median": float(tokens_median) if tokens_median is not None else None,
            "turns_average": float(turns_average) if turns_average is not None else None,
            "turns_median": float(turns_median) if turns_median is not None else None,
        }

        df = pd.DataFrame([aggregated_data])
        return df, json_results
