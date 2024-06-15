from pydantic import BaseModel, Field

class Question(BaseModel):
    text: str = Field(description="The text of the question to ask")