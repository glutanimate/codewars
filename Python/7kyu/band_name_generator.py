# -*- coding: utf-8 -*-
""" Band name generator

My friend wants a new band name for her band. She like bands that use the formula: 'The' + a noun with first letter capitalized.

dolphin -> The Dolphin

However, when a noun STARTS and ENDS with the same letter, she likes to repeat the noun twice and connect them together with the first and last letter, combined into one word like so (WITHOUT a 'The' in front):

alaska -> Alaskalaska

europe -> Europeurope

Can you write a function that takes in a noun as a string, and returns her preferred band name written as a string?


Tags: FUNDAMENTALS

Link: https://www.codewars.com/kata/59727ff285281a44e3000011/solutions/python
"""

#############################################################
#                        MY SOLUTIONS                       #
#############################################################


def band_name_generator(name):
    name = name.lower()
    if name[0] == name[-1]:
        return (name[:-1] + name).capitalize()
    return "The {}".format(name.capitalize())



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

test.describe("Basic tests")
test.assert_equals(band_name_generator("knife"), "The Knife")
test.assert_equals(band_name_generator("tart"), "Tartart")
test.assert_equals(band_name_generator("sandles"), "Sandlesandles")
test.assert_equals(band_name_generator("bed"), "The Bed")
test.assert_equals(band_name_generator("qq"), "Qqq")

test.describe("Random tests")
from random import randint


def sol(s): return (
    s + s[1:]).capitalize() if s[0] == s[-1] else "The " + s.capitalize()


base = "abcdefghijklmnopqrstuvwxyz"

for _ in range(40):
  s = "".join(base[randint(0, len(base) - 1)] for q in range(randint(1, 25)))
  test.it("Testing for " + repr(s))
  test.assert_equals(band_name_generator(s), sol(
      s), "It should work for random inputs too")
