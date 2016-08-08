#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PROBLEM

You want to create a string in which embedded variable names are substituted
with a string representation of a variable’s value.
"""


"""
SOLUTION
"""

s = '{name} has {n} messages.'
print(s.format(name='Guido', n=37))

name = 'Guido'
n = 37
print(s.format_map(vars()))

class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n


a = Info('Guido', 37)
print(s.format_map(vars(a)))

# The downside of format() and format_map() --- can not deal gracefully with
# missing values.
# print(s.format(name='Guido'))

class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'

del n
print(s.format_map(safesub(vars())))

import sys

def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))

name = 'Guido'
n = 37
print(sub('Hello {name}'))
print(sub('You have {n} messages.'))
print(sub('Your favorite color is {color}'))


"""
DISCUSSION
"""

name = 'Guido'
n = 37
# print('%(name) has %(n) messages.' % vars())

import string
s = string.Template('$name has $n messages.')
s.substitute(vars())
