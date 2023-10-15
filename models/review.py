#!/usr/bin/python3
"""classes that inherit from BaseModel review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review classes that inherit from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
