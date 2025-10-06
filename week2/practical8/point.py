class Point:
    """class to represent a point on a graph"""

    def __init__(self, x, y):
        """constructor for a point"""
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        """string representation of a point"""
        return f"Point(x = {self.x}, y = {self.y})"

    def __repr__(self):
        """formal string representation of a point"""
        return f"Point(x={self.x},y={self.y})"

    def __contains__(self, p):
        """method to determine whether a given point is inside the object"""
        if p.x <= self.o.x and p.y <= self.o.y:
            return True
        else:
            return False


if __name__ == "__main__":
    p = Point(2, 1)
    print(p)
    print(p.__repr__())
