import logging

from dotenv import load_dotenv

from livekit import agents
from livekit.agents import Agent, AgentSession, RoomInputOptions
from livekit.plugins import sarvam, silero

load_dotenv()

logger = logging.getLogger("voice-agent")


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions=(
                "You are a friendly, concise voice assistant speaking with a user "
                "over a live call. Keep replies short and natural, as if spoken "
                "aloud. You can understand and respond in English or Hindi, "
                "matching whichever language the user speaks."
            )
        )


async def entrypoint(ctx: agents.JobContext) -> None:
    await ctx.connect()

    session = AgentSession(
        stt=sarvam.STT(
            model="saaras:v4",
            language="hi-IN",  # auto-handles code-mixed Hindi/English input
        ),
        llm=sarvam.LLM(model="sarvam-105b"),
        tts=sarvam.TTS(
            model="bulbul:v3",
            target_language_code="en-IN",
            speaker="shubh",
        ),
        vad=silero.VAD.load(),
        turn_detection="stt",
    )

    await session.start(
        agent=Assistant(),
        room=ctx.room,
        room_input_options=RoomInputOptions(),
    )


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
