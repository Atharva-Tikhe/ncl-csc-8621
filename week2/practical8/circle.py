from math import pi, sqrt

from abstracts import AbstractCircle
from point import Point


class CircleByRadius(AbstractCircle):
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
        return f"Circle({self.o.x}, {self.o.y}, {self.radius()})"

    def __repr__(self):
        """formal string representation of a circle"""
        return f"Circle({self.o}, {self.radius()})"

    def radius(self):
        """Returns the radius of the circle"""
        return self.r

    def area(self):
        """method to find the area of a circle"""
        return pi * self.radius() ** 2

    def perimeter(self):
        """method to find the perimeter of a rectangle"""
        return 2 * pi * self.radius()

    def __contains__(self, p):
        """method to determine whether a given point is inside the object"""
        if p.x <= self.o.x and p.y <= self.o.y:
            return True
        else:
            return False


class CircleByArea(AbstractCircle):
    def __init__(self, o: Point, a: float):
        if type(o) != Point:
            raise TypeError
        else:
            self.o = o
        self.a = a
        self.r = self.radius()

    def __str__(self):
        return f"CircleByArea(area = {self.a})"

    def __repr__(self):
        return f"CircleByArea(a={self.a})"

    def radius(self):
        r_sqr = self.a / pi
        return sqrt(r_sqr)

    def area(self):
        return self.a

    def perimeter(self):
        return 2 * pi * self.r

    def __contains__(self, p):
        """method to determine whether a given point is inside the object"""
        if p.x <= self.o.x and p.y <= self.o.y:
            return True
        else:
            return False


if __name__ == "__main__":

    cba = CircleByArea(Point(3, 2), 46.123)
    print(cba.radius())
    print(cba.area())
    print(cba.perimeter())
    print(Point(4, 1) in cba)

    c = CircleByRadius(Point(1, 1), cba.radius())
    print(Point(0, 0) in c)
    ca = c.area()
    print(ca)

    # error presentation
    # c = CircleByRadius((1, 1), 3)
    # ca = c.area()
    # print(ca)
