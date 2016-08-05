#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PROBLEM

You want to perform various calculations (e.g., minimum value, maximum value,
sorting etc.) on a dictionary of data.
"""


"""
SOLUTION
"""

prices = {
    'ACME' : 45.32,
    'AAPL' : 612.78,
    'IBM' : 205.55,
    'HPQ' : 37.20,
    'FB' : 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
print(min_price)

max_price = max(zip(prices.values(), prices.keys()))
print(max_price)

# The iterator created by zip() can only consumed once on Python 3.5,
# while on Python 2.7, it can be cunsumed many times.
prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))
# print(max(prices_and_names))


"""
DISCUSSION
"""

print(min(prices))  # Print 'AAPL'
print(max(prices))  # Print 'IBMA'

print(min(prices.values())) # Print 10.75
print(max(prices.values())) # Print 612.78

print(min(prices, key=lambda k: prices[k])) # Print 'FB'
print(max(prices, key=lambda k: prices[k])) # Print 'AAPL'

min_value = prices[min(prices, key=lambda k: prices[k])]
print(min_value)

prices = {
    'AAA' : 45.23,
    'ZZZ' : 45.23
}

print(min(zip(prices.values(), prices.keys())))
print(max(zip(prices.values(), prices.keys())))
