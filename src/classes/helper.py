import os
import json
import hashlib
import copy
import logging

class Helper:
    @staticmethod
    def get_transcript_file_path(session_id: str):
        base_dir = os.getcwd() 
        file_path = os.path.join(base_dir, "history", session_id, "transcript.jsonl")
        return file_path

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
    def parse_turns(transcript):
        allowed_events = {"response.done", "response.audio_transcript.done", "response.text.done"}
        events = []
        
        for item in transcript:
            try:
                inner = json.loads(item.get("message", "{}"))
            except Exception:
                inner = {}
            event_type = inner.get("event")
            if event_type in allowed_events:
                events.append({
                    "role": item.get("role"),
                    "event": event_type,
                    "message": inner.get("text"),
                })
                
        turns = []
        current_turn = []
        client_done = False
        agent_done = False
        
        for ev in events:
            if ev["event"] in ("response.text.done", "response.audio_transcript.done"):
                current_turn.append({
                    "role": ev["role"],
                    "message": ev["message"]
                })
            elif ev["event"] == "response.done":
                if ev["role"] == "client":
                    client_done = True
                elif ev["role"] == "agent":
                    agent_done = True

            if client_done and agent_done:
                if current_turn:
                    turns.append(current_turn)
                current_turn = []
                client_done = False
                agent_done = False
                
        if current_turn:
            turns.append(current_turn)
        
        return turns