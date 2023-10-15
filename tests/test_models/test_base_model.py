#!/usr/bin/python3
"""Unittest test_base_model module"""

from models.base_model import BaseModel
import unittest
from datetime import datetime
import time
import pycodestyle


class TestBaseModel0(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def setUp(self):
        """Set up a BaseModel instance for testing"""
        self.my_model = BaseModel()

    def _docstrings(self):
        """Test module, class, and method docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def _init(self):
        """Test init method of the BaseModel class"""
        self.assertIsInstance(self.my_model, BaseModel)
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)

    def t_str(self):
        """str method of the BaseModel class"""
        ex_Oput = f"[BaseModel] ({self.my_model.id}) {self.my_model.__dict__}"
        self.assertEqual(str(self.my_model), ex_Oput)

    def test_save_updates_updated_at(self):
        """method updates the updated_at attribute"""
        myold_updated_at = self.my_model.updated_at
        self.my_model.save()
        mynew_updated_at = self.my_model.updated_at
        self.assertNotEqual(myold_updated_at, mynew_updated_at)

    def test_correct_keys_and_values(self):
        """Test that to_dict"""
        Mydicts = self.my_model.to_dict()
        self.assertEqual(Mydicts["id"], self.my_model.id)
        self.assertEqual(Mydicts["__class__"], "BaseModel")
        self.assertIn("created_at", Mydicts)
        self.assertIn("updated_at", Mydicts)

    def test_attributes_after_modification(self):
        """Test attributes"""
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89
        self.my_model.save()
        mymodel_json = self.my_model.to_dict()
        self.assertEqual(self.my_model.name, mymodel_json['name'])
        self.assertEqual(self.my_model.my_number, mymodel_json['my_number'])
        self.assertEqual('BaseModel', mymodel_json['__class__'])
        self.assertEqual(self.my_model.id, mymodel_json['id'])


if __name__ == "__main__":
    unittest.main()
