# -*- coding: utf-8 -*-
""" Build Tower

Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *

Python: return a list;
JavaScript: returns an Array;
C#: returns a string[];
PHP: returns an array;
C++: returns a vector<string>;
Haskell: returns a [String];
Have fun!

for example, a tower of 3 floors looks like below

[
  '  *  ', 
  ' *** ', 
  '*****'
]
and a tower of 6 floors looks like below

[
  '     *     ', 
  '    ***    ', 
  '   *****   ', 
  '  *******  ', 
  ' ********* ', 
  '***********'
]
Go challenge Build Tower Advanced once you have finished this :)


Tags: FUNDAMENTALS, STRINGS, BASIC LANGUAGE FEATURES

Link: https://www.codewars.com/kata/build-tower
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


def tower_builder(n_floors):
    tower = []
    base = 1 + (n_floors - 1) * 2
    for i in range(0, n_floors):
        times = 1 + i * 2
        floor = "*" * times
        tower.append(floor.center(base))
    return tower


#############################################################
#             OTHER INTERESTING SOLUTIONS & REMARKS         #
#############################################################

# using str.center
def tower_builder2(n):
    return [("*" * (i * 2 - 1)).center(n * 2 - 1) for i in range(1, n + 1)]


#############################################################
#                           TESTS                           #
#############################################################



# Use test.describe (or Test.describe) to describe your test suite
test.describe("Tests")

# Use "it" calls to describe the specific test case
test.it("Blanket Test")

# assert equals will pass if both items equal each other (using ==). If
# the test fails, assert_equals will output a descriptive message indicating
# what the values were expected to be.


def sol(n_floors):
    floors = []
    n = n_floors
    for i in range(n_floors):
        n -= 1
        floors.append(' ' * n + '*' * (i * 2 + 1) + ' ' * n)

    return floors


for i in range(1, 101):
    test.assert_equals(tower_builder(i), sol(i))
