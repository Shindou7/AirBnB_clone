#!/usr/bin/pyhon3
"""
Parent class that will inherit
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            daytimes = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(kwargs[key], daytimes)
                if key != '__class__':
                    setattr(self, key, value)

    def save(self):
        """attribute  datetime, save to storage"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary rep of the BaseModel instance"""
        Base_dict = self.__dict__.copy()
        Base_dict['__class__'] = self.__class__.__name__
        Base_dict['created_at'] = self.created_at.isoformat()
        Base_dict['updated_at'] = self.updated_at.isoformat()
        return Base_dict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)
