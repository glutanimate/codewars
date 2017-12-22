""" Give me a Diamond

This kata is to practice simple string output. Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants a diamond string from James. Since James doesn't know how to make this happen, he needs your help.

###Task:

You need to return a string that displays a diamond shape on the screen using asterisk ("*") characters. Please see provided test cases for exact output format.

The shape that will be returned from print method resembles a diamond, where the number provided as input represents the number of *’s printed on the middle line. The line above and below will be centered and will have 2 less *’s than the middle line. This reduction by 2 *’s for each line continues until a line with a single * is printed at the top and bottom of the figure.

Return null if input is even number or negative (as it is not possible to print diamond with even number or negative number).

Please see provided test case(s) for examples.

Python Note

Since print is a reserved word in Python, Python students must implement the diamond(n) method instead, and return None for invalid input.

JS Note

JS students, like Python ones, must implement the diamond(n) method, and return null for invalid input.


Tags: FUNDAMENTALS, STRINGS

Link: https://www.codewars.com/kata/give-me-a-diamond
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


def diamond(n):
    if not n % 2 or n < 0:
        return None
    side = []
    k = 1
    while k < n:
        side.append(" " * ((n - k) / 2) + "*" * k)
        k += 2
    return "\n".join(side + ["*" * n] + list(reversed(side))) + "\n"


#############################################################
#             OTHER INTERESTING SOLUTIONS & REMARKS         #
#############################################################


def diamond2(n):
    if n > 0 and n % 2 == 1:
        diamond = ""
        for i in range(n):
            diamond += " " * abs((n / 2) - i)
            diamond += "*" * (n - abs((n - 1) - 2 * i))
            diamond += "\n"
        return diamond
    else:
        return None


#############################################################
#                           TESTS                           #
#############################################################


test.assert_equals(diamond(3), " *\n***\n *\n")
test.assert_equals(diamond(0), None)
test.assert_equals(diamond(2), None)
test.assert_equals(diamond(-1), None)
test.assert_equals(diamond(-2), None)


def known_diamond(n):
    if n % 2 == 0 or n < 0:
        return None
    result = []

    def append(c, n, nl):
        for _ in xrange(n):
            result.append(c)
        if nl:
            result.append('\n')
    indent = n // 2
    for i in xrange(indent, 0, -1):
        append(' ', i, False)
        append('*', n - 2 * i, True)
    append('*', n, True)
    for i in xrange(1, indent + 1):
        append(' ', i, False)
        append('*', n - 2 * i, True)
    return "".join(result)


test.assert_equals(diamond(5), known_diamond(5))
test.assert_equals(diamond(7), known_diamond(7))
test.assert_equals(diamond(15), known_diamond(15))
