from abstracts import AbstractShape
from point import Point


class Rectangle(AbstractShape):
    """Class to represent a rectangle on a graph"""

    def __init__(self, o, w, l):
        """constructor for a rectangle, origin point is middle"""
        if type(o) != Point:
            raise TypeError
        else:
            self.o = o
            self.w = w
            self.l = l

    def __str__(self):
        """string representation of a rectangle"""
        return f"Rectangle(origin = {self.o}, width = {self.w}, length = {self.l})"

    def __repr__(self):
        """formal string representation of a rectangle"""
        return f"Rectangle(o={self.o}, w={self.w}, l={self.l})"

    def area(self):
        """method to find the area of a rectangle"""
        return self.l * self.w

    def perimeter(self):
        """method to find the perimeter of a rectangle"""
        return 2 * (self.l + self.w)

    def __contains__(self, p):
        """method to determine whether a given point is inside the object"""
        if p.x <= self.o.x and p.y <= self.o.y:
            return True
        else:
            return False
