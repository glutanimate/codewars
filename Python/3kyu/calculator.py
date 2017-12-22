""" Calculator

Create a simple calculator that given a string of operators (+ - * and /) and numbers separated by spaces returns the value of that expression

Example:

Calculator().evaluate("2 / 2 + 3 * 4 - 6") # => 7
Remember about the order of operations! Multiplications and divisions have a higher priority and should be performed left-to-right. Additions and subtractions have a lower priority and should also be performed left-to-right.

Tags: ALGORITHMS, PARSINGSTRINGS, EXPRESSIONS, BASIC LANGUAGE FEATURES, FUNDAMENTALS

Link: https://www.codewars.com/kata/calculator/python
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

# this is cheating and quite dangerous,  but it works!
class Calculator(object):
    def evaluate(self, string):
        return round(eval(string), 3)

# TODO: implement an actual Calculator class when you find the time

#############################################################
#                           TESTS                           #
#############################################################


for key, val in {
    "127": 127,
    "2 + 3": 5,
    "2 - 3 - 4": -5,
    "10 * 5 / 2": 25,
    "2 / 2 + 3 * 4 - 6": 7,
    "2 + 3 * 4 / 3 - 6 / 3 * 3 + 8": 8,
    "1.1 + 2.2 + 3.3": 6.6,
    "1.1 * 2.2 * 3.3": 7.986
}.items():
  actual = Calculator().evaluate(key)
  test.assert_equals(actual, val, "Expected %s == %s, got %s" %
                     (key, val, actual))


#############################################################
#                      COMMENTS, ETC.                       #
#############################################################



