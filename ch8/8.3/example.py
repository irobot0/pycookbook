#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to make your objects support the context-management protocol (the with
statement).
"""


"""
SOLUTION
"""

from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM


class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        else:
            self.sock = socket(self.family, self.type)
            self.sock.connect(self.address)
            return self.sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None


class LazyConnection2:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.connections = []

    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.connections.pop().close()


if __name__ == '__main__':
    from functools import partial

    conn = LazyConnection(('www.python.org', 80))
    # Connection closed
    with conn as s:
        # conn.__enter__() executes: connection open
        s.send(b'GET /index.html HTTP/1.0\r\n')
        s.send(b'Host: www.python.org\r\n')
        s.send(b'\r\n')
        resp = b''.join(iter(partial(s.recv, 8192), b''))
        print(resp)
        print('')
        # conn.__exit__() executes: connection closed

    conn2 = LazyConnection2(('www.python.org', 80))
    # Connection s1 and Connection s2 closed
    with conn2 as s1:
        # conn.__enter__() executes: connection s1 open
        s1.send(b'GET /index.html HTTP/1.0\r\n')
        s1.send(b'Host: www.python.org\r\n')
        s1.send(b'\r\n')
        resp = b''.join(iter(partial(s1.recv, 8192), b''))
        print(resp)
        print('')

        with conn2 as s2:
            # conn.__enter__() executes: connection s2 open
            s2.send(b'GET /index.html HTTP/1.0\r\n')
            s2.send(b'Host: www.python.org\r\n')
            s2.send(b'\r\n')
            resp = b''.join(iter(partial(s2.recv, 8192), b''))
            print(resp)
            print('')
            # conn.__exit__() executes: connection s2 closed

        # conn.__exit__() executes: connection s1 closed
