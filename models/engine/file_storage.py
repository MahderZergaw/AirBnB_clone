#!/usr/bin/python3
"""This module contains FileStorages class"""
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
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON
        file (path: __file_path)
        """
        with open(FileStorage.__file_path, "w") as file:
            json.dump(FileStorage.__objects, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        otherwise, does nothing
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                FileStorage.__objects = json.load(file)
