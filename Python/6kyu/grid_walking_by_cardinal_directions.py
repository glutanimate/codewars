""" Take a Ten Minute Walk

You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).

Tags: FUNDAMENTALS, ARRAYS

Link: https://www.codewars.com/kata/take-a-ten-minute-walk
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


def isValidWalk(walk):
    x = walk.count("n") - walk.count("s")
    y = walk.count("e") - walk.count("w")
    if len(walk) == 10 and x == 0 and y == 0:
        return True
    else:
        return False



#############################################################
#             OTHER INTERESTING SOLUTIONS & REMARKS         #
#############################################################

# the main issue with the implementation above is that it traverses the
# array 4 times, which is ok for smaller arrays, but can quickly
# amount to major performance issue as the istruction size increases

# top-voted answer. More elegant, but also traverses the array 4 times:
def isValidWalk2(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')


#############################################################
#                           TESTS                           #
#############################################################


