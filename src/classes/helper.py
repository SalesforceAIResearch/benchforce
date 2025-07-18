import os
import json
import hashlib
import copy
import logging
import tiktoken

SESSION_TRANSCRIPT_FILE_NAME = "transcript.jsonl"
SESSION_AUDIO_FILE_NAME = "output.wav"
SESSION_COMPLETED_FILE_NAME = "COMPLETED"


class Helper:
    @staticmethod
    def get_runs_base_path():
        return os.path.join(os.getcwd(), "results")

    @staticmethod
    def get_run_base_path(runner_id: str):
        return os.path.join(Helper.get_runs_base_path(), runner_id)

    @staticmethod
    def get_run_result_file_path(runner_id: str):
        return os.path.join(Helper.get_run_base_path(runner_id=runner_id), "result.json")

    @staticmethod
    def get_sessions_base_path():
        return os.path.join(os.getcwd(), "history")

    @staticmethod
    def get_session_base_path(session_id: str):
        return os.path.join(Helper.get_sessions_base_path(), session_id)

    @staticmethod
    def get_transcript_file_path(session_id: str):
        return os.path.join(Helper.get_session_base_path(session_id=session_id), SESSION_TRANSCRIPT_FILE_NAME)

    @staticmethod
    def get_audio_file_path(session_id: str):
        return os.path.join(Helper.get_session_base_path(session_id=session_id), SESSION_AUDIO_FILE_NAME)

    @staticmethod
    def get_completed_file_path(session_id: str):
        return os.path.join(Helper.get_session_base_path(session_id=session_id), SESSION_COMPLETED_FILE_NAME)

    @staticmethod
    def is_session_completed(session_id: str, mode: str = "voice") -> bool:
        transcript_path = Helper.get_transcript_file_path(session_id=session_id)
        audio_path = Helper.get_audio_file_path(session_id=session_id)
        completed_path = Helper.get_completed_file_path(session_id=session_id)
        
        if mode == "voice":
            all_outputs = [transcript_path, audio_path, completed_path]
        else:
            all_outputs = [transcript_path, completed_path]
        
        # Check all files exist
        if not all(os.path.isfile(path) for path in all_outputs):
            return False
        
        # Check file sizes - COMPLETED file just needs to be non-empty
        if os.path.getsize(completed_path) == 0:
            return False
            
        # Other files need to be at least 50 bytes
        if os.path.getsize(transcript_path) < 50 or (mode == "voice" and os.path.getsize(audio_path) < 50):
            return False
            
        return True

    @staticmethod
    def deleted_session_outputs(session_id: str) -> bool:
        all_outputs = [
            Helper.get_transcript_file_path(session_id=session_id),
            Helper.get_audio_file_path(session_id=session_id),
            Helper.get_completed_file_path(session_id=session_id),
        ]
        for path in all_outputs:
            if os.path.exists(path):
                os.remove(path)

    @staticmethod
    def read_transcript(session_id: str):
        file_path = Helper.get_transcript_file_path(session_id)

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File {file_path} not found!")

        with open(file_path, "r", encoding="utf-8") as f:
            return [json.loads(line) for line in f]
        
    @staticmethod
    def oai_parse_functions(functions):
        parsed_functions = []

        for function_class in functions:
            function_instance = function_class()
            function_info = function_instance.get_metadata()
            parsed_functions.append(function_info)
        return parsed_functions
    
    @staticmethod
    def oai_rt_parse_functions(functions):
        parsed_functions = []

        for function_class in functions:
            function_instance = function_class()
            function_info = function_instance.get_metadata()
            function_info["function"]["type"] = "function"
            parsed_functions.append(function_info["function"])

        return parsed_functions
    
    @staticmethod
    def xai_parse_functions(functions):
        parsed_functions = []

        for function_class in functions:
            function_instance = function_class()
            function_info = function_instance.get_metadata()
            parsed_functions.append(function_info)
        return parsed_functions
        
    @staticmethod
    def google_parse_functions(functions):
        parsed_functions = []

        for function_class in functions:
            function = {}
            function_instance = function_class()
            function_info = function_instance.get_metadata()
            function["name"] = function_info["function"]["name"]
            function["description"] = function_info["function"]["description"]
            function["parameters"] = function_info["function"]["parameters"]

            parsed_functions.append(function)

        return parsed_functions
    
    @staticmethod
    def anthropic_parse_functions(functions):
        parsed_functions = []

        for function_class in functions:
            function = {}
            function_instance = function_class()
            function_info = function_instance.get_metadata()
            function["name"] = function_info["function"]["name"]
            function["description"] = function_info["function"]["description"]
            function["input_schema"] = function_info["function"]["parameters"]
            
            parsed_functions.append(function)

        return parsed_functions
    
    @staticmethod
    def get_modalities(type, client_mode, agent_mode):
        mode = client_mode if type == "client" else agent_mode

        if mode in {"realtime-multimodal", "text-voice-multimodal"}:
            return ["text", "audio"]
        elif mode in {"realtime-voice", "voice"}:
            return ["audio"]
        elif mode in {"realtime-text", "text"}:
            return ["text"]
        
        return []
    
    @staticmethod
    def generate_full_mask(data):
        if isinstance(data, dict):
            return {k: Helper.generate_full_mask(v) for k, v in data.items()}
        elif isinstance(data, list) and data:
            return Helper.generate_full_mask(data[0])
        else:
            return True
        
    @staticmethod
    def dry_run(data, entry, functions):
        data_copy = copy.deepcopy(data)
        for action in entry['actions']:
            func_name = action['name']
            arguments = action['arguments']

            if func_name in functions:
                func_class = functions[func_name]
                try:
                    func_class.apply(data_copy, **arguments)
                except Exception as e:
                    logging.error(f"Error while executing function {entry['id']} '{func_name}': {e}")
        return data_copy
    
    
    @staticmethod
    def normalize_data(data):
        if isinstance(data, dict):
            return {k: Helper.normalize_data(data[k]) for k in sorted(data)}
        elif isinstance(data, list):
            normalized_list = [Helper.normalize_data(item) for item in data]
            try:
                return sorted(normalized_list, key=lambda x: json.dumps(x, sort_keys=True, separators=(",", ":")))
            except TypeError:
                return normalized_list
        else:
            return data

    @staticmethod
    def get_data_hash(data):
        normalized = Helper.normalize_data(data)
        json_str = json.dumps(normalized, sort_keys=True, separators=(",", ":"))
        return hashlib.sha256(json_str.encode("utf-8")).hexdigest()

    @staticmethod
    def apply_mask(data, mask):
        if mask is True:
            return data
        elif mask is False or mask is None:
            return None

        if isinstance(data, dict) and isinstance(mask, dict):
            result = {}
            for k, v in data.items():
                if k in mask:
                    submask = mask[k]
                    if submask is False:
                        continue
                    masked_value = Helper.apply_mask(v, submask)
                    if masked_value is not None:
                        result[k] = masked_value
                elif "*" in mask:
                    submask = mask["*"]
                    if submask is False:
                        continue
                    masked_value = Helper.apply_mask(v, submask)
                    if masked_value is not None:
                        result[k] = masked_value
            return result

        elif isinstance(data, list):
            if isinstance(mask, dict):
                return [Helper.apply_mask(item, mask) for item in data]
            elif mask is True:
                return data
            else:
                return None

        return data if mask is True else None
    
    @staticmethod
    def strip_markdown(text: str) -> str:
        """Strip markdown formatting from text"""
        import re
        
        text = re.sub(r'```[\s\S]*?```', '', text)
        text = re.sub(r'`([^`]*)`', r'\1', text)
        text = re.sub(r'^\s{0,3}(#{1,6})\s*', '', text, flags=re.MULTILINE)
        text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
        text = re.sub(r'\*(.*?)\*', r'\1', text)
        text = re.sub(r'__(.*?)__', r'\1', text)
        text = re.sub(r'_(.*?)_', r'\1', text)
        text = text.replace('~~', '')
        text = re.sub(r'^\s{0,3}>\s?', '', text, flags=re.MULTILINE)
        text = re.sub(r'!\[(.*?)\]\((.*?)\)', '', text)
        text = re.sub(r'\[(.*?)\]\((.*?)\)', r'\1', text)
        
        return text


    def format_number_with_dashes(text: str) -> str:
        """Format long numbers with dashes for better speech synthesis"""
        import re
        
        pattern = r'\b\d{7,}\b'
        
        def replace_with_dashes(match):
            number = match.group(0)
            return ' '.join(list(number))
        
        return re.sub(pattern, replace_with_dashes, text)
    
    
    @staticmethod
    def num_tokens_from_string(string: str, model_name: str = "gpt-4o") -> int:
        encoding = tiktoken.encoding_for_model(model_name)
        num_tokens = len(encoding.encode(string))
        return num_tokens

    @staticmethod
    def filter_by_event_role(transcript, event, role):
        events = []

        for item in transcript:
            try:
                inner = json.loads(item.get("message", "{}"))
            except Exception:
                inner = {}
            event_type = inner.get("event")
            event_role = item.get("role")
            if event_type == event and event_role == role:
                events.append(inner)

        return events


    @staticmethod
    def parse_turns(transcript, with_timestamp = False, with_functions = False):
        allowed_events = {"response.done", "response.audio_transcript.done", "response.text.done", "response.function_call"}
        events = []
        
        for item in transcript:
            try:
                inner = json.loads(item.get("message", "{}"))
            except Exception:
                inner = {}
            event_type = inner.get("event")
            if event_type in allowed_events:
                event = {
                    "role": item.get("role"),
                    "event": event_type,
                    "message": inner.get("text"),
                }

                if with_timestamp:
                    event["timestamp"] = item.get("timestamp")

                events.append(event)
                
        turns = []
        current_turn = []
        client_done = False
        agent_done = False
        function_called = False
        
        for ev in events:
            if ev["event"] in ("response.text.done", "response.audio_transcript.done"):
                el = {
                    "role": ev["role"],
                    "message": ev["message"]
                }

                if with_timestamp:
                    el["timestamp"] = ev.get("timestamp")

                current_turn.append(el)

            elif ev["event"] == "response.done":
                if ev["role"] == "client":
                    client_done = True
                elif ev["role"] == "agent":
                    agent_done = True

            elif ev["event"] == "response.function_call" and with_functions and ev["role"] == "agent":
                function_called = True

            if client_done and agent_done:
                if function_called:
                    for el in current_turn:
                        el["function_call"] = True

                if current_turn:
                    turns.append(current_turn)
                current_turn = []
                client_done = False
                agent_done = False
                function_called = False
        
        return turns
