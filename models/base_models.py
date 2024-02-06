#!/usr/bin/python3
"""This is the base class of the AirBnB"""

from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """defines all common attributes/methods for other classes"""



    def __init__(self, *args, **kwargs):
        """Initializes class Base Model
        args:
            kwargs - argumets used for the constructor of a base model
        
        attributes:
            created_at -assigns the current datetime when an instance is created
            updated_at-assign the current datetime when an instance is created
            id - string - assign with an uuid when an instance is created
        """

        tformat = '%Y-%m-%dT%H:%M:%S.%f'

        self.id == str(uuid.uuid4())
        self.updated_at = datetime.now()
        self.create_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """this updates thepulic istance attribute 'updated_at' with current
        datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all key/
        values of '__dict__' of the instance
        """
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["id"] = self.id
        my_dict["updated_at"] = self.updated_at.isoformat()

        return my_dict

    def __str__(self):
        """Returns a string of class name, id, and dictionary"""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)
