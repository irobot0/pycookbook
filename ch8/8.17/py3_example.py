#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You need to create an instance, but want to bypass the execution of the
__init__() method for some reason.
"""


"""
DISCUSSION
"""


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


d = Date.__new__(Date)
print(d)

data = {
    'year'  : 2012,
    'month' : 8,
    'day'   : 29
}

for key, value in data.items():
    setattr(d, key, value)

print(d.year)
print(d.month)
print('')


"""
DISCUSSION
"""

from time import localtime


class Date2:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        d = cls.__new__(cls)
        t = localtime()
        d.year = t.tm_year
        d.month = t.tm_mon
        d.day = t.tm_mday
        return d

    @classmethod
    def makedate(cls, data):
        d = cls.__new__(cls)
        for key, value in data.items():
            setattr(d, key, value)
        return d


d2 = Date2.makedate(data)
print(d2.year)
print(d2.month)
print(d2.day)
