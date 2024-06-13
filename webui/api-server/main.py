import logging
from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from worldender.models.location import Location
from worldender.simulation import next_event
from .dtos import (
    Choice,
    NewScenarioRequest,
    NewScenarioResponse,
    Event,
    Player,
    Scenario,
    World,
)
from .util import gen_scenario_id
from .error_handling import *
from .storage import *

# this gives a lot of detail from openai, instructor and pymongo
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello WorldEnder!"}


@app.post("/scenario/new", response_model=NewScenarioResponse)
async def new_scenario(scenario_init: NewScenarioRequest) -> NewScenarioResponse:
    (slug, id) = gen_scenario_id(scenario_init)
    scenario = Scenario(
        slug=slug,
        world=World(current_location=Location(latitude=0, longitude=0)),
        player=Player(name=scenario_init.player_name, city=scenario_init.city),
        last_event=None,
    )
    event = await next_event(scenario_init.scenario)
    logger.info(f"Got event: {event}")
    scenario.last_event = event
    await store_scenario(id, scenario)
    return NewScenarioResponse(slug=slug, result="success")


@app.get("/scenario/{scenario_id}", response_model=Scenario)
async def get_scenario(scenario_id: str):
    scenario = await fetch_scenario(scenario_id)
    return scenario


@app.post("/scenario/{scenario_id}/choose", response_model=Scenario)
async def choose(scenario_id: str, choice: Choice):
    scenario = await fetch_scenario(scenario_id)
    logger.info(f"Choosing {choice} for scenario {scenario_id}")
    event: Event = await next_event(choice.choice)
    logger.info(f"Got event: {event}")
    scenario.last_event = event
    await store_scenario(scenario_id, scenario)
    return scenario


@app.post("/scenario/{scenario_id}/tick", response_model=Scenario)
async def tick(scenario_id: str):
    scenario = await fetch_scenario(scenario_id)
    logger.info(f"Ticking scenario {scenario_id}")
    scenario.world.tick()
    await store_scenario(scenario_id, scenario)
    return scenario


@app.exception_handler(CanonicalException)
async def canonical_exception_handler(request: Request, exc: CanonicalException):
    logger.info(f"Caught exception: {exc}")
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": str(exc),
            "details": exc.details,
        },
    )
