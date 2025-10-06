from point import Point
from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, o, s):
        super().__init__(o, s, s)
        self.s = s

    def __str__(self):
        return f"Square (side = {self.s})"

    def __repr__(self):
        return f"Sqaure(s={self.s})"


sq = Square(Point(1, 1), 5)

print(sq.area())
