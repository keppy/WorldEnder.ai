import time
import hashlib
import random
import re
import unicodedata
import uuid
from .dtos import NewScenarioRequest


def gen_scenario_id(req: NewScenarioRequest) -> tuple[str, str]:
    """Generate a pseudo-unique string based on a random number and current time."""

    random_number = random.randint(100000, 999999)
    combined_string = f"{random_number}{time.time()}"
    hash_object = hashlib.sha256(combined_string.encode())
    hex_dig = hash_object.hexdigest()
    slug = f"{create_slug(req.scenario[0:20])}-{hex_dig[0:10]}"
    hash_slug = hashlib.sha256(slug.encode())

    return slug, hash_slug.hexdigest()[0:24]


def gen_illustration_id() -> str:
    # return guid in string form
    return str(uuid.uuid4()).replace("-", "")[0:24]


def get_id_from_slug(slug: str) -> str:
    """Get the id from a slug."""
    return hashlib.sha256(slug.encode()).hexdigest()[0:24]


def create_slug(text: str) -> str:
    # Normalize the text to decompose combined characters into their base and diacritic parts
    text = unicodedata.normalize("NFKD", text)
    # Encode to ASCII bytes, ignore non-ASCII characters, and decode back to string
    text = text.encode("ascii", "ignore").decode("ascii")
    # Convert to lowercase
    text = text.lower()
    # Remove any remaining unwanted characters and replace spaces with hyphens
    text = re.sub(r"[^a-z0-9]+", "-", text)
    # Strip any leading or trailing hyphens
    text = text.strip("-")
    return text
