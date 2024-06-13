from datetime import date
from urllib.request import urlopen

from bs4 import BeautifulSoup
import instructor
import openai

from .models.event import Event
from .models.world_ender import WorldEnder
from .config import app_config


def getContext(url: str) -> str:
    html_content = urlopen(url)
    soup = BeautifulSoup(html_content, "html.parser")
    sorted_stripped_and_deduped = list(dict.fromkeys(soup.stripped_strings))
    context = str.join(", ",sorted_stripped_and_deduped)
    return context

async def next_event(player_choice: str, aclient: openai.Client) -> Event:
    """
    This function calls the OpenAI API to generate the next event based on the player's choices.
    Construct a chain of thought using choices, consequences, and events.
    """
    cfg = app_config
    context_url = "https://www.aljazeera.com/"
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
            {"role": "user", "content": f"{player_choice} using this as context: {getContext(context_url)}"},
        ],
        max_retries=3,
    )

async def next_world_ender(query: str, aclient: openai.Client) -> Event:
    cfg = app_config
    context_url = "https://www.bbc.com/news/world"
    aclient = instructor.patch(openai.AsyncOpenAI())
    print(f"calling llm: {query}")
    return await aclient.chat.completions.create(
        model=cfg.llm_model,
        temperature=cfg.llm_temp,
        response_model=WorldEnder,
        messages=[
            {
                "role": "system",
                "content": f"You are WorldEnder.ai, the date is {date.today()}, return a detailed description of how this world ends and how humans continue existing. death_toll and survival_rate properties should be logical according to the way the world is ending.",
            },
            {"role": "user", "content": f"{query} using this context:{getContext(context_url)}"},
        ],
        max_retries=3,
    )