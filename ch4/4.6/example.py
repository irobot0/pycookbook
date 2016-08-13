#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You would like to define a generator function, but it involves extra state that
you would like to expose to the user somehow.
"""


"""
SOLUTION
"""

from collections import deque


class LineHistory:
    def __init__(self, lines, hislen=3):
        self.lines =  lines
        self.history = deque(maxlen=hislen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


with open('somefile.txt') as f:
    lines = LineHistory(f)
    for line in lines:
        if 'python' in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline))


"""
DISCUSSION
"""

f = open('somefile.txt')
lines = LineHistory(f)

# Call iter() first, then start iterating
it = iter(lines)
print(next(it))
print(next(it))
