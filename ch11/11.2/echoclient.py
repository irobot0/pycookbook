#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to implement a server that communicates with clients using the TCP
Internet protocol.
"""


"""
SOLUTION
"""

from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 20000))

s.send(b'Hello')
resp = s.recv(8192)
print('Response: ', resp)
s.close()
