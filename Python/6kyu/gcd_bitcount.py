""" Greatest Common Divisor Bitcount

The objective is to write a method that takes two integer parameters and returns a single integer equal to the number of 1s in the binary representation of the greatest common divisor of the parameters.

Taken from Wikipedia: "In mathematics, the greatest common divisor (gcd) of two or more integers, when at least one of them is not zero, is the largest positive integer that divides the numbers without a remainder. For example, the GCD of 8 and 12 is 4."

For example: the greatest common divisor of 300 and 45 is 15. The binary representation of 15 is 1111, so the correct output would be 4.

If both parameters are 0, the method should return 0. The function must be able to handle negative input.

Tags: ALGORITHMS BINARY

Link: https://www.codewars.com/kata/greatest-common-divisor-bitcount/python"""

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

from fractions import gcd


def binary_gcd(x, y):
    return str(bin(gcd(x, y))).count("1")



#############################################################
#                           TESTS                           #
#############################################################


test.describe("Example tests")


def run_test(x, y, a):
    msg = "Oh no! binary_gcd({}, {}) returned".format(x, y)
    test.assert_equals(binary_gcd(x, y), a, msg)


run_test(666666, 333111, 6)
run_test(545034, 5, 1)
run_test(0, 0, 0)
run_test(0, 76899299, 14)
run_test(666666, 333111, 6)
run_test(-124, -16, 1)

test.describe("Random tests")
import random


def known_binary_gcd(x, y):
    a, b = x, y
    while b != 0:
        a, b = b, a % b
    gcd = a if a > 0 else -a
    result = len([c for c in str(bin(gcd)) if c == '1'])
    return result


def r(n): return random.randint(0, n) if n > 0 else -random.randint(0, -n)


bases = [r(n) for n in [30, 20, 100, 620, -12]]
tests = [r(n) for n in [3, -4, 6, -8, 10, 12, 17, 21, 99,
                        644, 32, 700, -500, 50, 50, -50, 3, 33, -35]]
for base_val in bases:
    for test_val in tests:
        run_test(base_val, test_val, known_binary_gcd(base_val, test_val))


#############################################################
#                      COMMENTS, ETC.                       #
#############################################################
