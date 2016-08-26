#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You’ve defined an anonymous function using lambda, but you also need to capture
the values of certain variables at the time of definition.
"""


"""
SOLUTION
"""

x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y

print(a(10))
print(b(10))
print('')

x = 15
print(a(10))
x = 3
print(a(10))
print('')


x = 10
a = lambda y, x=x: x + y
x = 20
b = lambda y, x=x: x + y

print(a(10))
print(b(10))
print('')


"""
DISCUSSION
"""

funcs = [ lambda x: x+n for n in range(5) ]
for f in funcs:
    print(f(0))
print('')


funcs = [ lambda x, n=n: x+n for n in range(5) ]
for f in funcs:
    print(f(0))
print('')
