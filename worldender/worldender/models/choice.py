from pydantic import BaseModel, Field


class Choice(BaseModel):
    """
    Choice is a possible choice to make in response to an Event
    This choice will have an impact on the world and how the story progresses
    It could lead to the world ending sooner, or later
    """

    choice: str = Field(description="The choice to make in response to the event")
    consequence: str = Field(
        description="The outcome of the choice made in response to the event"
    )

    def report(self):
        dct = self.model_dump()
        dct["usage"] = self._raw_response.usage.model_dump()
        return dct
