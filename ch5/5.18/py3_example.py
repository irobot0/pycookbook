#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You have an integer file descriptor correponding to an already open I/O channel
on the operating system (e.g., file, pipe, socket, etc.), and you want to wrap a
higher-level Python file object around it.
"""


"""
SOLUTION
"""

# Open a low-level file descriptor
import os
fd = os.open('somefile.txt', os.O_WRONLY | os.O_CREAT)

# Turn into a proper file
# Create a file object, but don't close underlying fd when this file is closed.
f = open(fd, 'wt', closefd=False)
f.write('hello world\n')
f.close()


"""
DISCUSSION
"""

from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM

def echo_client(client_sock, addr):
    print('Got connection from', addr)

    # Make text-mode file wrappers for socket reading/writing
    client_in = open(client_sock.fileno(), 'rt', encoding='latin-1',
                     closefd=False)
    client_out = open(client_sock.fileno(), 'wt', encoding='latin-1',
                      closefd=False)

    # Echo lines back to the client using file I/O
    for line in client_in:
        client_out.write(line)
        client_out.flush()

    client_sock.close()

def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    while True:
        client, addr = sock.accept()
        echo_client(client, addr)

import sys
# Create a binary-mode file for stdout
bstdout = open(sys.stdout.fileno(), 'wb', closefd=False)
bstdout.write(b'Hello World\n')
bstdout.flush()
