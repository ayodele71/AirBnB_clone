#!/usr/bin/python3
"""
    This module defines the BaseModel class and is a
    class from which all other classes would inherit
"""
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """
        The base class for all other classes created 
        in this project..
    """

    def __init__(self, num=0):
        self.id = uuid4()
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """Define the print() representation of the BaseModel"""
        pass

    def save(self):
        """Updates the attribute 'update_at' with the current datetime"""
        self.update_at = datetime.today()

    def to_dict(self):
        """Returns a dictionary containing key/value pairs of __dict__"""
        pass



