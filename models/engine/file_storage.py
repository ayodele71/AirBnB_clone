"""
    This module handles serialization/deserialization of objects
"""
import json
from pathlib import Path

class FileStorage:
    """
    Serializes instances to a JSON file and deserializes
    JSON file to instances

    """
    def __init__(self, file_path, objects):
        """Instantiates the class with prameters"""
        self.file_path = file_path
        self.objects = objects

    @property
    def file_path(self):
        """Get/set the file path for the JSON object"""
        return (self.__file_path)

    @file_path.setter
    def file_path(self):
        if not self.__path:
            self.__path = str(Path.cwd() / objects.json)
    
    def objects(self):
        """Get/set the dictionary that stores all objects by <class name>.id"""
        return (self.__objects)

    @objects.setter
    def objects(self):
        try:
            if self.__objects:
                pass
        except (NameError):
            self.__objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        self.objects()

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        class_name = obj['__class__'] 
        obj_id = obj['id']
        class_name_id = class_name + '.' + obj_id
        self.__objects[class_name_id] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        obj_file = open(self.__file_path, w)
        obj_file.write(json.dumps(self.__objects))
        obj_file.close()
    
    def reload(self):
        """Deserializes the JSON fileto __objects"""
        if self.__file_path:
            object_file = open(self.__file)
            self.__objects = json.load(object_file.read())
