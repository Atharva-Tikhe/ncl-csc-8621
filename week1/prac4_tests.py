#!/usr/bin/python3

import unittest
import bill as p4

class TestStringMethods(unittest.TestCase):
    """Ignore this code for now; will explain in week 2."""

    def test_constants(self):
        self.assertEqual(p4.TARIFFS[1], [20, 200, 150])
        self.assertEqual(p4.TARIFFS[2], [35, 400, 350])
        self.assertEqual(p4.EXTRA_MINS_RATE, 0.1)
        self.assertEqual(p4.EXTRA_TEXT_RATE, 0.05)

    def test_calculate_extra(self):
        self.assertEqual(p4.calculate_extra(100, 50, 0.1), (0, 0))
        self.assertEqual(p4.calculate_extra(50, 100, 0.05), (50, 2.5))

if __name__ == '__main__':
    unittest.main()