from typing import Literal, List

from pydantic import BaseModel, Field

from worldender.models.choice import Choice
from worldender.models.location import Location
from worldender.models.outcome import Outcome
from worldender.models.player import Player
from worldender.models.world_ender import WorldEnder
from worldender.models.event import Event
from worldender.models.world import World
from worldender.planners.query import QueryPlan


class Scenario(BaseModel):
    slug: str
    world: World
    player: Player
    last_event: Event | None
    last_world_ender: WorldEnder | None
    events: List[Event] = Field(default_factory=list)
    world_enders: List[WorldEnder] = Field(default_factory=list)
    query_plan: QueryPlan | None


class NewScenarioRequest(BaseModel):
    player_name: str
    city: str
    scenario: str


class NewScenarioResponse(BaseModel):
    slug: str
    result: Literal["success", "failure"]
