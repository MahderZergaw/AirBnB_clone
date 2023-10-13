#!/usr/bin/python3
""" Module contains BaseModel class that
   defines common methods for other classes
"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """ Defines common methods for other classes"""

    def __init__(self, *args,**kwargs):
        """Initializing an instance of BaseModel"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value,
                                              "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()

    def __str__(self):
        """returns a string representation of
        [<class name>] (<self.id>) <self.__dict__>

        """
        return "[{}] ({}) {}".format(__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of _dict_ of the instance:
        """
        self.__dict__["__class__"] = _class__.__name_
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        return self.__dict__