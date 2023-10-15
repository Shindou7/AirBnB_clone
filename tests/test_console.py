#!/usr/bin/python3
"""Unittest test_console module"""

import unittest
import console
import pycodestyle
from unittest.mock import patch
from io import StringIO
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestConsole(unittest.TestCase):
