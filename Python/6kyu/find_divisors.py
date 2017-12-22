""" Find the divisors!

Create a function named divisors/Divisors that takes an integer and returns an array with all of the integer's divisors(except for 1 and the number itself). If the number is prime return the string '(integer) is prime' (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).

Example:

divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"
You can assume that you will only get positive integers as inputs.


Tags: ALGORITHMS, MATHEMATICS, NUMBERS

Link: https://www.codewars.com/kata/find-the-divisors
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


def divisors(integer):
    div = [i for i in range(2, integer) if not integer % i]
    return div if div else str(integer) + " is prime"


#############################################################
#             OTHER INTERESTING SOLUTIONS & REMARKS         #
#############################################################


def divisors2(n):
    return [i for i in xrange(2, n) if not n % i] or '%d is prime' % n


def divisors3(n):

    divs = set()

    for t in range(2, int(n ** 0.5) + 1):
        div, mod = divmod(n, t)

    if mod == 0:
        divs.add(t)
        divs.add(div)

    return '{:d} is prime'.format(n) if len(divs) == 0 else sorted(list(divs))

#############################################################
#                           TESTS                           #
#############################################################



test.assert_equals(divisors(15), [3, 5])
test.assert_equals(divisors(253), [11, 23])
test.assert_equals(divisors(24), [2, 3, 4, 6, 8, 12])

test.assert_equals(divisors(13), "13 is prime")
test.assert_equals(divisors(3), "3 is prime")
test.assert_equals(divisors(29), "29 is prime")

