#!/usr/bin/python3
"""
Unittest for state.py
"""
import unittest
from models.state import State
import datetime


class TestState(unittest.TestCase):
    def test_class_exists(self):
        s = State()
        self.assertEqual(str(type(s)), "<class 'models.state.State'>")

    def test_state_inheritance(self):
        s = State()
        self.assertIsInstance(s, State)

    def test_has_attributes(self):
        s = State()
        self.assertTrue(hasattr(s, 'name'))
        self.assertTrue(hasattr(s, 'id'))
        self.assertTrue(hasattr(s, 'created_at'))
        self.assertTrue(hasattr(s, 'updated_at'))

    def test_attribute_types(self):
        s = State()
        self.assertIsInstance(s.name, str)
        self.assertIsInstance(s.id, str)
        self.assertIsInstance(s.created_at, datetime.datetime)
        self.assertIsInstance(s.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
