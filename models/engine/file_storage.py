#!/usr/bin/python3
"""
This class serializes instances to a JSON
"""
import json
import os


class FileStorage:
    """ Class that serializes"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dic objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __object """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes objects to the JSONf """
        obj_dict = {
                key: value.to_dict() for key,
                value in FileStorage.__objects.items()
                }
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """ Deserializes objects from the JSONf """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.amenity import Amenity
        from models.state import State
        from models.review import Review
        class_mapping = {
           'BaseModel': BaseModel,
           'User': User,
           'Place': Place,
           'City': City,
           'Amenity': Amenity,
           'State': State,
           'Review': Review
         }
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    cls = class_mapping.get(class_name)
                    if cls:
                        new_obj = cls(**value)
                        self.new(new_obj)
