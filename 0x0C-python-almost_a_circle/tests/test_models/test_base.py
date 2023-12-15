#!/usr/bin/python3

import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_init_id(self):
        base_instance = Base(id=5)
        self.assertEqual(base_instance.id, 5)

    def test_init_no_id(self):
        base_instance = Base()
        self.assertEqual(base_instance.id, 1)

    def test_increment_id(self):
        base_instance_1 = Base()
        base_instance_2 = Base()
        base_instance_3 = Base()
        self.assertEqual(base_instance_1.id, 1)
        self.assertEqual(base_instance_2.id, 2)
        self.assertEqual(base_instance_3.id, 3)

if __name__ == '__main__':
    unittest.main()
