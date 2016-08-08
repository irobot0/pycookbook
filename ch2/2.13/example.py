#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PROBLEM

You need to format text with some sort of alignment applied.
"""


"""
SOLUTION
"""

text = 'Hello World'
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))

print(text.rjust(20, '='))
print(text.center(20, '*'))

print(format(text, '>20'))
print(format(text, '<20'))
print(format(text, '^20'))

print(format(text, '=>20s'))
print(format(text, '*^20s'))

print('{:>10s} {:>10s}'.format('Hello', 'World'))

x = 1.2345
print(format(x, '>10'))
print(format(x, '^10.2f'))


"""
DISCUSSION
"""

print('%-20s' % text)
print('%20s' % text)
