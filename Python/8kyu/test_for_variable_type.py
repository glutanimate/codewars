# -*- coding: utf-8 -*-
""" Who ate the cookie?

For this problem you must create a program that says who ate the last cookie. If the input is a string then "Zach" ate the cookie. If the input is a float or an int then "Monica" ate the cookie. If the input is anything else "the dog" ate the cookie. The way to return the statement is: "Who ate the last cookie? It was (name)!"

Ex: Input = "hi" --> Output = "Who ate the last cookie? It was Zach! (The reason you return Zach is because the input is a string)

Note: Make sure you return the correct message with correct spaces and punctuation.

Please leave feedback for this kata. Cheers!

Tags: FUNDAMENTALS

Link: https://www.codewars.com/kata/who-ate-the-cookie/train/python
"""

#############################################################
#                        MY SOLUTIONS                       #
#############################################################

# turns out that you can actually use these basic type classes as dict keys:
names = {str: "Zach", float: "Monica", int: "Monica"}

def cookie(x):
    return "Who ate the last cookie? It was {}!".format(names.get(type(x), "the dog"))



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

test.assert_equals(cookie("Ryan"), "Who ate the last cookie? It was Zach!")
test.assert_equals(cookie(2.3), "Who ate the last cookie? It was Monica!")
test.assert_equals(cookie(26), "Who ate the last cookie? It was Monica!")
test.assert_equals(cookie(True), "Who ate the last cookie? It was the dog!")