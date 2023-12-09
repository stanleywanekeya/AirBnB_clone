#!/usr/bin/env python3
"""Module implimentation of baseclass Base"""


import uuid
from datetime import datetime
class BaseModel:
    """Class representation of BaseModel"""

    def __init__(self):
        """Initialization of class BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """Returns string representation of class BaseModels"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates public instance attribute"""
        self.update_at = datetime.today()

    def to_dict(self):
        """Returns a dictionary containing all keys/values"""
        cls_dict = self.__dict__.copy()
        cls_dict["__class__"] = self.__class__.__name__
        cls_dict["updated_at"] = self.updated_at.isoformat()
        cls_dict["created_at"] = self.created_at.isoformat()
        return cls_dict
