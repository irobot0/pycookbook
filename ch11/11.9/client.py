#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want a simple way to authenticate the clients connecting to servers in a
distributed system, but don’t need the complexity of something like SSL.
"""


"""
SOLUTION
"""

from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM
from auth import client_authenticate

secret_key = b'peekaboo'

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 18000))
client_authenticate(s, secret_key)
s.send(b'Hello World')
resp = s.recv(1024)
print('Got:', resp)
