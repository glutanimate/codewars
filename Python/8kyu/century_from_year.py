# -*- coding: utf-8 -*-
""" Century_From_Year !!!!!!!!!!

Description:

Given a year, return the century it is in.

The first century spans from the year 1 up to and including the year 100,
the second - from the year 101 up to and including the year 200, etc.

Let's see some examples:

centuryFromYear(1705) // returns 18
centuryFromYear(1900) // returns 19
centuryFromYear(1601) // returns 17
centuryFromYear(2000) // returns 20
Hope you enjoy it .. Awaiting for Best Practice Codes hahaha ..

Enjoy Learning !!!

NOTE: for C++, cmath (i.e. math.h) is disallowed in this Kata, in particular the ceil function; otherwise, what is the fun of this Kata? ;)


Tags: FUNDAMENTALSNUMBERSMATHEMATICSALGORITHMSBASIC LANGUAGE FEATURESDATES/TIME

Link: https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097/solutions/python
"""

#############################################################
#                        MY SOLUTIONS                       #
#############################################################

def century(year):
    cent = year // 100
    if year % 100:
        cent += 1
    return cent


#############################################################
#             OTHER INTERESTING SOLUTIONS & REMARKS         #
#############################################################

# beautifully simple using ceiling division:
def century(year):
    return (year + 99) // 100


#############################################################
#                           TESTS                           #
#############################################################

import sys, os
sys.path.append(os.path.abspath(
                os.path.join(os.path.dirname(__file__), '..', "tests")))
from Test import *


