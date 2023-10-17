#!/usr/bin/python3
"""This module contains Unittest for the FileStorage class"""

import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class"""

    def setUp(self):
        """Setup method to initialize instances"""
        self.storage = FileStorage()
        if FileStorage._FileStorage__file_path is None:
            raise ValueError("File path is None"
                             " Please set a valid file path.")

    def reloadStorage(self):
        """resets JSON objects created"""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """clean up after testing to remove JSON file created"""
        self.reloadStorage()

    def test_no_args(self):
        """Tests __init__ without arguments"""
        self.reloadStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.__init__()
        err_msg = "descriptor '__init__' of 'object' object needs an argument"
        self.assertEqual(str(e.exception), err_msg)

    def test_attributes(self):
        """tests class attribute"""
        self.assertTrue(hasattr(FileStorage,
                                "_FileStorage__file_path"))
        self.assertEqual(getattr(FileStorage,
                                 "_FileStorage__objects"), {})
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))

    def test_all(self):
        """tests all() method"""
        obj = BaseModel()
        storage.new(obj)
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertTrue(key in storage.all())
        self.assertEqual(storage.all()[key], obj)

    def test_all_return_empty_dict(self):
        """Test if all() method returns an empty dictionary"""
        self.reloadStorage()
        result = self.storage.all()
        self.assertEqual(result, {})

    def test_new(self):
        """tests new() method"""
        obj = BaseModel()
        storage.new(obj)
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertTrue(key in FileStorage._FileStorage__objects)
        self.assertEqual(FileStorage._FileStorage__objects[key], obj)

    def test_new_do_nothing(self):
        """Test if new() method does nothing"""
        self.reloadStorage()
        initial_objects = self.storage.all()
        obj = BaseModel()
        self.storage.new(obj)
        updated_objects = self.storage.all()
        self.assertEqual(initial_objects, updated_objects)

    def test_save(self):
        """tests save() method"""
        obj = BaseModel()
        storage.new(obj)
        key = "{}.{}".format(type(obj).__name__, obj.id)
        storage.save()
        self.assertTrue(os.path.isfile(FileStorage
                                       ._FileStorage__file_path))
        obj_dict = {key: obj.to_dict()}
        with open(FileStorage._FileStorage__file_path, "r") as file:
            self.assertEqual(len(file.read()),
                             len(json.dumps(obj_dict)))
            file.seek(0)
            self.assertEqual(json.load(file), obj_dict)

    def test_save_do_nothing(self):
        """Test if save() method does nothing"""
        self.reloadStorage()
        initial_objects = self.storage.all()
        obj = BaseModel()
        self.storage.save(obj)
        updated_objects = self.storage.all()
        self.assertEqual(initial_objects, updated_objects)

    def test_reload_do_nothing(self):
        """Test if reload() method does nothing"""
        self.reloadStorage()
        initial_objects = self.storage.all()
        self.storage.reload()
        updated_objects = self.storage.all()
        self.assertEqual(initial_objects, updated_objects)


if __name__ == "__main__":
    unittest.main()
