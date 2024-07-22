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

    building: str = Field(
        description="The description of the building including the type and name"
    )


class Research(BaseModel):
    """
    Research is a possible action that the player can take
    """

    research: str = Field(
        description="The description of the research including the field and name"
    )


class GameMaster(BaseModel):
    """
    GameMaster is the main class for the game master, who controls the game
    mainly, he controls what is done with the input from the player
    """

    cot: str = Field(
        "chain of thought", description="The chain of thought that led to the decision"
    )
    action: Union[Move, Build, Research] = Field(
        description="The action that the player can take"
    )

    def roll_d_20(self):
        """
        roll_d_20 rolls a 20 sided die to determine the outcome of the action
        """
        return random.randint(1, 20)


def build_query(s: str) -> str:
    """
    build_query takes a string and returns a query string
    """
    return f"The player is sending you a query. You are the game master. The query is: {s}. Pick the correct action to return and give good reasoning why."
