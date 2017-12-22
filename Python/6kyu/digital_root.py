""" Sum of Digits / Digital Root

In this kata, you must create a digital root function.

A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that value has two digits, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.

Here's how it works (Ruby example given):

digital_root(16)
=> 1 + 6
=> 7

digital_root(942)
=> 9 + 4 + 2
=> 15 ...
=> 1 + 5
=> 6

digital_root(132189)
=> 1 + 3 + 2 + 1 + 8 + 9
=> 24 ...
=> 2 + 4
=> 6

digital_root(493193)
=> 4 + 9 + 3 + 1 + 9 + 3
=> 29 ...
=> 2 + 9
=> 11 ...
=> 1 + 1
=> 2

Tags: ALGORITHMS, MATHEMATICS, NUMBERS, ARITHMETIC

Link: https://www.codewars.com/kata/sum-of-digits-slash-digital-root
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

def digital_root(n):
    while n >= 10:
        n = sum(int(i) for i in str(n))
    return n



#############################################################
#             OTHER INTERESTING SOLUTIONS & REMARKS         #
#############################################################


def digital_root2(n):
    return n % 9 or n and 9


#############################################################
#                           TESTS                           #
#############################################################

test.assert_equals(digital_root(16), 7)
test.assert_equals(digital_root(195), 6)
test.assert_equals(digital_root(992), 2)
test.assert_equals(digital_root(999999999999), 9)
test.assert_equals(digital_root(167346), 9)
test.assert_equals(digital_root(0), 0)
