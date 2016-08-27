#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You’re writing code that relies on the use of callback functions (e.g., event
handlers, completion callbacks, etc.), but you want to have the callback
function carry extra state for use inside the callback function.
"""


"""
SOLUTION
"""

def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)

    # Invoke the callback with the result
    callback(result)

def print_result(result):
    print('Got:', result)

def add(x, y):
    return x + y

apply_async(add, (2, 3), callback=print_result)
apply_async(add, ('hello', 'world'), callback=print_result)
print('')


# Using class
class ResultHandler:

    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence = self.sequence + 1
        print('[{}] Got: {}'.format(self.sequence, result))

r = ResultHandler()
apply_async(add, (2, 3), callback=r.handler)
apply_async(add, ('hello', 'world'), callback=r.handler)
print('')


# Using closure
def make_handler():
    sequence = 0
    def handler(result):
        nonlocal sequence
        sequence = sequence + 1
        print('[{}] Got: {}'.format(sequence, result))
    return handler

handler = make_handler()
apply_async(add, (2, 3), callback=handler)
apply_async(add, ('hello', 'world'), callback=handler)
print('')


# Using coroutine
def make_handler2():
    sequence = 0
    while True:
        result = yield
        sequence = 1
        print('[{}] Got: {}'.format(sequence, result))

handler = make_handler2()
next(handler)   # Advance to the yield
apply_async(add, (2, 3), callback=handler.send)
apply_async(add, ('hello', 'world'), callback=handler.send)
