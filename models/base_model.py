#!/usr/bin/python3
"""It defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """it represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """It initializes a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for a, b in kwargs.items():
                if a == "created_at" or b == "updated_at":
                    self.__dict__[a] = datetime.strptime(b, tform)
                else:
                    self.__dict__[a] = b
        else:
            models.storage.new(self)

    def save(self):
        """It update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """It return the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """It return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
