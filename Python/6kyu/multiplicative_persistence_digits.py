""" Persistent Bugger.

Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

For example:

 persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.

 persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                       # 1*2*6 = 12, and finally 1*2 = 2.

 persistence(4) => 0   # Because 4 is already a one-digit number.
 persistence(39) # returns 3, because 3*9=27, 2*7=14, 1*4=4
                 # and 4 has only one digit

 persistence(999) # returns 4, because 9*9*9=729, 7*2*9=126,
                  # 1*2*6=12, and finally 1*2=2

 persistence(4) # returns 0, because 4 is already a one-digit number


Tags: FUNDAMENTALS NUMBERS

Link: https://www.codewars.com/kata/persistent-bugger
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

def persistence(n):
    c = 0
    while n > 9:
        k = 1
        for i in str(n):
            k *= int(i)
        n = k
        c += 1
    return c


#############################################################
#                           TESTS                           #
#############################################################

#import functools
from random import randint

#-----------------


def soluce(n):
        digits = [int(d) for d in str(n)]
        if (len(digits) == 1):
            return 0
        p = reduce(lambda x, y: x * y, digits, 1)
        return 1 + persistence(p)
#-----------------


test.it("Basic tests")
test.assert_equals(persistence(39), 3)
test.assert_equals(persistence(4), 0)
test.assert_equals(persistence(25), 2)
test.assert_equals(persistence(999), 4)
test.assert_equals(persistence(444), 3)

test.describe("Random tests")
for _ in xrange(50):
    n = randint(1, 500000)
    test.it("Testing for: " + str(n))
    test.assert_equals(persistence(n), soluce(n))


#############################################################
#                      COMMENTS, ETC.                       #
#############################################################



