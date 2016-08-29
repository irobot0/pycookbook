#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You are writing a lot of classes that serve as data structures, but you are
getting tired of writing highly repetitive and boilerplate __init__() functions.
"""


"""
DISCUSSION
"""


def init_fromlocals(self):
    import sys
    locs = sys._getframe(1).f_locals
    for k, v in locs.items():
        if k != 'self':
            setattr(self, k, v)


class Stock:
    def __init__(self, name, shares, price):
        init_fromlocals(self)
