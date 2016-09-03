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

import socket
import struct


def recv_fd(sock):
    '''
    Receive a single file descriptor
    '''
    msg, ancdata, flags, addr = sock.recvmsg(1,
                                        socket.CMSG_LEN(struct.calcsize('i')))

    cmsg_level, cmsg_type, cmsg_data = ancdata[0]
    assert cmsg_level == socket.SOL_SOCKET and cmsg_type == socket.SCM_RIGHTS
    sock.sendall(b'OK')

    return struct.unpack('i', cmsg_data)[0]


def worker(server_address):
    serv = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    serv.connect(server_address)
    while True:
        fd = recv_fd(serv)
        print('WORKER: GOT FD', fd)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM, fileno=fd) as client:
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
