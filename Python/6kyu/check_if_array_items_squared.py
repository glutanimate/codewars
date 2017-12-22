""" Are they the "same"?

Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure) that checks whether the two arrays have the "same" elements, with the same multiplicities. "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

Examples

Valid arrays

a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121, 20736 the square of 144, 361 the square of 19, 25921 the square of 161, and so on. It gets obvious if we write b's elements in terms of squares:

a = [121, 144, 19, 161, 19, 144, 19, 11] 
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
Invalid arrays

If we change the first number to something else, comp may not return true anymore:

a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a,b) returns false because in b 132 is not the square of any number of a.

a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
comp(a,b) returns false because in b 36100 is not the square of any number of a.

Remarks

a or b might be [] (all languages except R, Shell). a or b might be nil or null or None (except in Haskell, Elixir, C++, Rust, R, Shell).

If a or b are nil (or null or None), the problem doesn't make sense so return false.

If a or b are empty the result is evident by itself.

Note for C

The two arrays have the same size (> 0) given as parameter in function comp.

Tags: FUNDAMENTALS

Link: https://www.codewars.com/kata/are-they-the-same
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


def comp(array1, array2):
    if None in (array1, array2):
        return False
    comparr = [i**2 for i in array1]
    return sorted(comparr) == sorted(array2)


#############################################################
#             OTHER INTERESTING SOLUTIONS & REMARKS         #
#############################################################





#############################################################
#                           TESTS                           #
#############################################################


test.describe("Basic tests")
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11 * 11, 121 * 121, 144 * 144, 19 * 19,
      161 * 161, 19 * 19, 144 * 144, 19 * 19]
test.assert_equals(comp(a1, a2), True)
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11 * 21, 121 * 121, 144 * 144, 19 * 19,
      161 * 161, 19 * 19, 144 * 144, 19 * 19]
test.assert_equals(comp(a1, a2), False)
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11 * 11, 121 * 121, 144 * 144, 190 * 190,
      161 * 161, 19 * 19, 144 * 144, 19 * 19]
test.assert_equals(comp(a1, a2), False)
a1 = []
a2 = []
test.assert_equals(comp(a1, a2), True)
a1 = []
a2 = None
test.assert_equals(comp(a1, a2), False)
a1 = [121, 144, 19, 161, 19, 144, 19, 11, 1008]
a2 = [11 * 11, 121 * 121, 144 * 144, 190 * 190,
      161 * 161, 19 * 19, 144 * 144, 19 * 19]
test.assert_equals(comp(a1, a2), False)
a1 = [10000000, 100000000]
a2 = [10000000 * 10000000, 100000000 * 100000000]
test.assert_equals(comp(a1, a2), True)
a1 = [10000001, 100000000]
a2 = [10000000 * 10000000, 100000000 * 100000000]
test.assert_equals(comp(a1, a2), False)

test.describe("Random tests")
from random import randint


def sol(a1, a2): return sorted(a1) == sorted(
    [item**.5 for item in a2]) if a1 != None and a2 != None else False


for i in range(40):
    a1 = [randint(0, 100) for i in range(randint(1, 8))]
    a2 = [elem * elem for elem in a1]
    if randint(0, 1) == 1:
        a2[randint(0, len(a2) - 1)] += 1
    test.it("Testing for " + str(a1) + " and " + str(a2))
    test.assert_equals(comp(a1[:], a2[:]), sol(
        a1, a2), "It should work with random inputs too")
