from pydantic import BaseModel, Field
from typing import List

class Choice(BaseModel):
    """
    Choice is a possible choice to make in response to an Event
    """
    choice: str = Field(
        description="The choice to make in response to the event"
    )
    consequence: str = Field(
        description="A description of the choice and its consequences"
    )

    def report(self):
        return self.model_dump()