#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PROBLEM

You want to match or search text for a specific pattern.
"""


"""
SOLUTION
"""

text = 'yeah, but no, but yeah, but no, but yeah'

# Exact match
print(text == 'yeah')

# Match at start or end
print(text.startswith('yeah'))
print(text.endswith('no'))

# Search for the location of the first occurence
text.find('no')

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re

# Simple matching: \d+ means match one or more digits
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')

datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')

if datepat.match(text2):
    print('yes')
else:
    print('no')

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))

# Using capture groups
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

m = datepat.match('11/27/2012')
print(m)

# Extract the contents of each groups
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())
month, day, year = m.groups()

# Find all matches (notice splitting into tuples)
print(text)
print(datepat.findall(text))
for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))

# Match text iteratively
for m in datepat.finditer(text):
    print(m.groups())


"""
DISCUSSION
"""

m = datepat.match('11/27/2012abcdef')
print(m)
print(m.group())

# Exact match with terminator $
datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
print(datepat.match('11/27/2012abcdef'))
print(datepat.match('11/27/2012'))
print(re.findall(r'(\d+)/(\d+)/(\d+)', text))
