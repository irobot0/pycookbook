#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to implement a state machine or an object that operates in a number of
different states, but don’t want to litter your code with a lot of conditionals.
"""


"""
SOLUTION
"""


class Connection:
    def __init__(self):
        self.state = 'CLOSED'

    def read(self):
        if self.state == 'OPEN':
            print('reading')
        else:
            raise RuntimeError('Not open')

    def write(self, data):
        if self.state == 'OPEN':
            print('writing')
        else:
            raise RuntimeError('Not open')

    def open(self):
        if self.state == 'OPEN':
            raise RuntimeError('Already open')
        else:
            self.state == 'OPEN'

    def close(self):
        if self.state == 'CLOSED':
            raise RuntimeError('Already closed')
        else:
            self.state = 'CLOSED'
