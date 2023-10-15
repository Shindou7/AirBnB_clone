#!/usr/bin/python3
"""
Unittest for user.py
"""
import unittest
from models.user import User
import datetime

class TestUser(unittest.TestCase):
    def test_class_exists(self):
        u = User()
        self.assertEqual(str(type(u)), "<class 'models.user.User'>")

    def test_user_inheritance(self):
        u = User()
        self.assertIsInstance(u, User)

    def test_has_attributes(self):
        u = User()
        self.assertTrue(hasattr(u, 'email'))
        self.assertTrue(hasattr(u, 'password'))
        self.assertTrue(hasattr(u, 'first_name'))
        self.assertTrue(hasattr(u, 'last_name'))
        self.assertTrue(hasattr(u, 'id'))
        self.assertTrue(hasattr(u, 'created_at'))
        self.assertTrue(hasattr(u, 'updated_at'))

    def test_attribute_types(self):
        u = User()
        self.assertIsInstance(u.first_name, str)
        self.assertIsInstance(u.last_name, str)
        self.assertIsInstance(u.email, str)
        self.assertIsInstance(u.password, str)
        self.assertIsInstance(u.id, str)
        self.assertIsInstance(u.created_at, datetime.datetime)
        self.assertIsInstance(u.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
