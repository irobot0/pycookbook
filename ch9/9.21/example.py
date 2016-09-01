#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You are writing classes where you are repeatedly having to define property
methods that perform common tasks, such as type checking. You would like to
simplify the code so there is not so much code repetition.
"""


"""
SOLUTION
"""


def typed_property(name, expected_type):

    storage_name = '_' + name

    @property
    def prop(self):
        return getattr(self, storage_name)

    @prop.setter
    def prop(self, value):
        if isinstance(value, expected_type):
            setattr(self, storage_name, value)
        else:
            raise TypeError('{} must be a {}'.format(name, expected_type))

    return prop


# Example use
class Person:
    name = typed_property('name', str)
    age = typed_property('age', int)

    def __init__(self, name, age):
        self.name = name
        self.age = age


from functools import partial

String = partial(typed_property, expected_type=str)
Integer = partial(typed_property, expected_type=int)


# Example 2
class Person2:
    name = String('name')
    age = Integer('age')

    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':

    p = Person('Dave', 39)
    p.name = 'Guido'
    print('name: {}'.format(p.name))
    try:
        p.age = 'Old'
    except TypeError as e:
        print(e)
    else:
        print('age: {}'.format(p.age))
    print('')

    p2 = Person2('James', 39)
    p2.name = 'Vanderr'
    print('name: {}'.format(p2.name))
    try:
        p2.age = '42'
    except TypeError as e:
        print(e)
    else:
        print('age: {}'.format(p2.age))
