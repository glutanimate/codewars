""" Don't rely on luck

The test fixture I use for this kata is pre-populated.

It will compare your guess to a random number generated using:

randint(1,100)
You can pass by relying on luck or skill but try not to rely on luck.

"The power to define the situation is the ultimate power." - Jerry Rubin

Good luck!

Tags: PUZZLES, GAME

Link: https://www.codewars.com/kata/dont-rely-on-luck/solutions/python
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


# cheating:
def randint(a, b):
    return 10

guess = 10


#############################################################
#             OTHER INTERESTING SOLUTIONS & REMARKS         #
#############################################################


# proper solution using seeds:

import random
from random import randint

# Seed and get the random state
random.seed('SEED')
state = random.getstate()

# Set our guess to a random number
guess = random.randint(1, 100)

# Restore the state so the next call gets the
# same number.
random.setstate(state)



# another clever solution that cheats the test suite:

from random import randint


class CheatingNumber:
    def __eq__(self, x):
        return True


guess = CheatingNumber()


#############################################################
#                           TESTS                           #
#############################################################


lucky_number = randint(1, 100)
test.assert_equals(guess, lucky_number, "Sorry. Unlucky this time.")
