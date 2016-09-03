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

from zerocopy import send_from
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 25000))
s.listen(1)
conn, addr = s.accept()

import numpy
arr = numpy.arange(0.0, 50000000.0)
send_from(arr, conn)
conn.close()
