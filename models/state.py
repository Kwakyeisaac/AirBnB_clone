#!/usr/bin/python3
"""It defines the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """It represent a state.

    Attributes:
        name (str): The name of the state.
    """

    name = ""
