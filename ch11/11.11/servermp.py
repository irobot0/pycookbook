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

from multiprocessing.connection import Listener
from multiprocessing.reduction import send_handle
import socket


def server(work_address, port):
    # Wait for the worker to connect
    work_serv = Listener(work_address, authkey=b'peekaboo')
    worker = work_serv.accept()
    worker_pid = worker.recv()

    # Now run a TCP/IP server and send clients to worker
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    s.bind(('', port))
    s.listen(1)

    while True:
        client, addr = s.accept()
        print('SERVER: Got connection from', addr)
        send_handle(worker, client.fileno(), worker_pid)
        client.close()


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print('Usage: server.py server_address port', file=sys.stderr)
        raise SystemExit(1)
    else:
        server(sys.argv[1], int(sys.argv[2]))
