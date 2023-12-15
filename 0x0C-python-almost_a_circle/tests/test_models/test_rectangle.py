#!/usr/bin/python3
"""Defines unittests for rectangle.py"""

import unittest
from models.base import Base
from models.Rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unittests for testing of the Rectangle class"""
    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10,2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

