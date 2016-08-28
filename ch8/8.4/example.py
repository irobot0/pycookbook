#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

Your program creates a large number (e.g., millions) of instances and uses a
large amount of memory.
"""


"""
SOLUTION
"""


class Date:

    __slots__ = ['year', 'month', 'day']

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
