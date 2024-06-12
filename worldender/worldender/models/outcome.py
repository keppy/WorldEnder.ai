from __future__ import annotations
from pydantic import BaseModel, Field
from typing import List


class Outcome(BaseModel):
    """
    Outcome is the likely outcome from an Event, taking into account
    recent developments in obscure wars, as we believe their impact
    is more nuanced and far reaching than the government realizes.
    """

    description: str = Field(
        description="An unlikely but scary outcome description, one we didn't see coming"
    )
    consequence: str = Field(
        description="The price that must be paid for progress. This is casualties, deaths, or other tragedies."
    )
    choices: List[str] = Field(
        description="A List of choices; only one of them will keep the world from ending"
    )
    outcomes: List[str] = Field(
        description="A list of three outcomes; two are world ending outcomes and one keeps the world going"
    )

    def report(self):
        dct = self.model_dump()
        dct["usage"] = self._raw_response.usage.model_dump()
        return dct
