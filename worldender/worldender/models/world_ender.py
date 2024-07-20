from pydantic import BaseModel, Field


class WorldEnder(BaseModel):
    """
    An apocalyptic event that the human race, and likely the world, cannot come back from.
    This will likely be a nuclear event. The consequences will likely be long term fallout.
    The class should tell the story of how we got here and why these things happened.
    """

    kind: str = Field(
        description="What kind of world ending event was this? (astrological, biological, war, etc.)"
    )
    description: str = Field(
        description="A detailed description of what happened, including the Events and Outcomes involved"
    )
    death_toll: str = Field(
        description="The total estimated cost of human life as a readable number example: 1bil"
    )
    survival_rate: float = Field(
        description="The percentage chance that any humans will survive the world ending event",
        ge=0.0,
        le=1.0,
    )

    def report(self):
        dct = self.model_dump()
        dct["usage"] = self._raw_response.usage.model_dump()
        return dct
