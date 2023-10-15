#!/usr/bin/python3
""" contains a user class that inherits from BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
    """Inherits from BaseModel for the User"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
