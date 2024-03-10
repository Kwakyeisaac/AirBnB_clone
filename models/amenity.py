#!/usr/bin/python3
"""It defines the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """It represents an amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
