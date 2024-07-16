from pydantic import BaseModel, Field
from typing import List
from .choice import Choice


class Event(BaseModel):
    """
    Event is a possible World Ending event, with a list of possible outcomes
    country and city fields should represent a real location
    """

    country: str = Field(
        description="The country where the apocalyptic event is happening"
    )
    city: str = Field(
        description="The city where the predicted pivotal event is happening"
    )
    description: str = Field(
        description="A two to three sentence description of the event and its outcome"
    )
    possible_choices: List[Choice] = Field(
        description="Three possible choices to take in reaction to this event, which will dictate the next event in the world"
    )

    def report(self):
        dct = self.model_dump()
        dct["usage"] = self._raw_response.usage.model_dump()
        return dct
