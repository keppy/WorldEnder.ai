from __future__ import annotations
from typing import List
from pydantic import BaseModel, Field

class Location(BaseModel):
    """
    A location with a latitude and longitude.
    Parent and children are used to create a tree structure.
    The destroyed flag is used to mark a location as destroyed.
    """
    latitude: float = Field(ge=-90.0, le=90.0, description="Latitude of the location")
    longitude: float = Field(ge=-180.0, le=180.0, description="Longitude of the location")
    parent: Location = Field(None, description="The parent location")
    children: List[Location] = Field([], description="The children locations")
    destroyed: bool = Field(False, description="Whether the location is destroyed")

    def __init__(self, **data):
        super().__init__(**data)

    def destroy(self) -> None:
        """destroy the location and all its children."""
        self.destroyed = True
        for child in self.children:
            child.destroy()