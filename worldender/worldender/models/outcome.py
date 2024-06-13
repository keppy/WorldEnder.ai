from __future__ import annotations
from pydantic import BaseModel, Field


class Outcome(BaseModel):
    """
    Outcome is the likely outcome from an Event, taking into account
    recent developments in obscure wars, as we believe their impact
    is more nuanced and far reaching than the government realizes.
    """

    description: str = Field(
        description="An unlikely but scary outcome description, one we didn't see coming"
    )

    def report(self):
        dct = self.model_dump()
        dct["usage"] = self._raw_response.usage.model_dump()
        return dct
