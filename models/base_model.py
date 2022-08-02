#!/usr/bin/python3
"""
    This module defines the BaseModel class and is a
    class from which all other classes would inherit
"""

class BaseModel:
    """
        The base class for all other classes created 
        in this project..
    """
    from uuid import uuid4
    from datetime import datetime


    @property
    def id(self):
        """
        Get/set the unique id for each instance
        """
        return (self.id)

    @id.setter
    def id(self):
        """Creates a unique id for each instance"""
        self.id = uuid4()

    @property
    def created_at(self):
        """
        Get/set datetime when and instance was created
        """
        return (self.created_at)

    @created_at.setter
    def created_at(self):
        """
        Create and assign datetime of creation
        """
        pass

    @property
    def updated_at(self):
        """
        Get/set datetime when and instance was updated
        """
        pass

    def __str__(self):
        """Define the print() representation of the BaseModel"""
        pass

    def save(self):
        """Updates the attribute 'update_at' with the current datetime"""
        pass

    def to_dict(self):
        """Returns a dictionary containing key/value pairs of __dict__"""
        pass



