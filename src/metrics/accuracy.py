import json
import pandas as pd
import numpy as np

from collections import defaultdict
from src.classes.packet import EventType
from src.classes.helper import Helper


class Accuracy:
    @staticmethod
    def calculate(session_id: str, entry, **kwargs):
        transcript = Helper.read_transcript(session_id)

        ground_truth_outputs = entry.get("outputs", [])

        last_runtime_hash = next(
            (json.loads(item["message"]) for item in reversed(transcript)
             if json.loads(item["message"]).get("event") == EventType.RESPONSE_FUNCTION_CALL_RESULT
             and json.loads(item["message"]).get("hash")),
            None
        )

        last_ground_truth_hash  = next(
            (json.loads(item["message"]) for item in reversed(transcript)
             if json.loads(item["message"]).get("event") == EventType.BENCHFORCE_LOG_DRYRUN_DB
             and json.loads(item["message"]).get("hash")),
            None
        )

        last_original_hash = next(
            (json.loads(item["message"]) for item in reversed(transcript)
             if json.loads(item["message"]).get("event") == EventType.BENCHFORCE_LOG_ORIG_DB
             and json.loads(item["message"]).get("hash")),
            None
        )

        terminated = next(
            (json.loads(item["message"]) for item in transcript
             if json.loads(item["message"]).get("event") == EventType.BENCHFORCE_TERMINATE),
            None
        )

        runtime_hash = last_runtime_hash.get("hash") if last_runtime_hash else None
        ground_truth_hash = last_ground_truth_hash.get("hash") if last_ground_truth_hash else None
        original_hash = last_original_hash.get("hash") if last_original_hash else None

        agent_text_outputs = " ".join([
            json.loads(item["message"]).get("text")
            for item in transcript
            if item["role"] == "agent" and json.loads(item["message"]).get("event")
               in [EventType.RESPONSE_TEXT_DONE, EventType.RESPONSE_AUDIO_TRANSCRIPT_DONE]
        ])

        accuracy = 0

        total_outputs = len(ground_truth_outputs)
        matched_outputs = 0

        if total_outputs > 0:
            agent_text_outputs_lower = agent_text_outputs.lower()
            available_text = agent_text_outputs_lower
            processed_ground_truth = [str(item).lower() for item in ground_truth_outputs if isinstance(item, str)]
            for expected_output in processed_ground_truth:
                idx = available_text.find(expected_output)
                if idx != -1:
                    matched_outputs += 1
                    available_text = available_text[:idx] + " " * len(expected_output) + available_text[idx+len(expected_output):]

            accuracy = 1 if total_outputs == matched_outputs else 0

        elif runtime_hash and ground_truth_hash and original_hash:
            accuracy = 1 if runtime_hash == ground_truth_hash else 0

        return {"session_id": session_id, "accuracy": accuracy, "terminated": True if terminated else False}


    @staticmethod
    def aggregate(results):
        grouped_sessions = defaultdict(list)
        for result in results:
            session_id_full = result["session_id"]
            base_session_id = "-".join(session_id_full.split("-")[:-1])
            grouped_sessions[base_session_id].append(result)

        total_tasks = len(results)
        finished_tasks = sum(1 for r in results if r.get("terminated"))

        all_scores = []
        finished_scores = []

        for session_id, session_results in grouped_sessions.items():
            session_score_all = 1 if all(r["accuracy"] == 1 for r in session_results) else 0
            all_scores.append(session_score_all)

            finished = [r for r in session_results if r.get("terminated")]
            if finished:
                session_score_finished = 1 if all(r["accuracy"] == 1 for r in finished) else 0
                finished_scores.append(session_score_finished)

        accuracy_all = np.mean(all_scores) if all_scores else 0
        accuracy_finished = np.mean(finished_scores) if finished_scores else 0

        aggregated_data = {
            "Total entries": total_tasks,
            "Finished entries": finished_tasks,
            "Accuracy (All)": accuracy_all,
            "Accuracy (Finished)": accuracy_finished
        }

        json_results = {
            "total_entries": total_tasks,
            "finished_entries": finished_tasks,
            "accuracy_all": float(accuracy_all),
            "accuracy_finished": float(accuracy_finished)
        }

        df = pd.DataFrame([aggregated_data])
        return df, json_results
