#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to read or write data encoded as JSON (JavaScript Object Notation).
"""


"""
SOLUTION
"""

import json

data = {
    'name'      :   'ACME',
    'shares'    :   100,
    'price'     :   542.23
}

json_str = json.dumps(data)

print(json_str)

data = json.loads(json_str)

print(data)

# Writing JSON data
with open('data.json', 'w') as f:
    json.dump(data, f)

# Reading data back
with open('data.json', 'r') as f:
    data = json.load(f)
    print(data)


"""
DISCUSSION
"""

print(json.dumps(False))

d = {
    'a' : True,
    'b' : 'Hello',
    'c' : None
}

print(json.dumps(d))

from urllib.request import urlopen

u = urlopen('https://slack.com/api/api.test')
resp = json.loads(u.read().decode('utf-8'))

from pprint import pprint
pprint(resp)

s = '{"name": "ACME", "shares": 50, "price": 490.1}'
from collections import OrderedDict
data = json.loads(s, object_pairs_hook=OrderedDict)
print(data)


class JSONObject:
    def __init__(self, d):
        self.__dict__ = d


data = json.loads(s, object_hook=JSONObject)
print(data.name)
print(data.shares)
print(data.price)

data = json.loads(s)
print(json.dumps(data))
print(json.dumps(data, indent=4))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def serialize_instance(obj):
    d = {
        '__classname__' : type(obj).__name__
    }
    d.update(vars(obj))
    return d


# Dictionary mapping names to known classed
classes = {
    'Point' : Point
}

def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)  # Make instance without calling __init__
        for key, value in d.items():
            setattr(obj, key, value)
        return obj
    else:
        return d


p = Point(2, 3)
s = json.dumps(p, default=serialize_instance)
print(s)
a = json.loads(s, object_hook=unserialize_object)
print(a)
print(a.x)
print(a.y)
