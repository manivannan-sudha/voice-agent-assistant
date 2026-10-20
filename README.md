# voice-agent-assistant

A real-time, multilingual voice AI agent built with [LiveKit Agents](https://docs.livekit.io/agents/) and [Sarvam AI](https://www.sarvam.ai/) (speech-to-text, LLM, and text-to-speech for Indian languages).

## Status

**v1 (this stage):** a working conversational voice agent — speak into a LiveKit room, the agent transcribes with Sarvam STT, reasons with a Sarvam LLM, and replies out loud with Sarvam TTS. Understands English and Hindi (including code-mixed speech).

**v2 (next):** a concrete use case on top of the same pipeline (tool-calling against a mock booking/ordering backend) — TBD.

## Stack

- **STT:** Sarvam `saaras:v4`
- **LLM:** Sarvam `sarvam-105b` (OpenAI-compatible)
- **TTS:** Sarvam `bulbul:v3`
- **Orchestration:** LiveKit Agents (turn-taking, VAD via Silero, realtime audio pipeline)

## Setup

1. **Python deps**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Credentials** — copy `.env.example` to `.env` and fill in:
   - `SARVAM_API_KEY` from https://dashboard.sarvam.ai
   - `LIVEKIT_URL`, `LIVEKIT_API_KEY`, `LIVEKIT_API_SECRET` from a LiveKit Cloud project at https://cloud.livekit.io

3. **Download the VAD model** (one-time, required by the LiveKit CLI):
   ```bash
   python src/agent.py download-files
   ```

4. **Run the agent** in dev mode:
   ```bash
   python src/agent.py dev
   ```

5. **Talk to it** — open the [LiveKit Agents Playground](https://agents-playground.livekit.io), connect to your project, and join the room the agent is running in.

## Project layout

```
src/agent.py       # agent entrypoint: STT/LLM/TTS wiring and turn-taking config
requirements.txt   # Python dependencies
.env.example        # required environment variables
```
