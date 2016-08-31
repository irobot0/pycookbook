#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You’re writing code that ultimately needs to create a new class object. You’ve
thought about emitting emit class source code to a string and using a function
such as exec() to evaluate it, but you’d prefer a more elegant solution.
"""


"""
DISCUSSION
"""

import operator
import types
import sys


def named_tuple(classname, fieldnames):
    # Populate a dictionary of field property accessors
    cls_dict = {
        name : property(operator.itemgetter(n))
        for n, name in enumerate(fieldnames)
    }

    # Make a __new__ function and add to the class dict
    def __new__(cls, *args):
        if len(args) != len(fieldnames):
            raise TypeError('Expected {} arguments'.format(len(fieldnames)))
        else:
            return tuple.__new__(cls, args)

    cls_dict['__new__'] = __new__

    # Make the class
    cls = types.new_class(classname, (tuple,), {},
                          lambda ns: ns.update(cls_dict))

    # Set the module to that of the caller
    cls.__module__ = sys._getframe(1).f_globals['__name__']
    return cls


if __name__ == '__main__':
    Point = named_tuple('Point', ['x', 'y'])
    print(Point)
    p = Point(4, 5)
    print(len(p))
    print(p.x, p[0])
    print(p.y, p[1])

    try:
        p.x = 2
    except AttributeError as e:
        print(e)

    print('%s %s' % p)
