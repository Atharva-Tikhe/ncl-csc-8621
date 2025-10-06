# from sympy.utilities.iterables import iterable

from point import Point

class Curve:
    """Class to represent a list of points on a graph"""

    def __init__(self, *inputs):
        """constructor for a curve"""
        self.__points = []
        # Added type checking for inputs (input validation)
        for raw_input in inputs:
            if type(raw_input) != Point:
                raise TypeError
            else:
                self.append_if_valid(raw_input)

    def append_if_valid(self, item):
        """add a new point object to the curve"""
        self.__points.append(item)

    def __str__(self):
        """string representation of a curve"""
        return f'Curve:{self.__points}'

    def __repr__(self):
        """formal string representation of a curve"""
        return f'Curve{tuple(self.__points)}'

    def __getitem__(self, index):
        """get point(s) in curve"""
        return self.__points[index]

    def __setitem__(self, index, item):
        """update curve with given point value"""
        if type(item) == Point:
            self.__points[index] = item
        else:
            raise TypeError