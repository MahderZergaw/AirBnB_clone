#!/usr/bin/python3
"""moduls contains Review class that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """manages reviews"""
    place_id = ""
    user_id = ""
    text = ""
