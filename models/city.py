#!/usr/bin/python3
"""classes that inherit from BaseModel City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """state_id (str),name (str)"""

    state_id = ""
    name = ""
