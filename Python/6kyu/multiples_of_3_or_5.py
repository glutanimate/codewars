""" Multiples of 3 or 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Note: If the number is a multiple of both 3 and 5, only count it once.
Courtesy of ProjectEuler.net

Tags: ALGORITHMS, MATHEMATICS, NUMBERS

Link: https://www.codewars.com/kata/multiples-of-3-or-5
"""

#############################################################
#                       TEST FRAMEWORK                      #
#############################################################

import sys, os
sys.path.append(os.path.abspath(
                os.path.join(os.path.dirname(__file__), '..', "tests")))
from Test import *


#############################################################
#                         SOLUTIONS                         #
#############################################################

def solution(number):
    return sum(i for i in range(1, number) if not i % 3 or not i % 5)


#############################################################
#                           TESTS                           #
#############################################################

test.describe("Multiples of 3 and 5")

test.it("should handle basic cases")
test.assert_equals(solution(10), 23)
test.assert_equals(solution(20), 78)

test.it("should handle zeroes")
test.assert_equals(solution(0), 0)
test.assert_equals(solution(1), 0)

test.it("should handle large numbers")
test.assert_equals(solution(200), 9168)


#############################################################
#                      COMMENTS, ETC.                       #
#############################################################



