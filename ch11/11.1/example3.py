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

# A POST request using requests library

import requests

# Base URL being accessed
url = 'http://httpbin.org/post'

# Dictionary of query parameters (if any)
params = {
    'name1' : 'value1',
    'name2' : 'value2'
}

# Extra headers
headers = {
    'User-agent'    :   'none/ofyourbusiness',
    'Spam'          :   'Eggs'
}

resp = requests.post(url, data=params, headers=headers)

# Decode text returned by the request
text = resp.text

from pprint import pprint
pprint(resp.json)
