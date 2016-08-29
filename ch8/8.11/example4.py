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


class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
