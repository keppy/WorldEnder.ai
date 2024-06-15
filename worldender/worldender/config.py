import os
from pydantic import BaseModel


class AppConfig(BaseModel):
    llm_model: str
    llm_temp: float


app_config = AppConfig(
    llm_model=os.environ.get("LLM_MODEL", "gpt-4o"),
    llm_temp=float(os.environ.get("LLM_TEMP", 0.85)),
)
