#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to pick random items out of a sequence or generate random numbers.
"""


"""
SOLUTION
"""

import random

values = [1, 2, 3, 4, 5, 6]
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))

print(random.sample(values, 2))
print(random.sample(values, 2))
print(random.sample(values, 3))
print(random.sample(values, 3))

random.shuffle(values)
print(values)
random.shuffle(values)
print(values)

print(random.randint(0, 10))
print(random.randint(0, 10))
print(random.randint(0, 10))
print(random.randint(0, 10))
print(random.randint(0, 10))
print(random.randint(0, 10))

print(random.random())
print(random.random())
print(random.random())

print(random.getrandbits(200))

"""
DISCUSSION
"""

random.seed()
random.seed(12345)
random.seed(b'bytedata')
