#!/usr/bin/python3
"""
Unittest for review.py
"""
import unittest
from models.review import Review
import datetime

class TestReview(unittest.TestCase):
    def test_class_exists(self):
        r = Review()
        self.assertEqual(str(type(r)), "<class 'models.review.Review'>")

    def test_review_inheritance(self):
        r = Review()
        self.assertIsInstance(r, Review)

    def test_has_attributes(self):
        r = Review()
        self.assertTrue(hasattr(r, 'place_id'))
        self.assertTrue(hasattr(r, 'user_id'))
        self.assertTrue(hasattr(r, 'text'))
        self.assertTrue(hasattr(r, 'id'))
        self.assertTrue(hasattr(r, 'created_at'))
        self.assertTrue(hasattr(r, 'updated_at'))

    def test_attribute_types(self):
        r = Review()
        self.assertIsInstance(r.place_id, str)
        self.assertIsInstance(r.user_id, str)
        self.assertIsInstance(r.text, str)
        self.assertIsInstance(r.id, str)
        self.assertIsInstance(r.created_at, datetime.datetime)
        self.assertIsInstance(r.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
