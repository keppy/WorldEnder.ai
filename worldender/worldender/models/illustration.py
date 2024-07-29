from typing import List, Literal, Optional
from pydantic import BaseModel, Field


class Illustration(BaseModel):
    """ """

    prompt: str
    negative_prompt: str
    aspect_ratio: str
    image_path: str
    progress: Literal["none", "inprogress", "complete", "failed"] = Field(
        default="none"
    )

    def report(self):
        dct = self.model_dump()
        dct["usage"] = self._raw_response.usage.model_dump()
        return dct
