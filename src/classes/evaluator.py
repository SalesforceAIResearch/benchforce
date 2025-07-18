import time
import uuid
import os

import pandas as pd

from src.classes.helper import Helper


class Evaluator:
    def __init__(self, metrics):
        self.task_results = []
        self.metrics = metrics
        self.id = str(uuid.uuid4())

    def check_entry(self, session_id, entry, environment):
        file_path = Helper.get_transcript_file_path(session_id)
        if not os.path.exists(file_path):
            return

        results = {
            "entry_id": f"{entry.get('entry_num', 1):03}",
            "timestamp": time.time()
        }

        for metric_name, metric_class in self.metrics.items():
            if hasattr(metric_class, "calculate") and callable(getattr(metric_class, "calculate")):
                results[metric_name] = metric_class.calculate(session_id, entry, environment=environment)
            else:
                results[metric_name] = None
        
        self.task_results.append(results)

    def final_results(self):
        aggregated_dfs = []
        json_results = {}

        for metric_name, metric_class in self.metrics.items():
            metric_results = []
            for result in self.task_results:
                if metric_name in result and result[metric_name] is not None:
                    metric_results.append(result[metric_name])
                
            if metric_results:
                try:
                    agg_df, agg_json = metric_class.aggregate(metric_results)
                    melted_df = agg_df.melt(var_name="parameter", value_name="value")
                    melted_df["metric"] = metric_name
                    melted_df = melted_df[["metric", "parameter", "value"]]
                    aggregated_dfs.append(melted_df)
                    json_results[metric_name] = agg_json
                except Exception as e:
                    error_df = pd.DataFrame({
                        "metric": [metric_name],
                        "parameter": [f"{metric_name}_error"],
                        "value": [str(e)]
                    })
                    aggregated_dfs.append(error_df)

        if aggregated_dfs:
            final_df = pd.concat(aggregated_dfs, axis=0, ignore_index=True)
        else:
            final_df = pd.DataFrame()
        
        return final_df, json_results
