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

    if not hasattr(self, '__file_path'):
        __file_path = str(Path.cwd() / objects.json)
    
    
    if not hasattr(self, '__objects'):
        __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return (__objects)

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        class_name = obj['__class__'] 
        obj_id = obj['id']
        class_name_id = class_name + '.' + obj_id
        __objects[class_name_id] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        obj_file = open(__file_path, w)
        obj_file.write(json.dumps(__objects))
        obj_file.close()
    
    def reload(self):
        """Deserializes the JSON fileto __objects"""
        if __file_path:
            object_file = open(__file_path)
            __objects = json.load(object_file.read())
            object_file.close()