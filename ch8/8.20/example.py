#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You have the name of a method that you want to call on an object stored in a
string and you want to execute the method.
"""


"""
SOLUTION
"""

import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({!r:}, {!r:})'.format(self.x, self.y)

    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)

p = Point(2, 3)
d = getattr(p, 'distance')(0, 0)    # Calls p.distance(0, 0)
print('d = {}'.format(d))
print('')


import operator
d2 = operator.methodcaller('distance', 0, 0)(p)
print('d2 = {}'.format(d2))
print('')


points = [
    Point(1, 2),
    Point(3, 0),
    Point(10, -3),
    Point(-5, -7),
    Point(-1, 8),
    Point(3, 2)
]

# Sort by distance from origin (0, 0)
points.sort(key=operator.methodcaller('distance', 0, 0))
print(points)
print('')


"""
DISCUSSION
"""

p = Point(3, 4)
d = operator.methodcaller('distance', 0, 0)
print(d(p))
