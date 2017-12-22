#!/usr/bin/python3

"""
Counting Duplicates

Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example

"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (bandB)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice

https://www.codewars.com/kata/counting-duplicates/train/python
"""

import timeit

# Solution using collections

from collections import Counter


def duplicate_count(text):
    counter = Counter(text.lower())
    by_frequency = counter.most_common()
    return sum(1 for i in by_frequency if i[1] > 1)


print(timeit.timeit('duplicate_count("abcde")',
                    setup="from __main__ import duplicate_count"))


# Barebones solution – much faster, interestingly

def duplicate_count(text):
    frequencies = {}
    for c in text.lower():
        try:
            frequencies[c] += 1
        except KeyError:
            frequencies[c] = 1
    return sum(1 for i in frequencies.values() if i > 1)  


print(timeit.timeit('duplicate_count("abcde")',
                    setup="from __main__ import duplicate_count"))
