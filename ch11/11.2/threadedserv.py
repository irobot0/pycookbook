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


class EchoHandler(StreamRequestHandler):
    def handler(self):
        print('Got connection from', self.client_address)
        # self.rfile is a file-like object for reading
        for line in self.rfile:
            # self.wfile is a file-like object for writing
            self.wfile.write(line)


if __name__ == '__main__':

    from threading import Thread

    NWORKERS = 16
    serv = TCPServer(('', 20000), EchoHandler)
    for n in range(NWORKERS):
        t = Thread(target=serv.serve_forever)
        t.daemon = True
        t.start()
    print('Multithreaded server running on port 20000')
    serv.serve_forever()
