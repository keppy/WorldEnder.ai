from typing import Literal
# from worldender.models import Event, Outcome, Player

from pydantic import BaseModel, Field

class NewScenarioResponse(BaseModel):
    result: Literal["success", "failure"]