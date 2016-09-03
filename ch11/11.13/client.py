#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to send and receive large arrays of contiguous data across a network
connection, making as few copies of the data as possible.
"""


"""
SOLUTION
"""

from zerocopy import recv_into
import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(('localhost', 25000))

import numpy
arr = numpy.zeros(shape=50000000, dtype=float)
print(arr[0:10])
recv_into(arr, conn)
print(arr[0:10])
print(arr[-10:])
