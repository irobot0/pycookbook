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
import time


def time_server(address):
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(address)
    while True:
        msg, addr = sock.recvfrom(8192)
        print('Got message from', addr)
        resp = time.ctime()
        sock.sendto(resp.encode('ascii'), addr)


if __name__ == '__main__':
    time_server(('', 20000))
