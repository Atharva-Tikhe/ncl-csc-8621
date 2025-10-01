#!/usr/bin/python3

import unittest
import bakery as p1


class TestStringMethods(unittest.TestCase):
    """Ignore this code for now; will explain in week 2."""

    def test_pies(self):
        self.assertEqual(p1.pies, 12)

    def test_volume(self):
        self.assertEqual(round(p1.volume,1), 78.5)

    def test_average(self):
        self.assertEqual(p1.average, 4)

    def test_profit(self):
        self.assertEqual(round(p1.profit), 84)

if __name__ != '__main__':
    unittest.main()
