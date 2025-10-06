import unittest

from circle import CircleByRadius
from curve import Curve
from point import Point
from rectangle import Rectangle


class TestPoint(unittest.TestCase):

    def test_point_str(self):
        """Exercise 1"""
        p = Point(2, 1)
        self.assertEqual(p.__repr__(), "Point(x=2,y=1)")
        self.assertEqual(p.__str__(), "Point(x = 2, y = 1)")


class TestRectangle(unittest.TestCase):
    """Test for exercise 2"""

    def setUp(self):
        self.r = Rectangle(Point(1, 1), 2, 3)

    def test_init(self):
        with self.assertRaises(TypeError):
            self.r = Rectangle((1, 1), 2, 3)

    def test_membership(self):
        self.assertTrue(Point(1, 1) in self.r)
        self.assertTrue(Point(1, 0) in self.r)
        self.assertFalse(Point(0, 3) in self.r)
        self.assertFalse(Point(3, 0) in self.r)

    def test_area(self):
        self.assertEqual(self.r.area(), 6)

    def test_perimeter(self):
        self.assertEqual(self.r.perimeter(), 10)


class TestCircle(unittest.TestCase):
    """Test for exercise 3"""

    def setUp(self):
        self.c = CircleByRadius(Point(1, 1), 3)

    def test_membership(self):
        self.assertTrue(Point(1, 1) in self.c)
        self.assertTrue(Point(1, 0) in self.c)
        self.assertFalse(Point(0, 3) in self.c)
        self.assertFalse(Point(3, 0) in self.c)

    def test_area(self):
        self.assertAlmostEqual(round(self.c.area(), 4), 28.2743, delta=0.1)

    def test_perimeter(self):
        self.assertAlmostEqual(round(self.c.perimeter(), 4), 18.8495, delta=0.1)


class TestCurve(unittest.TestCase):
    """Test for exercise 4"""

    def setUp(self):
        self.curve = Curve(Point(1, 1), Point(2, 4), Point(3, 9))

    def test_init(self):
        with self.assertRaises(TypeError):
            self.curve = Curve((1, 1), (1, 2), (1, 3))

    def test_slicing(self):
        self.assertEqual(self.curve[1].__repr__(), Point(2, 4).__repr__())
        self.assertEqual(
            self.curve[0:2].__repr__(), [Point(x=1, y=1), Point(x=2, y=4)].__repr__()
        )
        with self.assertRaises(TypeError):
            self.curve[1] = (1, 1)


if __name__ == "__main__":
    unittest.main()
