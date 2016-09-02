#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You are running multiple instances of the Python interpreter, possibly on
different machines, and you would like to exchange data between interpreters
using messages.
"""


"""
SOLUTION
"""

from multiprocessing.connection import Client

c = Client(('localhost', 25000), authkey=b'peekaboo')

c.send('hello')
print('Got: ', c.recv())

c.send(42)
print('Got: ', c.recv())

c.send([1, 2, 3, 4, 5])
print('Got: ', c.recv())
