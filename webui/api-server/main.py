import logging
from dotenv import load_dotenv
from worldender.agents.gm import GameMaster, Move
from worldender.models.game_plan import GamePlan
from worldender.models.question import Question
from worldender.models.question_response import QuestionResponse
from .illustrate import gen_illustrate

load_dotenv()

import openai
import instructor
from fastapi import Body, FastAPI, Request, BackgroundTasks
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from worldender.models.location import Location
from worldender.models.world_ender import WorldEnder
from worldender.simulation import (
    ask_question,
    get_game_plan,
    next_event,
    next_world_ender,
    query_gm,
)
from .dtos import (
    Choice,
    GMResponse,
    GMRequest,
    NewIllustrationRequest,
    NewIllustrationResponse,
    NewScenarioRequest,
    NewScenarioResponse,
    Event,
    Player,
    Scenario,
    World,
)
from .util import gen_illustration_id, gen_scenario_id
from .error_handling import *
from .storage import *

# this gives a lot of detail from openai, instructor and pymongo
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = FastAPI()
aclient = instructor.patch(openai.AsyncOpenAI())

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


@app.post("/gm/query", response_model=GMResponse)
async def gm_query(data: GMRequest) -> GMResponse:
    gm = query_gm(data.query, gm)
    return GMResponse(game_master=gm)


@app.post("/scenario/new", response_model=NewScenarioResponse)
async def new_scenario(scenario_init: NewScenarioRequest) -> NewScenarioResponse:
    (slug, id) = gen_scenario_id(scenario_init)
    scenario = Scenario(
        slug=slug,
        world=World(current_location=Location(latitude=0, longitude=0)),
        player=Player(name=scenario_init.player_name, city=scenario_init.city),
        last_event=None,
        last_world_ender=None,
        question_response=None,
        final_population=None,
        Outcome=None,
    )
    event = await next_event(
        f"{scenario_init.city},  {scenario_init.scenario}", aclient
    )
    logger.info(f"Got event: {event}")
    scenario.last_event = event
    scenario.events.append(event)
    await store_scenario(id, scenario)
    return NewScenarioResponse(slug=slug, result="success")


@app.get("/scenario/{scenario_id}", response_model=Scenario)
async def get_scenario(scenario_id: str):
    scenario = await fetch_scenario(scenario_id)
    return scenario


@app.post("/scenario/{scenario_id}/choose", response_model=Scenario)
async def choose(scenario_id: str, choice: Choice):
    scenario = await fetch_scenario(scenario_id)
    logger.info(f"Choosing {choice.choice[:10]} for scenario {scenario_id}")
    world_ender: WorldEnder = await next_world_ender(choice.choice, aclient)
    logger.info(f"Got WorldEnder: {world_ender}")
    scenario.last_world_ender = world_ender
    scenario.world_enders.append(world_ender)
    await store_scenario(scenario_id, scenario)
    return scenario


@app.post("/scenario/{scenario_id}/tick", response_model=Scenario)
async def tick(scenario_id: str):
    scenario = await fetch_scenario(scenario_id)
    logger.info(f"Ticking scenario {scenario_id}")
    scenario.world.tick()
    await store_scenario(scenario_id, scenario)
    return scenario


@app.post("/gameplan/{scenario_id}", response_model=Scenario)
async def post_game_plan(scenario_id: str) -> GamePlan:
    scenario = await fetch_scenario(scenario_id)
    logger.info(f"Getting game plan for scenario {scenario_id}")
    game_plan: GamePlan = await get_game_plan(
        scenario.last_world_ender.description, aclient
    )
    logger.info(f"Got game plan: {game_plan}")
    return game_plan


@app.post("/question/{scenario_id}", response_model=QuestionResponse)
async def post_ask_question(scenario_id: str, data: Question) -> QuestionResponse:
    scenario = await fetch_scenario(scenario_id)
    logger.info(f"Asking question {data.text} for scenario {scenario_id}")
    question_response = await ask_question(
        data.text, aclient, scenario.last_world_ender
    )
    logger.info(f"Got question response: {question_response}")
    if question_response.correct_question:
        scenario.final_population = scenario.world.population
    scenario.question_response = question_response
    await store_scenario(scenario_id, scenario)
    return question_response


@app.post("/illustration/new", response_model=NewIllustrationResponse)
async def new_illustration(
    req: NewIllustrationRequest, bgtasks: BackgroundTasks
) -> NewIllustrationResponse:
    id = gen_illustration_id()
    illustration = Illustration(
        prompt=req.prompt,
        negative_prompt=req.negative_prompt,
        aspect_ratio=req.aspect_ratio,
        image_path="",
        progress="inprogress",
    )

    await store_illustration(id, illustration)

    # specifically dont await this
    bgtasks.add_task(
        gen_illustrate,
        id,
        req.prompt,
        negative_prompt=req.negative_prompt,
        aspect_ratio=req.aspect_ratio,
    )
    return NewIllustrationResponse(id=id, result=illustration)


@app.get("/illustration/{illustration_id}")
async def get_illustration(illustration_id: str):
    illustration = await fetch_illustration(illustration_id)
    del illustration.image_path
    return illustration


@app.get("/illustration/{illustration_id}/image")
async def get_illustration_image(illustration_id: str):
    illustration = await fetch_illustration(illustration_id)
    if illustration.progress != "complete":
        raise NotFoundException(f"Illustration with id {illustration_id} not ready")
    return FileResponse(illustration.image_path, media_type="image/png")


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
