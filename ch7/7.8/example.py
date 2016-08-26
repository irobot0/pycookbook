#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You have a callable that you would like to use with some other Python code,
possibly as a callback function or handler, but it takes too many arguments and
causes an exception when called.
"""


"""
SOLUTION
"""

import logging
import math
from multiprocessing import Pool
from functools import partial
from socketserver import StreamRequestHandler
from socketserver import TCPServer


def spam(a, b, c, d):
    print(a, b, c, d)


"""
DISCUSSION
"""

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)

def output_result(result, log=None):
    if log is not None:
        log.debug('Got: %r', result)

# A sample function
def add(x, y):
    return x + y


class EchoHandler(StreamRequestHandler):
    # ack is added keyword-only argument. *args, **kwargs are
    # any normal parameters supplied (which are passed on)
    def __init__(self, *args, ack, **kwargs):
        self.ack = ack
        super().__init__(*args, **kwargs)

    def handle(self):
        for line in self.rfile:
            self.wfile.write(b'GOT:' + line)


if __name__ == '__main__':

    s1 = partial(spam, 1)       # a = 1
    print(s1(2, 3, 4))
    print(s1(4, 5, 6))
    print('')

    s2 = partial(spam, d=42)    # d = 42
    print(s2(1, 2, 3))
    print(s2(4, 5, 5))
    print('')

    s3 = partial(spam, 1, 2, d=42)  # a = 1, b = 2, d = 42
    print(s3(3))
    print(s3(4))
    print(s3(5))
    print('')

    points = [ (1, 2), (3, 4), (5, 6), (7, 8) ]

    pt = (4, 3)
    points.sort(key=partial(distance, pt))
    points.sort(key=lambda p: distance(pt, p))
    print(points)
    print('')

    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger('test')

    p = Pool()
    p.apply_async(add, (3, 4), callback=partial(output_result, log=log))
    p.apply_async(add, (3, 4), callback=lambda result: output_result(result, log))
    p.close()
    p.join()

    serv = TCPServer(('', 15000), partial(EchoHandler, ack=b'RECEIVED:'))
    serv = TCPServer(('', 15001),
                     lambda *args, **kwargs: EchoHandler(*args,
                                                         ack=b'RECEIVED:',
                                                         **kwargs))
    serv.serve_forever()
