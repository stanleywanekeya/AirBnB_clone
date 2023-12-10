#!/usr/bin/python
"""Module representation of class City"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class implementation of City
    Attributes:
        name (str): name of the city
        state_id (str): the id of the city
    """

    state_id = ""
    name = ""
