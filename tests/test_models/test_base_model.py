#!/usr/bin/python3
"""Unitests cases to test base_model.py"""

import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """to setup test methods"""
        self.base_model = BaseModel()

    def test_id_gen(self):
        """test Unique ID"""
        self.assertIsNotNone(self.base_model.id)

    def reloadStorage(self):
        """resets JSON objects"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_created_at(self):
        """test if created_at has valid datetime"""
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at(self):
        """test if updated_at has valid datetime"""
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str_(self):
        """test the string representation of BaseModel"""
        str_rep = "[{}] ({}) {}".format("BaseModel",
                                        self.base_model.id,
                                        self.base_model.__dict__)
        self.assertEqual(str(self.base_model), str_rep)

    def test_dict_to(self):
        """test if to_dict method returns a dictionary
           with the right attributes
        """
        dict_to = self.base_model.to_dict()
        self.assertIsInstance(dict_to, dict)
        self.assertEqual(dict_to["__class__"], "BaseModel")
        self.assertIsInstance(dict_to["created_at"], str)
        self.assertIsInstance(dict_to["updated_at"], str)

    def test_no_args(self):
        """Tests __init__ without arguments"""
        self.reloadStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.__init__()
        err_msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), err_msg)

    def test_save_reload(self):
        """Test the save() and reload() methods"""
        self.reloadStorage()
        class_ = BaseModel()
        class_.save()
        key = "{}.{}".format(type(class_).__name__, class_.id)
        obj_dict = {key: class_.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage.
                                       _FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path, "r") as file:
            self.assertEqual(len(file.read()),
                             len(json.dumps(obj_dict)))
            file.seek(0)
            self.assertEqual(json.load(file), obj_dict)


if __name__ == "__main__":
    unittest.main()
