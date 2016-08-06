#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PROBLEM

You need to execute a reduction function (e.g., sum(), min(), max()), but first
need to transform or filter the data.

"""


"""
SOLUTION
"""

nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)

# Determine if any .py file exist in a directory
import os
files = os.listdir('./')
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')

# Output a tuple as CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

# Data reduction across fields of a data structure
portfolio = [
    {'name':'GOOG', 'shares': 50},
    {'name':'YHOO', 'shares': 75},
    {'name':'AOL', 'shares': 20},
    {'name':'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)


"""
DISCUSSION
"""

s = sum((x * x for x in nums))  # Pass generator-expr as argument
print(s)
s = sum(x * x for x in nums)    # More elegant syntax
print(s)

# Using a temporary list
nums = [1, 2, 3, 4, 5]
s = sum([x * x for x in nums])
print(s)

# Original: Return 20
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)

# Alternative: Return {'name': 'AOL', 'shares':20}
min_shares = min(portfolio, key=lambda s: s['shares'])
print(min_shares)
