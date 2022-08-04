#!/usr/bin/python3
"""This module represents our storage engine"""
import json

class FileStorage:
    """This file storage class
        serializes instances to JSON file
        and deserializes JSON file to instances
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """This method returns a dictionary
            of all objects from __objects
        """
        return FileStorage.__objects
    
    def new(self, obj):
        """This method sets in __objects (obj)
            with key <obj class name>.id
        """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects.update(key)

    def save(self):
        """
