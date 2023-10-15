#!/usr/bin/python3
"""This module contains FileStorages class"""

import datetime
import json
import os


class FileStorage:
    """Serializes instances to a JSON file
       Deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in objects the obj with key <obj class name>.id"""
        class_name = obj.__class__.__name__
        key = class_name + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON
        file (path: __file_path)
        """
        with open(FileStorage.__file_path, "w") as file:
            fl = {key: value.to_dict() for key,
                  value in FileStorage.__objects.items()}
            json.dump(fl, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        otherwise, does nothing
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                _objects = json.load(file)
                _objects = {key: self.classes()
                            [value["__class__"]](**value) for
                            key, value in _objects.items()}
                FileStorage.__objects = _objects

    def classes(self):
        """returns valid classes dictionary"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        all_class = {"BaseModel": BaseModel,
                     "User": User,
                     "State": State,
                     "City": City,
                     "Amenity": Amenity,
                     "Place": Place,
                     "Review": Review}
        return all_class

    def attributes(self):
        attr = {
            "BaseModel":
            {"id": str,
             "created_at": datetime.datetime,
             "Update_at": datetime.datetime},
            "User":
            {"email": str,
             "password": str,
             "first_name": str,
             "last_name": str},
            "State":
            {"name": str},
            "City":
            {"state_id": str,
             "name": str},
            "Amenity":
            {"name": str},
            "Place":
            {"city_id": str,
             "user_id": str,
             "name": str,
             "description": str,
             "number_rooms": int,
             "number_bathrooms": int,
             "max_guest": int,
             "price_by_night": int,
             "latitude": float,
             "longitude": float,
             "amenity_ids": list},
            "Review":
            {"place_id": str,
             "user_id": str,
             "text": str}
            }
        return attr
