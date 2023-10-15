#!/usr/bin/python3
"""contains a class that inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """state class to manage state objects"""
    name = ""
