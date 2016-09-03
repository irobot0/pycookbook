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

def send_from(arr, dest):
    view = memoryview(arr).cast('B')
    while len(view) > 0:
        nsent = dest.send(view)
        view = view[nsent:]


def recv_into(arr, source):
    view = memoryview(arr).cast('B')
    while len(view) > 0:
        nsent = source.recv_into(view)
        view = view[nsent:]
