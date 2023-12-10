#!/usr/bin/python
"""Module representation of Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class implementation of Amenity

    Attributes:
        name (str): name of the amenity
    """

    name = ""
