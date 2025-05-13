## Overview

**Benchforce** is a flexible framework designed for evaluating text-based and voice-based agents, supporting real-time and three-leg interaction scenarios. It emphasizes ease of extensibility and customization for various use cases.

 
## Architecture

The core application components include:

- **WebSocket server**
- **Agent under evaluation**
- **Judge (client agent)**

Both agents (participants) engage in conversations based on a preconfigured agenda.

Participants exchange packets through the WebSocket server. Packets support:

- Streaming and synchronous audio/text generation
- Logging and technical features

This architecture enables concurrent execution of multiple parallel dialogues.

## Running an Evaluation: Walkthrough

When launching the framework, the primary source of configuration is the `config.yaml` file, which defines all parameters related to the evaluation.

Upon startup, the WebSocket server is initialized first. It includes a routing component responsible for directing packets between session participants, ensuring that the session is fully established and both participants — the agent and the judge — are connected.

The server also handles packet logging. As a result, it produces:

* A **text transcript** containing a complete list of all exchanged packets (excluding audio),
* A **full audio recording** of the conversation in `.wav` format.


These files are saved in real time during the conversation and stored in the `history` directory. 


Each participant instance is initialized with configuration data from the selected environment:

#### For the Judge:

* **Agenda** – a textual description of the task goal, which may include identifiers and specific instructions for the conversation.

#### For the Agent (in standalone mode):

* **System prompt**
* **Available function definitions**
* **Database** in JSON format

Each environment contains a set of tasks to be processed by the judge. In addition to the agenda, each task may include:

* **Ground truth answers**
* **Expected function calls** with their respective arguments required to solve the task correctly

These references can also be used for computing database ground truth hash during evaluation.

Once the participant instances are created, the dialogue sessions are initiated either concurrently (multi-threaded) or sequentially, depending on the configuration specified in `config.yaml`. Each session begins with a handshake exchange between participants, after which the conversation proceeds.

After all sessions are completed, the **Evaluator** class is triggered. It performs the following steps:

1. **Per-session scoring** – Calculates evaluation metrics individually for each dialogue using the corresponding session logs and task data.
2. **Aggregation** – Combines the results into a final summary.


## UnifiedPacket

The `UnifiedPacket` class is a core structure in the Benchforce framework, used for communication between agents and the WebSocket server. Packets encapsulate various event types and associated data, supporting real-time streaming and synchronous interactions.

### **Implementation**

```python
import json
from dataclasses import dataclass
from typing import Optional, Dict, Any
from enum import Enum


class EventType(str, Enum):
    BENCHFORCE_HANDSHAKE = "benchforce.handshake"
    BENCHFORCE_TERMINATE = "benchforce.terminate"
    BENCHFORCE_LOG_ORIG_DB = "benchforce.log_original_db"
    BENCHFORCE_LOG_DRYRUN_DB = "benchforce.log_dryrun_db"
    RESPONSE_AUDIO_DELTA = "response.audio.delta"
    RESPONSE_AUDIO_DONE = "response.audio.done"
    RESPONSE_AUDIO_TRANSCRIPT_DONE = "response.audio_transcript.done"
    RESPONSE_TEXT_DONE = "response.text.done"
    RESPONSE_TEXT_DELTA = "response.text.delta"
    RESPONSE_DONE = "response.done"
    RESPONSE_LOG_TTS = "response.log_tts"
    RESPONSE_LOG_STT = "response.log_stt"
    RESPONSE_FUNCTION_CALL = "response.function_call"
    RESPONSE_FUNCTION_CALL_RESULT = "response.function_call_result"
    RESPONSE_ERROR = "response.error"


@dataclass
class UnifiedPacket:
    event: EventType
    audio_delta: Optional[str] = None
    audio: Optional[str] = None
    text: Optional[str] = None
    text_delta: Optional[str] = None
    function_call: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    config: Optional[str] = None
    hash: Optional[str] = None
    tokens: Optional[int] = None

    def to_json(self) -> str:
        return json.dumps(self.__dict__)
```

### **Properties**

| Property        | Type                       | Description                                   |
| --------------- | -------------------------- | --------------------------------------------- |
| `event`         | `EventType`                | Type of the event occurring.                  |
| `audio_delta`   | `Optional[str]`            | Incremental audio data (encoded).             |
| `audio`         | `Optional[str]`            | Final audio data (encoded).                   |
| `text`          | `Optional[str]`            | Complete text response data.                  |
| `text_delta`    | `Optional[str]`            | Incremental text response data.               |
| `function_call` | `Optional[Dict[str, Any]]` | Information about function calls triggered.   |
| `error`         | `Optional[str]`            | Error message, if any.                        |
| `config`        | `Optional[str]`            | Configuration data used for the task.         |
| `hash`          | `Optional[str]`            | Hash identifier of the DB.                    |
| `tokens`        | `Optional[int]`            | Token count used in the event.                |


### **Event Types**

#### **Control Events**

* `benchforce.handshake` – Initializes communication between client and server.
* `benchforce.terminate` – Signals termination of the interaction.

#### **Logging Events**

* `benchforce.log_original_db` – Logs original database hash value.
* `benchforce.log_dryrun_db` – Logs the database hash after functions are executed in dry-run mode.

#### **Response Events**

##### *Audio-related*

* `response.audio.delta` – Streams incremental audio response chunks.
* `response.audio.done` – Indicates completion of audio streaming.
* `response.audio_transcript.done` – Completion of speech-to-text transcript.

##### *Text-related*

* `response.text.delta` – Streams incremental text response chunks.
* `response.text.done` – Indicates the final text response completion.

##### *General Completion*

* `response.done` – General signal indicating completion of a response process.

##### *Logging of Speech Processing** (used for evaluating the accuracy and performance of TTS and STT models)*

* `response.log_tts` – Logs Text-to-Speech generation details.
* `response.log_stt` – Logs Speech-to-Text transcription details.

##### *Function Call Handling*

* `response.function_call` – Logs the function call along with the parameters used.
* `response.function_call_result` – Logs the result of the function execution.

##### *Error Handling*

* `response.error` – Indicates an error occurred during processing.

<br>

## Quick Start  

### 1. Install Dependencies  
Install the required dependencies using:  
```bash  
pip install .  
# or  
python setup.py install  
```
Make sure that `ffmpeg` is installed on your system and available in your system PATH. It is required for audio processing.


### 2. Set Environment Variables  
Use the `.env.example` file as a reference to create your own `.env` file with the required environment variables.

### 3. Run Evaluation for the Test Environment  
To start the evaluation, run:  
```bash
python run.py
```

## Supported Models

### Real-Time Agent

#### Multimodal Models
- **OpenAI**: `gpt-4o-realtime-preview`
- **Google**: `gemini-2.0-flash-exp`

### Pipelined Agent

#### LLMs
- **OpenAI** – `gpt-4o`, `gpt-4o-mini`, `gpt-4.5-preview`
- **Google** – `gemini-2.0-flash-001`, `gemini-2.5-pro-preview-03-25`  
- **xAI** – `grok-2-1212`, `grok-2-latest`  
- **Anthropic** – `claude-3-7-sonnet-20250219`, `claude-3-5-sonnet-20241022`  
- **Meta** – `meta-llama/Llama-4-Scout-17B-16E-Instruct`, `meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8`  
- **OpenAI compatible** - You can use any model compatible with the OpenAI SDK by specifying the following parameters in the configuration file:
```yaml
agent_openai_compatible_chat_model: false
agent_openai_compatible_base_url: ""
agent_openai_compatible_api_key: ""
agent_chat_model: ""
```

#### TTS (Text-to-Speech)

* **Cartesia**: `sonic`

#### STT (Speech-to-Text)

* **Deepgram**: `nova-3`

<br>

## Configuration

The behavior of the evaluation framework is controlled via the `config.yaml` file. Below is a complete list of supported configuration options:

### General Settings

| Parameter         | Type   | Description                                                                                     |
| ----------------- | ------ | ----------------------------------------------------------------------------------------------- |
| `debug`           | `bool` | Enables debug logging and verbose output.                                                       |
| `environment`     | `str`  | Name of the environment to evaluate (e.g., `"appointments_management"`).                        |
| `entries`         | `list` | List of task entry indices to process. Use `[-1]` to run all available entries.                 |
| `metrics`         | `list` | List of metric names to use (e.g., `["accuracy"]`).                                             |
| `task_iterations` | `int`  | Number of times to repeat each task.                                                            |
| `num_threads`     | `int`  | Maximum number of concurrent tasks.                                                             |
| `max_turns`       | `int`  | Maximum number of dialogue turns per session.                                                   |


### Agent Configuration

| Parameter                            | Type            | Description                                                                                         |
| ------------------------------------ | --------------- | --------------------------------------------------------------------------------------------------- |
| `agent_mode`                         | `str`           | Agent operation mode. Supported values: `"text"`, `"realtime-text"`, `"realtime-voice"`. |
| `agent_chat_model`                   | `str`           | Chat model to use in text mode (e.g., `"gpt-4o"`).                                                 |
| `agent_chat_provider`                | `str` or `null` | Optional: name of the external provider if not using OpenAI or local setup.                         |
| `agent_openai_compatible_chat_model` | `bool`          | Whether to use a custom OpenAI-compatible model.                                                    |
| `agent_openai_compatible_base_url`   | `str`           | Base URL for the OpenAI-compatible endpoint.                                                        |
| `agent_openai_compatible_api_key`    | `str`           | API key for the OpenAI-compatible endpoint.                                                         |


### Agent Voice Settings

| Parameter               | Type  | Description                                                                        |
| ----------------------- | ----- | ---------------------------------------------------------------------------------- |
| `agent_tts_model`       | `str` | Model used for text-to-speech (TTS), e.g., `"sonic"`.                              |
| `agent_tts_voice`       | `str` | Voice ID for TTS output.                                                           |
| `agent_tts_clean_model` | `str` | Post-processing model for cleaning TTS responses (e.g., `"gpt-4o-mini"`).          |
| `agent_stt_model`       | `str` | Speech-to-text (STT) model used to transcribe audio input.                         |


### Realtime Agent Settings

| Parameter              | Type  | Description                               |
| ---------------------- | ----- | ----------------------------------------- |
| `agent_realtime_model` | `str` | Realtime model for streaming interaction. |
| `agent_realtime_voice` | `str` | Voice ID used in realtime mode.           |


### Audio Processing (Client & Server)

| Parameter            | Type    | Description                                                      |
| -------------------- | ------- | ---------------------------------------------------------------- |
| `sample_rate`        | `int`   | Audio sample rate (e.g., `24000`).                               |
| `chunk_size_ms`      | `int`   | Audio processing chunk size in milliseconds.                     |
| `cutoff_freq`        | `int`   | Low-pass filter cutoff frequency (Hz), `0` means no filter.      |
| `clipping_threshold` | `float` | Amplitude clipping threshold, `0` means no clipping.             |
| `drop_probability`   | `float` | Probability of randomly dropping chunks to simulate packet loss. |
| `snr_db`             | `float` | Signal-to-noise ratio for synthetic noise injection.             |
| `noises`             | `list`  | List of background noise files to be used.                       |
| `noise_volume`       | `int`   | Volume level of the noise (relative scale).                      |


## Noise Effects and Audio Distortion

The **`NoiseMixer`** module applies various noise effects and distortions to audio data, useful for robustness evaluation or simulating real-world acoustic environments.

Available effects and parameters:

#### 1. Background Noise Overlay

Adds predefined noise samples to the audio.

**Parameters:**

* `noises`: List of noise filenames from `/src/classes/noises`.
* `noise_volume`: Noise volume (0–10).

#### 2. Low-Pass Filtering

Simulates bandwidth-limited channels.

**Parameters:**

* `cutoff_freq`: Frequency cutoff in Hz.

#### 3. Clipping

Limits audio amplitude.

**Parameters:**

* `clipping_threshold`: Amplitude threshold (0–1).

#### 4. Gaussian Noise Addition

Adds white Gaussian noise at specified SNR.

**Parameters:**

* `snr_db`: Signal-to-noise ratio in dB.

#### 5. Packet Loss Simulation

Simulates audio packet loss or errors.

**Parameters:**

* `drop_probability`: Probability of dropping chunks (0–1).
* `chunk_size_ms`: Chunk size in milliseconds.


## Adding Custom Metrics

To add new metrics, you need to create a file under the `src/metrics` directory. The file name must match the name of the implemented class. For example, for a class named `Accuracy`, the file should be named `accuracy.py`.

The class implementation must contain two `@staticmethod`s:

```python
@staticmethod
def calculate(session_id: str, entry, **kwargs):
```

This method receives the session ID and task-specific information via the `entry` parameter, which may include the prompt (e.g., a judge’s agenda), expected function calls, and other related data.

The framework provides helper functions to simplify implementation:

* `Helper.read_transcript(session_id)` – retrieves the session transcript.
* `Helper.parse_turns(transcript, with_timestamp=True)` – parses the transcript into structured turns, optionally including timestamps.

The `calculate` method should return a dictionary containing any relevant computed values.

The second required method is:

```python
@staticmethod
def aggregate(results):
```

This method receives a list of dictionaries returned by `calculate` and should return a pandas `DataFrame` that aggregates and summarizes the results.

To enable the custom metric, specify the file name (without the `.py` extension) in the `metrics` field of your `config.yaml` file.

