""" Array.diff

Your goal in this kata is to implement an difference function, which subtracts one list from another.

It should remove all values from list a, which are present in list b.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]

Tags: FUNDAMENTALS, ARRAYS

Link: https://www.codewars.com/kata/array-dot-diff
"""

#############################################################
#                       TEST FRAMEWORK                      #
#############################################################

import sys, os
sys.path.append(os.path.abspath(
                os.path.join(os.path.dirname(__file__), '..', "tests")))
from Test import *


#############################################################
#                        MY SOLUTIONS                       #
#############################################################

def array_diff(a, b):
    return [i for i in a if i not in b]



#############################################################
#             OTHER INTERESTING SOLUTIONS & REMARKS         #
#############################################################




#############################################################
#                           TESTS                           #
#############################################################

test.describe("Basic Tests")
test.assert_equals(array_diff([1, 2], [1]), [2],
                   "a was [1,2], b was [1], expected [2]")
test.assert_equals(array_diff([1, 2, 2], [1]), [
                   2, 2], "a was [1,2,2], b was [1], expected [2,2]")
test.assert_equals(array_diff([1, 2, 2], [2]), [
                   1], "a was [1,2,2], b was [2], expected [1]")
test.assert_equals(array_diff([1, 2, 2], []), [
                   1, 2, 2], "a was [1,2,2], b was [], expected [1,2,2]")
test.assert_equals(array_diff([], [1, 2]), [],
                   "a was [], b was [1,2], expected []")
test.describe("Random Tests")
from random import randint


def array_sol(a, b): return [item for item in a if item not in b]


for _ in range(40):
    alen, blen = randint(0, 20), randint(0, 20)
    a = [randint(0, 40) - 20 for i in range(alen)]
    b = [randint(0, 40) - 20 for i in range(blen)]
    test.it(
        "Testing for array_diff([" + ", ".join(map(str, a)) + "],[" + ", ".join(map(str, b)) + "])")
    test.assert_equals(array_diff(a, b), array_sol(
        a, b), "Should work for random arrays too")
