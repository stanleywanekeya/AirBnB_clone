#!/usr/bin/python3
"""Module implimentation of class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class implementation of User

    Attributes:
        email (str): email of the user
        password (str): password of the user
        first_name (str): first_name of the user
        last_name (str): last name of the user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
