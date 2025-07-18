# Benchforce

Benchforce is a flexible, extensible framework for evaluating text- and voice-based agents in real time or multi-leg scenarios. It supports:

- Multiple interaction modes (text, real-time speech, multi-turn dialogues)
- Third-party and custom models (OpenAI, Google Gemini, xAI Grok, Anthropic Claude, Meta Llama, etc.)
- Streaming audio/text with fine-grained function-call instrumentation
- Comprehensive packet logging (JSONL transcripts, full `.wav` recordings)
- Built-in metrics (accuracy, latency, custom, etc) and easy metric-plugging

---

## Quick Start

### 1. Clone & configure

```bash
git clone git@github.com:SalesforceAIResearch/benchforce.git
cd benchforce
```

Edit `config.yaml` to choose:

- **environment** (e.g. `"appointments_management"`)
- **entries** (`[-1]` = all tasks, or list of indices)
- **metrics** (e.g. `["accuracy"]`)
- **agent models** and **voice settings**
- **threading**, **max turns**, **noise**, etc.

Copy `.env.example` to `.env` and fill in relevant API keys, such as `ELEVENLABS_API_KEY` or `OPENAI_API_KEY`.

Create a Python environment:

```bash
uv venv --python 3.12
source .venv/bin/activate
uv pip install -r requirements.txt
```

### 2. Run Benchforce

```bash
python run.py --agent openai
```

### 4. Results

High-level results are displayed in a text box:

```
┌──────────────────────────────────────────────┐
│ Evaluation results:                          │
│           metric        parameter      value │
│ accuracy         Total Test Cases          3 │
│ accuracy                 Accuracy 100% (3/3) │
└──────────────────────────────────────────────┘
```

### 4. More Options

Re-run a previous run to fill in any gaps:

```bash
# Re-run the given runner_id with the current setup in config.yaml
# Note that the given runner_id must still have files on your computer from a previous run.
python run.py --runner_id SOME_EXISTING_RUNNER_ID
```

Specify entries to run (overrides config.yaml):

```bash
python run.py --entry_nums 10 11 12
```

Verbose logging:

```bash
LOG_LEVEL=DEBUG python run.py
```

Specific verbose logging (capitalized logger names):

```bash
LOG_LEVEL_DEEPGRAMSTT=DEBUG \
LOG_LEVEL_ELEVENLABSTTS=DEBUG \
    python run.py --skip_upload
```

---
