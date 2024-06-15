from typing import List
from pydantic import BaseModel, Field

class GamePlan (BaseModel):
    '''
    A plan of action
    '''
    query_hints: List[str] = Field(description="A list of hints to help the player, these hints would make good queries for figuring out the game plan's goal")
    goal: str = Field(description="The goal of the game plan, the thing the player needs to find to progress the game") 