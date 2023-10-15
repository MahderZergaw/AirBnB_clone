#!/usr/bin/python3
"""Unitests cases to test base_model.py"""

import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """to setup test methods"""
        self.base_model = BaseModel()

    def test_id_gen(self):
        """test Unique ID"""
        self.assertIsNotNone(self.base_model.id)

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

    def test_save(self):
        """test if updated_at is up to date"""
        past_time = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(past_time, self.base_model.updated_at)

if __name__ == "__main__":
    unittest.main()
    
