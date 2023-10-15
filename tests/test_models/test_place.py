#!/usr/bin/python3
"""
Unittest for place.py
"""
import unittest
from models.place import Place
import datetime

class TestPlace(unittest.TestCase):
    def test_class_exists(self):
        p = Place()
        self.assertEqual(str(type(p)), "<class 'models.place.Place'>")

    def test_place_inheritance(self):
        p = Place()
        self.assertIsInstance(p, Place)

    def test_has_attributes(self):
        p = Place()
        self.assertTrue(hasattr(p, 'city_id'))
        self.assertTrue(hasattr(p, 'user_id'))
        self.assertTrue(hasattr(p, 'name'))
        self.assertTrue(hasattr(p, 'description'))
        self.assertTrue(hasattr(p, 'number_rooms'))
        self.assertTrue(hasattr(p, 'number_bathrooms'))
        self.assertTrue(hasattr(p, 'max_guest'))
        self.assertTrue(hasattr(p, 'price_by_night'))
        self.assertTrue(hasattr(p, 'latitude'))
        self.assertTrue(hasattr(p, 'longitude'))
        self.assertTrue(hasattr(p, 'amenity_ids'))
        self.assertTrue(hasattr(p, 'id'))
        self.assertTrue(hasattr(p, 'created_at'))
        self.assertTrue(hasattr(p, 'updated_at'))

    def test_attribute_types(self):
        p = Place()
        self.assertIsInstance(p.city_id, str)
        self.assertIsInstance(p.user_id, str)
        self.assertIsInstance(p.name, str)
        self.assertIsInstance(p.description, str)
        self.assertIsInstance(p.number_rooms, int)
        self.assertIsInstance(p.number_bathrooms, int)
        self.assertIsInstance(p.max_guest, int)
        self.assertIsInstance(p.price_by_night, int)
        self.assertIsInstance(p.latitude, float)
        self.assertIsInstance(p.longitude, float)
        self.assertIsInstance(p.amenity_ids, list)
        self.assertIsInstance(p.id, str)
        self.assertIsInstance(p.created_at, datetime.datetime)
        self.assertIsInstance(p.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
