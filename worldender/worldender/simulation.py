import openai
import instructor
from .models.event import Event
from .config import app_config
from datetime import date


async def next_event(player_choice: str) -> Event:
    cfg = app_config
    aclient = instructor.patch(openai.AsyncOpenAI())
    print(f"calling llm: {player_choice}")
    return await aclient.chat.completions.create(
        model=cfg.llm_model,
        temperature=cfg.llm_temp,
        response_model=Event,
        messages=[
            {
                "role": "system",
                "content": f"You are WorldEnder.ai, the date is {date.today()}, you work with a human to predict the World Ender event/events. Use real locations for cities and countries.",
            },
            {"role": "user", "content": f"{player_choice}"},
        ],
        max_retries=3,
    )

async def end_world(query: str) -> Event:
    cfg = app_config
    aclient = instructor.patch(openai.AsyncOpenAI())
    print(f"calling llm: {query}")
    return await aclient.chat.completions.create(
        model=cfg.llm_model,
        temperature=cfg.llm_temp,
        response_model=Event,
        messages=[
            {
                "role": "system",
                "content": f"You are WorldEnder.ai, the date is {date.today()}, you work with a human to predict the World Ender event/events. Use real locations for cities and countries.",
            },
            {"role": "user", "content": f"{query} using this context:"},
        ],
        max_retries=3,
    )