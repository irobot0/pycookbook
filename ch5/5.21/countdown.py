#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You need to serialize a Python object into a byte stream so that you can do
things such as save it to a file, store it in a database, or transmit it over a
network connection.
"""


"""
DISCUSSION
"""

import time
import threading

class CountDown:
    def __init__(self, n):
        self.n = n
        self.thr = threading.Thread(target=self.run)
        self.thr.daemon = True
        self.thr.start()

    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n = self.n - 1
            time.sleep(5)

    def __getstate__(self):
        return self.n

    def __setstate__(self, n):
        self.__init__(n)
