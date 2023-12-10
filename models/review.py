#!/usr/bin/python3
"""Module representation of class review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class implementation of Review

    Attributes:
        place_id (str): id of the place
        user_id (str): id of the user
        text (str): text review
    """

    place_id = ""
    user_id = ""
    text = ""
