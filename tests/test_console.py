#!/usr/bin/python3
"""Unittest test_console module"""

import unittest
import console
from io import StringIO
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    def test_create_command(self):
        """Test the 'create' command"""
        console_output = StringIO()
        with patch("sys.stdout", console_output):
            console.HBNBCommand().onecmd("create BaseModel")
        output = console_output.getvalue()
        self.assertTrue(len(output) == 11)


if __name__ == "__main__":
    unittest.main()
