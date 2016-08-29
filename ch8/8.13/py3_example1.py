#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to define various kinds of data structures, but want to enforce
constraints on the values that are allowed to be assigned to certain attributes.
"""


"""
SOLUTION
"""


# Base class. Uses a descriptor to set a value
class Descriptor:
    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


# Descriptor for enforcing types
class Typed(Descriptor):
    expected_type = type(None)

    def __set__(self, instance, value):
        if isinstance(value, self.expected_type):
            super().__set__(instance, value)
        else:
            raise TypeError('Expected ' + str(self.expected_type) + '.')


# Descriptor for enforcing values
class Unsigned(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Expected >= 0.')
        else:
            super().__set__(instance, value)


class MaxSized(Descriptor):
    def __init__(self, name=None, **opts):
        if 'size' in opts:
            super().__init__(name, **opts)
        else:
            raise ValueError('Missing size option.')

    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError('Size must be < ' + str(self.size) + '.')
        else:
            super().__set__(instance, value)


class Integer(Typed):
    expected_type = int


class UnsignedInteger(Integer, Unsigned):
    pass


class Float(Typed):
    expected_type = float


class UnsignedFloat(Float, Unsigned):
    pass


class String(Typed):
    expected_type = str


class SizedString(String, MaxSized):
    pass


class Stock:
    # Specify constraints
    name = SizedString('name', size=8)
    shares = UnsignedInteger('shares')
    price = UnsignedFloat('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


s = Stock('ACME', 50, 91.1)
print(s.name)
print(s.shares)
print(s.price)

# s.shares = 75
# s.shares = -10
# s.price = 'a lot'
# s.name = 'ABRACADABRA'


# Class decorator to apply constraints
def check_attributes(**kwargs):
    def decorate(cls):
        for key, value in kwargs.items():
            if isinstance(value, Descriptor):
                value.name = key
                setattr(cls, key, value)
            else:
                setattr(cls, key, value(key))
        return cls
    return decorate


# Example
@check_attributes(name=SizedString(size=8),
                  shares=UnsignedInteger,
                  price=UnsignedFloat)
class Stock2:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


# A metaclass that applies checking
class checkedmeta(type):
    def __new__(cls, clsname, bases, methods):
        # Attach attribute names to the descriptors
        for key, value in methods.items():
            if isinstance(value, Descriptor):
                value.name = key
        return type.__new__(cls, clsname, bases, methods)


# Example
class Stock3(metaclass=checkedmeta):
    name = SizedString(size=8)
    shares = UnsignedInteger()
    price = UnsignedFloat()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
