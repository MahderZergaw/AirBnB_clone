#!/usr/bin/python3
"""BaseModel module"""

from datetime import datetime
from models import storage
import uuid


class BaseModel:
    """Defines common methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializing an instance of BaseModel"""

        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value,
                                              "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """returns a string representation of class"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance updated_at"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        obj_dict = self.__dict__.copy()
        if isinstance(obj_dict["created_at"], datetime):
            obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        if isinstance(obj_dict["updated_at"], datetime):
            obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()
        obj_dict["__class__"] = type(self).__name__
        return obj_dict
