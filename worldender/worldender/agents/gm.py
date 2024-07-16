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
    actions: Union[Move,] = Field(description="The actions that the player can take")
