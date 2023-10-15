#!/usr/bin/python3
"""
Unittest for city.py
"""
import unittest
from models.city import City
import datetime

class TestCity(unittest.TestCase):
    def test_class_exists(self):
        c = City()
        self.assertEqual(str(type(c)), "<class 'models.city.City'>")

    def test_city_inheritance(self):
        c = City()
        self.assertIsInstance(c, City)

    def test_has_attributes(self):
        c = City()
        self.assertTrue(hasattr(c, 'state_id'))
        self.assertTrue(hasattr(c, 'name'))
        self.assertTrue(hasattr(c, 'id'))
        self.assertTrue(hasattr(c, 'created_at'))
        self.assertTrue(hasattr(c, 'updated_at'))

    def test_attribute_types(self):
        c = City()
        self.assertIsInstance(c.state_id, str)
        self.assertIsInstance(c.name, str)
        self.assertIsInstance(c.id, str)
        self.assertIsInstance(c.created_at, datetime.datetime)
        self.assertIsInstance(c.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
