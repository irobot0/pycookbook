#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to implement a server that communicates with clients using the UDP
Internet protocol.
"""


"""
SOLUTION
"""

from socket import socket
from socket import AF_INET
from socket import SOCK_DGRAM


s = socket(AF_INET, SOCK_DGRAM)
s.sendto(b'', ('localhost', 20000))
print(s.recvfrom(8192))
