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

    def reloadStorage(self):
        """resets JSON file created"""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """clean up after testing to remove JSON file created"""
        self.reloadStorage()
        pass

    def test_all(self):
        """Test the all() method"""
        self.reloadStorage()
        self.assertEqual(storage.all(), {})
        o = storage.classes()[classname]()
        storage.new(o)
        key = "{}.{}".format(type(o).__name__, o.id)
        self.assertTrue(key in storage.all())
        self.assertEqual(storage.all()[key], o)

    def test_new(self):
        """Test the new() method"""
        obj = BaseModel()
        self.storage.new(obj)
        all_objs = self.storage.all()
        self.assertIn('BaseModel.' + obj.id, all_objs)
        self.assertEqual(all_objs['BaseModel.'
                                  + obj.id], obj.to_dict())

    def test_save_reload(self):
        """Test the save() and reload() methods"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertIn('BaseModel.' + obj.id, all_objs)
        self.assertEqual(all_objs['BaseModel.'
                                  + obj.id], obj.to_dict())


if __name__ == "__main__":
    unittest.main()
