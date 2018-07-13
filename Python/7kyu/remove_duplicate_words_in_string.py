# -*- coding: utf-8 -*-
""" Remove Duplicate Words

Your task is to remove all duplicate words from string, leaving only single words entries.

Example:

Input:

'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'

Output:

'alpha beta gamma delta'

Tags: FUNDAMENTALS, STRINGS, REGULAR EXPRESSIONS, DECLARATIVE PROGRAMMING, ADVANCED LANGUAGE FEATURES

Link: https://www.codewars.com/kata/remove-duplicate-words
"""

#############################################################
#                        MY SOLUTIONS                       #
#############################################################

# Conventional approach
def remove_duplicate_words(s):
    deduplicated = []
    for word in s.split():
        if word not in deduplicated:
            deduplicated.append(word)
    return " ".join(deduplicated)

# Note that the following does not work since set() loses the original order:
def remove_duplicate_words2(s):
    return " ".join(set(s.split()))


#############################################################
#             OTHER INTERESTING SOLUTIONS & REMARKS         #
#############################################################

# cf.: https://stackoverflow.com/questions/480214/how-do-you-remove-duplicates-from-a-list-whilst-preserving-order
#      https://www.peterbe.com/plog/uniqifiers-benchmark

# Approach using ordered dict, for Python 3.6+
# this is actually faster than the set hack below
def remove_duplicate_words3(s):
    return " ".join(dict.fromkeys(s.split()))

# set.add hack:
# Uses a separate set to keep track of unique values
# Relies on the fact that set.add always returns None
def remove_duplicate_words4(s):
    seq = s.split()
    seen = set()
    seen_add = seen.add
    return " ".join(x for x in seq if not (x in seen or seen_add(x)))


# Interesting solution using a generator, in case you only want
# to process the original list up to a certain point:
# (in this case of course it superfluous as we actually do need
#  to iterate over the entire list)
def remove_duplicate_words5(s):
    def f():
        seen = set()
        for word in s.split():
            if word in seen:
                continue
            seen.add(word)
            yield word
    return ' '.join(f())

# Another interesting solution: Build set, and then sort it out
# by looking at the original position of words in the string:
def remove_duplicate_words6(s):
    return ' '.join(sorted(set(s.split()), key=s.index))

#############################################################
#                           TESTS                           #
#############################################################


import sys
import os
sys.path.append(os.path.abspath(
                os.path.join(os.path.dirname(__file__), '..', "tests")))
from Test import *


import random
from string import ascii_letters as lets
Test.it("Basic tests")
Test.assert_equals(remove_duplicate_words(
    "alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"), "alpha beta gamma delta")
Test.assert_equals(remove_duplicate_words(
    "my cat is my cat fat"), "my cat is fat")


def randou8():
    def mnu8(s):
        a = set()
        b = a.add
        return ' '.join([x for x in s.split(" ") if not (x in a or b(x))])

    Test.it("Random tests")
    for i in range(0, 100):
        randWords = []
        for j in range(0, 10):
            c, cnt, randWord = random.randrange(8, 12), 0, ''
            while cnt < c:
                randWord += lets[random.randrange(0, len(lets))]
                cnt += 1
            randWords.append(randWord)
        repeat = random.randrange(1, len(randWords))
        for k in range(0, repeat):
            idx = random.randrange(2, len(randWords))
            randWords.insert(
                idx, randWords[random.randrange(0, len(randWords))])
        res = ' '.join(randWords)
        exp = mnu8(res)
        Test.assert_equals(remove_duplicate_words(res), exp)


randou8()
