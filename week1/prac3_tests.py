#!/usr/bin/python3

import unittest
import person as p3

class TestStringMethods(unittest.TestCase):
    """Ignore this code for now; will explain in week 2."""

    def setUp(self):
        self.person = p3.create_person("Daniel Radcliffe",1.65,57)

    def test_create_person(self):
        self.assertEqual(self.person, {'name': 'Daniel Radcliffe',
                                       'height': 1.65, 'weight': 57})

    def test_format(self):
        self.assertTrue(isinstance(p3.format(self.person), str))

    def test_display(self):
        self.assertEqual(p3.display(self.person), None)


if __name__ == '__main__':
    unittest.main()