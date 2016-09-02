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
from auth import server_authenticate

secret_key = b'peekaboo'


def echo_handler(client_sock):
    if server_authenticate(client_sock, secret_key):
        while True:
            msg = client_sock.recv(8192)
            if msg is None:
                break
            else:
                client_sock.sendall(msg)
    else:
        client_sock.close()
        return


def echo_server(address):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(5)
    while True:
        c, a = s.accept()
        echo_handler(c)


print('Echo server running on port 18000')

echo_server(('', 18000))
