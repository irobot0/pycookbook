#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You are using exec() to execute a fragment of code in the scope of the caller,
but after execution, none of its results seem to be visible.
"""


"""
SOLUTION
"""

a = 13
exec('b = a + 1')
print(b)
print('')


def test():
    a = 13
    exec('b = a + 1')
    print(b)

test()
print('')


def test2():
    a = 13
    loc = locals()
    exec('b = a + 1')
    b = loc['b']
    print(b)

test2()
print('')


"""
DISCUSSION
"""

def test3():
    x = 0
    exec('x = x + 1')
    print(x)

test3()
print('')


def test4():
    x = 0
    loc = locals()
    print('before:', loc)
    exec('x = x + 1')
    print('after:', loc)
    print('x =', x)

test4()
print('')


def test5():
    x = 0
    loc = locals()
    print(loc)
    exec('x = x + 1')
    print(loc)
    locals()
    print(loc)

test5()
print('')


def test6():
    a = 13
    loc = { 'a' : a }
    glb = {}
    exec('b = a + 1', glb, loc)
    b = loc['b']
    print(b)

test6()
print('')
