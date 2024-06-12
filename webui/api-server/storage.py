from .dtos import Scenario
from .error_handling import *
from .util import get_id_from_slug

import motor.motor_asyncio
from bson.objectid import ObjectId

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017/")
db = client["worldender"]
scenarios_collection = db["scenarios"]

# Insert a Pydantic object


async def fetch_scenario(slug: str) -> Scenario:
    id = get_id_from_slug(slug)
    print(f"fetching scenario with id {id}")
    dict = await scenarios_collection.find_one({"_id": ObjectId(id)})
    if dict:
        return Scenario(**dict)
    else:
        raise NotFoundException(f"Scenario with id {id} not found")


async def store_scenario(id: str, scenario: Scenario):
    dict = scenario.model_dump()
    id = get_id_from_slug(scenario.slug)
    result = await scenarios_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": dict}, upsert=True
    )
    if result.modified_count == 1 or result.upserted_id is not None:
        return True
    else:
        raise UnknownException(f"Failed to store scenario with id {id}")
