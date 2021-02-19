#!/usr/bin/python3
"""This is the module for the User class
It inherits from the BaseModel class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
