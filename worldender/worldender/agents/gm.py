import random
from pydantic import BaseModel, Field
from typing import List, Union


class Move(BaseModel):
    """
    Move is a possible action that the player can take
    """

    destination: str = Field(description="The name of the destination city")


class Build(BaseModel):
    """
    Build is a possible action that the player can take
    """

    building: str = Field(description="The name of the building")


class Research(BaseModel):
    """
    Research is a possible action that the player can take
    """

    research: str = Field(description="The name of the type of research")


class Warfare(BaseModel):
    """
    Warfare is a possible action that the player can take
    """

    warfare: str = Field(description="The name of the type of warfare")


class GameMaster(BaseModel):
    """
    GameMaster is the main class for the game master, who controls the game
    mainly, he controls what is done with the input from the player
    """

    cot: str = Field(
        "chain of thought", description="The chain of thought that led to the decision"
    )
    action: Union[Move, Build, Research, Warfare] = Field(
        description="The action that the player can take"
    )

    def roll_d_20(self):
        """
        roll_d_20 rolls a 20 sided die to determine the outcome of the action
        """
        return random.randint(1, 20)


SCENARIO_PROMPT = "Make up a scenario that the player must face and react to in response to the action they took"
CHALLENGE_PROMPT = (
    "Make up a challenge for the player that they must roll a d20 to overcome"
)
OUTCOME_PROMPT = "Make up an outcome for the player based on the scenario they faced, the action they took, and the challenge they faced"
