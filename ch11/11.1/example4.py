#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You need to access various services via HTTP as a client. For example,
downloading data or interacting with a REST-based API.
"""


"""
SOLUTION

NOTE: Before running the code below, make sure you have the requests package
      installed (running 'sudo pip install requests').
"""

# Example of a HEAD request

import requests

resp = requests.head('http://www.example.com/index.html')

status = resp.status_code
last_modified = resp.headers['last-modified']
content_type = resp.headers['content-type']
content_length = resp.headers['content-length']

print(status)
print(last_modified)
print(content_type)
print(content_length)
