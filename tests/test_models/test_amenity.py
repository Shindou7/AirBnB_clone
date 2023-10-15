#!/usr/bin/python3
"""
Unittest for amenity.py
"""
import unittest
from models.amenity import Amenity
import datetime


class TestAmenity(unittest.TestCase):
    def test_class_exists(self):
        a = Amenity()
        self.assertEqual(str(type(a)), "<class 'models.amenity.Amenity'>")

    def test_amenity_inheritance(self):
        a = Amenity()
        self.assertIsInstance(a, Amenity)

    def test_has_attributes(self):
        a = Amenity()
        self.assertTrue(hasattr(a, 'name'))
        self.assertTrue(hasattr(a, 'id'))
        self.assertTrue(hasattr(a, 'created_at'))
        self.assertTrue(hasattr(a, 'updated_at'))

    def test_attribute_types(self):
        a = Amenity()
        self.assertIsInstance(a.name, str)
        self.assertIsInstance(a.id, str)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
