import logging
from pymongo import MongoClient
from worldender.models.illustration import Illustration
from .dtos import Scenario
from .error_handling import *
from .util import get_id_from_slug

import motor.motor_asyncio
from bson.objectid import ObjectId

logger = logging.getLogger(__name__)

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017/")
db = client["worldender"]
scenarios_collection = db["scenarios"]
illustrations_collection = db["illustrations"]

# Insert a Pydantic object


async def fetch_scenario(slug: str) -> Scenario:
    id = get_id_from_slug(slug)
    logger.info(f"fetching scenario with id {id}")
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


async def fetch_illustration(id: str) -> Illustration:
    dict = await illustrations_collection.find_one({"_id": ObjectId(id)})
    if dict:
        return Illustration(**dict)
    else:
        raise NotFoundException(f"Illustration with id {id} not found")


async def store_illustration(id: str, illustration: Illustration):
    logger.info(f"storing illustration with id {id}")
    dict = illustration.model_dump()
    result = await illustrations_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": dict}, upsert=True
    )
    if result.modified_count == 1 or result.upserted_id is not None:
        return True
    else:
        raise UnknownException(f"Failed to store illustration with id {id}")


sync_client = MongoClient("mongodb://localhost:27017")
sync_db = sync_client.worldender
sync_illustrations_collection = sync_db["illustrations"]


def store_illustration_filepath(id: str, file_name: str):
    logger.info(f"storing illustration filepath with id {id}")
    result = sync_illustrations_collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": {"image_path": file_name, "progress": "complete"}},
    )
    if result.modified_count == 1 or result.upserted_id is not None:
        return True
    else:
        raise UnknownException(f"Failed to store illustration with id {id}")


def store_illustration_error(id: str):
    logger.info(f"storing illustration filepath with id {id}")
    result = sync_illustrations_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": {"progress": "failed"}}
    )
    if result.modified_count == 1 or result.upserted_id is not None:
        return True
    else:
        raise UnknownException(f"Failed to store illustration with id {id}")
