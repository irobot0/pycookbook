#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PROBLEM

You want to sort objects of the same class, but they don’t natively support
comparison operations.
"""


"""
SOLUTION FOR HASHABLE ELEMENTS
"""


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

# Example
users = [User(23), User(3), User(99)]
print(users)

# Sort it by user_id
print(sorted(users, key=lambda u: u.user_id))

# Using operator.attrgetter()
from operator import attrgetter
print(sorted(users, key=attrgetter('user_id')))


"""
DISCUSSION
"""

by_name = sorted(users, key=attrgetter('user_id'))
print(by_name)

print(min(users, key=attrgetter('user_id')))
print(max(users, key=attrgetter('user_id')))
