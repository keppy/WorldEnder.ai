from pydantic import BaseModel, Field


class QuestionResponse(BaseModel):
    """
    A response to a question about the world ending event. There is a correct question to ask that will reveal hidden information in the game.
    """

    correct_question: bool = Field(
        description="Indicate if this was the correct question to ask"
    )
    response: str = Field(description="The response to the question")
