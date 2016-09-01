#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to implement new kinds of context managers for use with the with
statement.
"""


"""
SOLUTION
"""

import time
from contextlib import contextmanager


@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        elapse = end - start
        print('{}: {}'.format(label, elapse))


# Example use
with timethis('counting'):
    n = 1000
    while n > 0:
        n = n - 1


@contextmanager
def list_transaction(orig_list):
    working = list(orig_list)
    yield working
    orig_list[:] = working


items = [1, 2, 3]

with list_transaction(items) as working:
    working.append(4)
    working.append(5)

print(items)


# with list_transaction(items) as working:
#     working.append(6)
#     working.append(7)
#     raise RuntimeError('oops')
#
# print(items)


"""
DISCUSSION
"""

class timethis2:
    def __init__(self, label):
        self.label = label

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_ty, exc_val, exc_tb):
        end = time.time()
        elapse = end - self.start
        print('{}: {}'.format(self.label, elapse))
