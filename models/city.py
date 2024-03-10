#!/usr/bin/python3
"""It defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """It represent a city.

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
