#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PROBLEM

You have code that accesses list or tuple elements by position, but this makes
the code somewhat difficult to read at times. You’d also like to be less
dependent on position in the structure, by accessing the elements by name.
"""


"""
SOLUTION
"""

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
print(sub.addr)
print(sub.joined)

print(len(sub))
addr, joined = sub
print(addr)
print(joined)

# Code that use ordinary tuple
def compute_cost(records):
    total = 0.0
    for rec in records:
        total = total + (rec[1] * rec[2])
    return total

Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total = total + (s.shares * s.price)
    return total


"""
DISCUSSION
"""

s = Stock('ACME', 100, 123.45)
print(s)

# Instances of namedtuple are immutable, which can not be modified.
# s.share = 75

# Alternatively, it can be done using the _replace() method of a namedtuple
# instance, which makes an entirely new namedtuple with specified values
# replace.
s = s._replace(shares=75)
print(s)

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

# Create a prototype instance.
stock_prototype = Stock('', 0, 0.0, None, None)

# Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)

a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))

b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(dict_to_stock(b))
