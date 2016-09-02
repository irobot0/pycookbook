#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You need to access various services via HTTP as a client. For example,
downloading data or interacting with a REST-based API.
"""


"""
SOLUTION
"""

# A basic POST request

from urllib import request
from urllib import parse

# Base URL being accessed
url = 'http://httpbin.org/post'

# Dictionary of query parameters (if any)
params = {
    'name1' : 'value1',
    'name2' : 'value2'
}

# Encode the query string
querystring = parse.urlencode(params)

# Make a GET request and read the response
u = request.urlopen(url, querystring.encode('ascii'))
resp = u.read()

import json
from pprint import pprint

json_resp = json.loads(resp.decode('utf-8'))
pprint(json_resp)
