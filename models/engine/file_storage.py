#!/usr/bin/python3
"""
This class serializes instances to a JSON
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ Class that serializes"""
    __file_path = "file.json"
    __objects = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def all(self):
        """ Returns the dict objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __object """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes objects to the JSON """
        obj_dict = {
            key: value.to_dict() for key, value in FileStorage.__objects.items()
        }
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """ Deserializes objects from the JSON """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    if class_name in self.__objects:
                        cls = self.__objects[class_name]
                        new_obj = cls(**value)
                        self.new(new_obj)
