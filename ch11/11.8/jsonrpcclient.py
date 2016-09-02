#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to implement simple remote procedure call (RPC) on top of a message
passing layer, such as sockets, multiprocessing connections, or ZeroMQ.
"""


"""
SOLUTION
"""

import json


class RPCProxy:

    def __init__(self, connection):
        self._connection = connection

    def __getattr__(self, name):
        def do_rpc(*args, **kwargs):
            self._connection.send(json.dumps((name, args, kwargs)))
            result = json.loads(self._connection.recv())
            if isinstance(result, Exception):
                raise result
            else:
                return result
        return do_rpc


# Example use
from multiprocessing.connection import Client

c = Client(('localhost', 17000), authkey=b'peekaboo')
proxy = RPCProxy(c)

print(proxy.add(2, 3))
print(proxy.sub(2, 3))
try:
    proxy.sub([1, 2], 4)
except Exception as e:
    print(e)
