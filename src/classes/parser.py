import sys
import logging
import yaml
import argparse
import pandas as pd

defaults = {
    "client_tts_model": "eleven_turbo_v2_5",
    "client_tts_voice": "56AoDkrOh6qfVPDXZ7Pt",
    "client_tts_clean_model": "gpt-4o-mini",
    "client_stt_model": "nova-3",
    "client_openai_compatible_chat_model": False,
    "client_openai_compatible_base_url": "",
    "client_openai_compatible_api_key": "",
    "client_chat_model": "gpt-4o",
    "client_realtime_model": "gpt-4o-realtime-preview",
    "client_realtime_voice": "echo",
    "client_chat_provider": None
}


def parse(config_file="config.yaml"):
    try:
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)

        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

        debug = config.get('debug')

        logging.basicConfig(
            level=logging.INFO if debug else logging.CRITICAL + 1,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[
                logging.FileHandler("server.log"),
                logging.StreamHandler()
            ]
        )

        if debug:
            df = pd.DataFrame(config.items(), columns=["Parameter", "Value"])

            logging.info("Configuration successfully loaded")
            logging.info("\n=== Configuration ===\n%s", df.to_string(index=False))
            
    except Exception as e:
        logging.error("Error loading configuration: %s", e)
        sys.exit(1)
    
    allowed_pairs = {
        "text": ["text-voice-multimodal", "realtime-multimodal", "realtime-text", "text"],
        "realtime-text": ["text-voice-multimodal", "realtime-multimodal", "text", "realtime-text"],
        "voice": ["text-voice-multimodal", "realtime-multimodal", "realtime-voice", "voice"],
        "realtime-voice": ["text-voice-multimodal", "realtime-multimodal", "voice", "realtime-voice"]
    }
    
    config = {**defaults, **config}

    agent_mode = config.get("agent_mode")

    client_mode_conditional = "text" if agent_mode == "text" else "voice"

    client_mode_config = config.get("client_mode")

    client_mode = client_mode_config if client_mode_config else client_mode_conditional

    config["client_mode"] = client_mode
    
    if client_mode in allowed_pairs:
        if agent_mode not in allowed_pairs[client_mode]:
            logging.error("Incompatible client_mode (%s) and agent_mode (%s)", client_mode, agent_mode)
            sys.exit(1)
    if agent_mode in allowed_pairs:
        if client_mode not in allowed_pairs[agent_mode]:
            logging.error("Incompatible client_mode (%s) and agent_mode (%s)", client_mode, agent_mode)
            sys.exit(1)
    
    if client_mode.startswith("realtime-"):
        if not config.get("client_realtime_model"):
            logging.error("client_realtime_model is required when client_mode starts with 'realtime-'")
            sys.exit(1)
    if agent_mode.startswith("realtime-"):
        if not config.get("agent_realtime_model"):
            logging.error("agent_realtime_model is required when agent_mode starts with 'realtime-'")
            sys.exit(1)
    
    logging.info("Configuration validation passed")
    
    namespace = argparse.Namespace(**config)
    return namespace
