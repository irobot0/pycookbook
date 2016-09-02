#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to be able to control or interact with your program remotely over the
network using a simple REST-based interface. However, you don’t want to do it by
installing a full-fledged web programming framework.
"""


"""
SOLUTION
"""

from urllib.request import urlopen

u = urlopen('http://localhost:8080/hello?name=Guido')
print(u.read().decode('utf-8'))

u = urlopen('http://localhost:8080/localtime')
print(u.read().decode('utf-8'))
