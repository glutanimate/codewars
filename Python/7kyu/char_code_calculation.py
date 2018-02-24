# -*- coding: utf-8 -*-
""" Char Code Calculation

Given a string, first turn each letter into its ASCII char code.

example:

'ABC' --> x=65, y=66, z=67 --> '656667'

Let's call this number 'total1'.

Then replace any incidence of the number 7, with the number 1.

'656667' ---> '656661'

Lets call this number 'total2'.

Then return the difference between the sum of the digits in total1 and total2:

  (6 + 5 + 6 + 6 + 6 + 7)
- (6 + 5 + 6 + 6 + 6 + 1)
-------------------------
                       6


Tags: FUNDAMENTALSARRAYSSTRINGSNUMBERSMATHEMATICSALGORITHMS

Link: https://www.codewars.com/kata/57f75cc397d62fc93d000059/solutions/python/me/best_practice
"""

#############################################################
#                        MY SOLUTIONS                       #
#############################################################


def calc(x):
    return "".join(str(ord(i)) for i in str(x)).count("7") * 6


#############################################################
#             OTHER INTERESTING SOLUTIONS & REMARKS         #
#############################################################





#############################################################
#                           TESTS                           #
#############################################################

import sys, os
sys.path.append(os.path.abspath(
                os.path.join(os.path.dirname(__file__), '..', "tests")))
from Test import *


def sumDig(nStr):
    return sum(map(int, list(nStr)))


def calc_randTests(x):
    total1 = ''
    for char in x:
        total1 += str(ord(char))
    total2 = ''
    for char_ in total1:
        if char_ == '7':
            char_ = '1'
        total2 += char_
    return sumDig(total1) - sumDig(total2)


test.describe("Basic Tests")
test.assert_equals(calc('abcdef'), 6)
test.assert_equals(calc('ifkhchlhfd'), 6)
test.assert_equals(calc('aaaaaddddr'), 30)
test.assert_equals(calc('jfmgklf8hglbe'), 6)
test.assert_equals(calc('jaam'), 12)

test.describe("Random Tests")
from random import randint, choice
names = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
         "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
for i in range(100):
    xL = []
    l = randint(1, 8)
    for k in range(l):
        name = choice(names)
        xL.append(name)
    x = ''.join(tuple(xL))
    test.it("Testing for " + x)
    result = calc_randTests(x)
    res = calc(x)
    test.assert_equals(res, result)
