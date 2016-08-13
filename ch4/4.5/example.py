#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to iterate in reverse over a sequence.
"""


"""
SOLUTION
"""

a = [1, 2, 3, 4]

for x in reversed(a):
    print(x)

# Print a file backwards
f = open('example.py')
for line in reversed(list(f)):
    print(line)


"""
DISCUSSION
"""

class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n = n - 1

    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n < self.start:
            yield n
            n = n + 1

c = Countdown(12)
for item in reversed(c):
    print(item)
