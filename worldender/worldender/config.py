import os
from pydantic import BaseModel


class AppConfig(BaseModel):
    llm_model: str
    llm_temp: float
    stabilityai_api_key: str
    illustration_path: str


app_config = AppConfig(
    llm_model=os.environ.get("LLM_MODEL", "gpt-4-turbo"),
    llm_temp=float(os.environ.get("LLM_TEMP", 0.2)),
    stabilityai_api_key=os.environ.get("STABILITYAI_API_KEY", ""),
    illustration_path=os.environ.get("ILLUSTRATION_PATH", "/tmp"),
)
