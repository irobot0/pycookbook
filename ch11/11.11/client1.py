#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You have multiple Python interpreter processes running and you want to pass an
open file descriptor from one interpreter to the other. For instance, perhaps
there is a server process that is responsible for receiving connections, but
the actual servicing of clients is to be handled by a different interpreter.
"""


"""
SOLUTION
"""

from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 15000))
s.send(b'Hello\n')
print('Got: ', s.recv(8192))
s.send('Got: ', s.recv(8192))
s.close()
