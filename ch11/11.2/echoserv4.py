#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to implement a server that communicates with clients using the TCP
Internet protocol.
"""


"""
SOLUTION
"""

from socketserver import StreamRequestHandler
from socketserver import TCPServer
import socket


class EchoHandler(StreamRequestHandler):
    timeout = 5
    rbufsize = -1
    wbufsize = 0
    disable_nagle_algorithm = False
    def handler(self):
        print('Got connection from', self.client_address)
        # self.rfile is a file-like object for reading
        try:
            for line in self.rfile:
                # self.wfile is a file-like object for writing
                self.wfile.write(line)
        except socket.timeout:
            print('Time out!')


if __name__ == '__main__':
    serv = TCPServer(('', 20000), EchoHandler)
    print('Echo server running on port 20000')
    serv.serve_forever()
