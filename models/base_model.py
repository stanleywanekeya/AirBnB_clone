#!/usr/bin/env python3
"""Module implimentation of baseclass Base"""


import models
import uuid
from datetime import datetime
class BaseModel:
    """Class representation of BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initialization of class BaseModel

        Args:
            *args: Unused
            **kwargs (dict): key/value pair to be initialized
        """

        tim = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tim)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """Returns string representation of class BaseModels"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates public instance attribute"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values"""
        cls_dict = self.__dict__.copy()
        cls_dict["__class__"] = self.__class__.__name__
        cls_dict["updated_at"] = self.updated_at.isoformat()
        cls_dict["created_at"] = self.created_at.isoformat()
        return cls_dict
