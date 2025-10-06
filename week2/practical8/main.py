from circle import Circle
from point import Point
from rectangle import Rectangle

"""Test for exercise 1"""
# p = Point(2,1)
# print(p)
# print(p.__repr__())

"""Test for exercise 2"""
r = Rectangle(Point(1, 1), 2, 3)
print(r)
# r = Rectangle((1,1), 2,3)
# print(r.o)
print(r.__repr__())
print("{} -> area={}, peri={}".format(r, r.area(), r.perimeter()))
print(Point(1,1) in r)
print(Point(1,0) in r)
print(Point(0,3) in r)
print(Point(3,0) in r)


"""Test for exercise 3"""
# define a circle
cir = Circle(Point(1, 1), 2)
# c = Circle((1,1),2) # should raise a TypeError
print(cir)
print(cir.__repr__())
print("{} -> area={}, peri={}".format(cir, cir.area(), cir.perimeter()))
# should be true
print(Point(1, 1) in cir)  # == print(cir.__contains__(Point(1,1)))
print(Point(1, 0) in cir)
# should be false
print(Point(0, 3) in cir)
print(Point(3, 0) in cir)


"""Test for exercise 4"""
from curve import Curve

cur = Curve(Point(1, 1), Point(2, 4), Point(3, 9))
# cur2 = Curve(Point(1,1),(2,2))
print(cur)
print(cur.__repr__())

# return a point/item
print(cur[1])  # == print(cur.__getitem__(1))
# return points/items i.e. subcurve
print(cur[0:2])  # == print(cur.__getitem__(0:2))
# update point
cur[1] = Point(1, 1)  # == print(cur.__setitem__(1,Point(1,1)))
# cur[1] = (1,1) # should raise a TypeError
print(cur)
