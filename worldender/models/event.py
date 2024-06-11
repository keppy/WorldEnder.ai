from pydantic import BaseModel, Field
from typing import List
from .outcome import Outcome

class Event(BaseModel):
    '''
    Event is a possilbe World Ending event, with a list of possible outcomes
    country and city fields should represent a real location
    '''
    country: str = Field(description="The country where the apocolyptic event is happening")
    city: str = Field(description="The city where the predicted pivitol event is happening")
    description: str = Field(description="A two to three sentance description of the event and its outcome")
    possible_outcomes: List[Outcome] = Field(description="three to five possible outcomes that are influenced by the location of this event")

    def report(self):
        dct = self.model_dump()
        dct["usage"] = self._raw_response.usage.model_dump()
        return dc
