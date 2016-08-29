#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You’re writing a class, but you want users to be able to create instances in
more than the one way provided by __init__().
"""


"""
DISCUSSION
"""

import time


class Date:
    # Primary constructor
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Alternate constructor
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


a = Date(2012, 12, 21)
b = Date.today()


"""
DISCUSSION
"""


class NewDate(Date):
    pass

c = Date.today()    # Creates an instance of Date (cls=Date)
d = NewDate.today() # Creates an instance of NewDate (cls=NewDate)
