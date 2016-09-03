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

import os
from multiprocessing.connection import Client
from multiprocessing.reduction import recv_handle
from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM


def worker(server_address):
    serv = Client(server_address, authkey=b'peekaboo')
    serv.send(os.getpid())
    while True:
        fd = recv_handle(serv)
        print('WORKER: GOT FD', fd)
        with socket(AF_INET, SOCK_STREAM, fileno=fd) as client:
            while True:
                msg = client.recv(1024)
                if msg is None:
                    break
                else:
                    print('WORKER: RECV {!r}'.format(msg))
                    client.send(msg)


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print('Usage: worker.py server_address', file=sys.stderr)
        raise SystemExit(1)
    else:
        worker(sys.argv[1])
