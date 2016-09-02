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

from socketserver import BaseRequestHandler
from socketserver import TCPServer


class EchoHandler(BaseRequestHandler):
    def handler(self):
        print('Got connection from', self.client_address)
        while True:
            msg = self.request.recv(8192)
            if not msg:
                break
            self.request.send(msg)


if __name__ == '__main__':
    serv = TCPServer(('', 20000), EchoHandler)
    print('Echo server running on port 20000')
    serv.serve_forever()
