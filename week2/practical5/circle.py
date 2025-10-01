from point import Point
from math import pi

class Circle:
    """Class to represent a circle on a graph"""

    def __init__(self, o, r):
        """constructor for a rectangle, origin point is middle"""
        if type(o) != Point:
            raise TypeError
        else:
            self.o = o
            self.r = r

    def __str__(self):
        """string representation of a circle"""
        return f"Circle({self.o.x}, {self.o.y}, {self.r})"

    def __repr__(self):
        """formal string representation of a circle"""
        return f"Circle({self.o}, {self.r})"

    def area(self):
        """method to find the area of a circle"""
        return pi * self.r ** 2

    def perimeter(self):
        """method to find the perimeter of a rectangle"""
        return 2 * pi * self.r

    def __contains__(self, p):
        """method to determine whether a given point is inside the object"""
        if p.x <= self.o.x and p.y <= self.o.y:
            return True
        else:
            return False


