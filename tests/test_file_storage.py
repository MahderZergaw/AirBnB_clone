# #!/usr/bin/python3
# """This module contains Unittest for the FileStorage class"""

# import unittest
# import os
# import json
# from models.engine.file_storage import FileStorage
# from models.base_model import BaseModel
# from models import storage

# class TestFileStorage(unittest.TestCase):
#     """Test cases for FileStorage class"""

#     def setUp(self):
#         """Setup method to initialize instances"""
#         self.storage = FileStorage()

#     def reloadStorage(self):
#         """resets JSON file created"""
#         if os.path.exists(FileStorage._FileStorage__file_path):
#             os.remove(FileStorage._FileStorage__file_path)


#     def tearDown(self):
#         """clean up after testing to remove JSON file created"""
#         self.reloadStorage()
#         pass

#     def test_all(self):
#         """Test the all() method"""
#         self.reloadStorage()
#         self.assertEqual(storage.all(), {})

#         o = storage.classes()[classname]()
#         storage.new(o)
#         key = "{}.{}".format(type(o).__name__, o.id)
#         self.assertTrue(key in storage.all())
#         self.assertEqual(storage.all()[key], o)

#     def test_new(self):
#         """Test the new() method"""
#         obj = BaseModel()
#         self.storage.new(obj)
#         all_objs = self.storage.all()
#         self.assertIn('BaseModel.' + obj.id, all_objs)
#         self.assertEqual(all_objs['BaseModel.' + obj.id],
#                          obj.to_dict())

#     def test_save_reload(self):
#         """Test the save() and reload() methods"""
#         obj = BaseModel()
#         self.storage.new(obj)
#         self.storage.save()
#         self.storage.reload()
#         all_objs = self.storage.all()
#         self.assertIn('BaseModel.' + obj.id, all_objs)
#         self.assertEqual(all_objs['BaseModel.' + obj.id],
#                          obj.to_dict())


# if __name__ == "__main__":
#     unittest.main()


#!/usr/bin/python3
"""Unittest module for the FileStorage class."""

import unittest
from datetime import datetime
import time
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import re
import json
import os


class TestFileStorage(unittest.TestCase):
    """Test Cases for the FileStorage class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def test_5_instantiation(self):
        """Tests instantiation of storage class."""
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test_3_init_no_args(self):
        """Tests __init__ with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.__init__()
        msg = "descriptor '__init__' of 'object' object needs an argument"
        self.assertEqual(str(e.exception), msg)

    def test_3_init_many_args(self):
        """Tests __init__ with many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            b = FileStorage(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        msg = "object() takes no parameters"
        self.assertEqual(str(e.exception), msg)

    def test_5_attributes(self):
        """Tests class attributes."""
        self.resetStorage()
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertEqual(getattr(FileStorage, "_FileStorage__objects"), {})

    def help_test_all(self, classname):
        """Helper tests all() method for classname."""
        self.resetStorage()
        self.assertEqual(storage.all(), {})

        o = storage.classes()[classname]()
        storage.new(o)
        key = "{}.{}".format(type(o).__name__, o.id)
        self.assertTrue(key in storage.all())
        self.assertEqual(storage.all()[key], o)
