#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

Within a subclass, you want to extend the functionality of a property defined
in a parent class.
"""


"""
SOLUTION
"""


class Person:
    def __init__(self, name):
        self.name = name

    # Getter function
    @property
    def name(self):
        return self.name

    # Setter function
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.name = value
        else:
            raise TypeError('Expected a string')

    # Deleter function (optional)
    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")


class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Delete name')
        super(SubPerson, SubPerson).name.__delete__(self)


s = SubPerson('Guido')
print(s.name)
s.name = 'Larry'
# s.name = 42


class SubPerson2(Person):
    @Person.name.getter
    def name(self):
        print('Getting name')
        return super().name


class SubPerson3(Person):
    @Person.name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)


s = SubPerson('Guido')
print(s.name)
s.name = 'Larry'
print(s.name)
# s.name = 42


# A descriptor
class String:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__(self.name)

    def __set__(self, instance, value):
        if isinstance(value, str):
            instance.__dict__[self.name] = value
        else:
            raise TypeError('Expected a string')


# A class with a descriptor
class Person2:
    name = String('name')

    def __init__(self, name):
        self.name = name


# Extending a descriptor with a property
class SubPerson4(Person2):
    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson4, SubPerson4).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson4, SubPerson4).name.__delete__(self)
