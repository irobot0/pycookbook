#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You need to serialize a Python object into a byte stream so that you can do
things such as save it to a file, store it in a database, or transmit it over a
network connection.
"""


"""
SOLUTION
"""

import pickle

data = {
    'id' : 101,
    'name': 'Jim Weinberg'
}

f = open('somefile', 'wb')
pickle.dump(data, f)
f.close()

s = pickle.dumps(data)

# Restore from a file
f = open('somefile', 'rb')
data = pickle.load(f)
print(data)
f.close()

# Restore from a string
data = pickle.loads(s)
print(data)


"""
DISCUSSION
"""

f = open('somedata', 'wb')
pickle.dump([1, 2, 3, 4], f)
pickle.dump('hello', f)
pickle.dump({'Apple', 'Pear', 'Banana'}, f)
f.close()
f = open('somedata', 'rb')
print(pickle.load(f))
print(pickle.load(f))
print(pickle.load(f))

import math
print(pickle.dumps(math.cos))
