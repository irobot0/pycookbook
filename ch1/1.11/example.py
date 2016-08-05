#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PROBLEM

Your program has become an unreadable mess of heardcoded slice indices and you
want to clean it up.
"""


"""
SOLUTION
"""

######    0123456789012345678901234567890123456789012345678901234567890'
record = '....................100          .......513.25     ..........'

SHARES = slice(20, 32)
PRICE = slice(40, 48)

cost = int(record[SHARES]) * float(record[PRICE])
print(cost)


"""
DISCUSSION
"""

items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[2:4])
print(items[a])
items[a] = [10, 11]
print(items)
del items[a]
print(items)

a = slice(10, 50, 2)
print(a.start)
print(a.stop)
print(a.step)

s = 'HelloWorld'
print(a.indices(len(s)))
for i in range(*a.indices(len(s))):
    print(s[i])
