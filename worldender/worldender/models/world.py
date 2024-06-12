import math
from typing import Optional
from typing_extensions import Literal
from pydantic import BaseModel, Field
from worldender.models.location import Location

CURRENT_WORLD_POP = 8019876189
LOG_MULTIPLIER = 1


class World(BaseModel):
    """
    World for the WorldEnder.ai game.
    The world is a tree of locations.
    The population ticks down according to the log_multiplier, which is set by
    the events in the game.
    """

    current_location: Location = Field(
        None, description="The current location of the player"
    )
    population: int = Field(
        CURRENT_WORLD_POP, description="The population of the world"
    )
    day: int = Field(0, description="The number of days that have passed in the game")
    log_multiplier: int = Field(
        LOG_MULTIPLIER, description="The log multiplier for the population decrease"
    )
    epoch: Literal["Apocalyptic", "Post-Apocalyptic", "Post-Post-Apocalyptic"] = (
        "Apocalyptic"
    )

    def __init__(self, **data):
        super().__init__(**data)

    def tick(self) -> None:
        """ "
        tick the world by one day and decrease the population.
        population := population - population / log(population) * log_multiplier
        """
        self.day += 1
        self.population = math.floor(
            self.population
            - (self.population / math.log(self.population) * self.log_multiplier)
        )
        if self.population < 0:
            self.population = 0
        if self.population < 1000000:
            self.epoch = "Post-Post-Apocalyptic"
        elif self.population < 10000000:
            self.epoch = "Post-Apocalyptic"

    def travel(self, location: Location) -> None:
        """
        travel to a new location.
        """
        self.current_location = location
