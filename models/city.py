#!/usr/bin/python3
"""module contains a city class that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """manages the cities"""
    state_id = ""
    name = ""
