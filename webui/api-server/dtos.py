from typing import Literal, List

from pydantic import BaseModel, Field

from worldender.models.player import Player
from worldender.models.world_ender import WorldEnder
from worldender.models.event import Event
from worldender.models.world import World


class Scenario(BaseModel):
    slug: str
    world: World
    player: Player
    last_event: Event | None
    last_world_ender: WorldEnder | None
    events: List[Event] = Field(default_factory=list)
    world_enders: List[WorldEnder] = Field(default_factory=list)


class NewScenarioRequest(BaseModel):
    player_name: str
    city: str
    scenario: str


class NewScenarioResponse(BaseModel):
    slug: str
    result: Literal["success", "failure"]


class Choice(BaseModel):
    choice: str
    predefined_index: int | None
