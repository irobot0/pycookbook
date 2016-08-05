#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PROBLEM

You have a sequence of items, and you'd like to determine the most frequently
occuring items in the sequence.
"""


"""
SOLUTION
"""

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)
# outputs [('eyes', 8), ('the', 5), ('look', 4)]


"""
DISCUSSION
"""

word_counts['not']
word_counts['eyes']

morewords = ['why','are','you','not','looking','in','my','eyes']
for word in morewords:
    word_counts[word] = word_counts[word] + 1
print(word_counts.most_common(3))

print(word_counts['eyes'])

# word_counts.update(morewords)

a = Counter(words)
b = Counter(morewords)
print(a)
print(b)

# Combine counts
c = a + b
print(c)

# Subtract counts
d = a - b
print(d)
