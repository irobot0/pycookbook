#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to add extra processing (e.g., type checking or validation) to the
getting or setting of an instance attribute.
"""


"""
SOLUTION
"""

import math


class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    # Getter function
    @property
    def first_name(self):
        return self._first_name

    # Setter function
    @first_name.setter
    def first_name(self, value):
        if isinstance(value, str):
            self._first_name = value
        else:
            raise TypeError('Expected a string')

    # Deleter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")


class Person2:
    def __init__(self, first_name):
        self.set_first_name(first_name)

    # Getter function
    def get_first_name(self):
        return self._first_name

    # Setter function
    def set_first_name(self, value):
        if isinstance(value, str):
            self._first_name = value
        else:
            raise TypeError('Excepted a string')

    # Deleter function (optional)
    def del_first_name(self):
        raise AttributeError("Can't delete attribute")

    # Make a property from existing get/set methods
    name = property(get_first_name, set_first_name, del_first_name)


"""
DISCUSSION
"""


class Person3:
    def __init__(self, first_name):
        self.first_name = name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius


class Person4:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if isinstance(value, str):
            self._first_name = value
        else:
            raise TypeError('Expected a string')

    # Repeared property code, but for a different name (bad!)
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if isinstance(value, str):
            self._last_name = value
        else:
            raise TypeError('Expected a string')


if __name__ == '__main__':
    a = Person('Guido')
    print(a.first_name)

    # The following 2 statements will cause exception in Python 3.
    # a.first_name = 42
    # del a.first_name

    a = Person2('Guy')
    print(a._first_name)

    print(Person.first_name.fget)
    print(Person.first_name.fset)
    print(Person.first_name.fdel)

    c = Circle(4.0)
    print(c.radius)
    print(c.area)           # without using ()
    print(c.perimeter)      # without using ()

    p = Person2('Guido')
    print(p.get_first_name())
    p.set_first_name('Larry')
    print(p.get_first_name())
