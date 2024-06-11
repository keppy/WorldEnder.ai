from fastapi import FastAPI
from worldender import models
from .dtos import NewScenarioResponse
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/scenario/new", response_model=NewScenarioResponse)
async def new_scenario(event: models.Event):
    return {"result": "success"}