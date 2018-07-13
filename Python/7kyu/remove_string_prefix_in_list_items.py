# -*- coding: utf-8 -*-
""" Help the Fruit Guy

Our fruit guy has a bag of fruit (represented as an array of strings) where some fruits are rotten. He wants to replace all the rotten pieces of fruit with fresh ones. For example, given ["apple","rottenBanana","apple"] the replaced array should be ["apple","banana","apple"]. Your task is to implement a method that accepts an array of strings containing fruits should returns an array of strings where all the rotten fruits are replaced by good ones.

Notes
If the array is null/nil/None or empty you should return empty array ([]).
The rotten fruit name will be in this camelcase (rottenFruit).
The returned array should be in lowercase.


Tags: FUNDAMENTALS, ARRAYS, STRINGS

Link: https://www.codewars.com/kata/help-the-fruit-guy/train/python
"""

#############################################################
#                        MY SOLUTIONS                       #
#############################################################

# bag_of_fruits could be None, so check for that
def remove_rotten(bag_of_fruits):
    return [] if not bag_of_fruits else [w.replace("rotten", "").lower() for w in bag_of_fruits]



#############################################################
#             OTHER INTERESTING SOLUTIONS & REMARKS         #
#############################################################

# The solution above could break if the actual fruit names contain "rotten"
# in any place other than the beginning. A more generalized solution would
# have to either check whether the strings starts with the string in
# question and then only once replace it:

def showcase1(i):
    if i.startswith('rotten'):
        i = i.replace('rotten', '', 1)

# or use a RegEx to handle the replacements:


def showcase2(i):
    import re
    re.sub(r"^rotten", "", i)

#############################################################
#                           TESTS                           #
#############################################################

import sys, os
sys.path.append(os.path.abspath(
                os.path.join(os.path.dirname(__file__), '..', "tests")))
from Test import *


import random


def sol(bag_of_fruits):
    if bag_of_fruits is None:
        return []

    clean_bag = []

    for fruit in bag_of_fruits:
        if "rotten" in fruit:
            clean_bag.append(fruit.replace("rotten", "").lower())
        else:
            clean_bag.append(fruit)

  return clean_bag


Test.assert_equals(remove_rotten(["apple", "banana", "kiwi", "melone", "orange"]), [
                   "apple", "banana", "kiwi", "melone", "orange"])
Test.assert_equals(remove_rotten(["rottenApple", "rottenBanana", "rottenApple", "rottenPineapple", "rottenKiwi"]), [
                   "apple", "banana", "apple", "pineapple", "kiwi"])
Test.assert_equals(remove_rotten([]), [])
Test.assert_equals(remove_rotten(None), [])
Test.assert_equals(remove_rotten(["apple", "rottenBanana", "rottenApple", "pineapple", "kiwi"]), [
                   "apple", "banana", "apple", "pineapple", "kiwi"])


fruit = ["apple", "tomato", "mango", "kiwi", "banana", "strawberry", "rottenApple",
         "rottenTomato", "rottenMango", "rottenKiwi", "rottenBanana", "rottenStrawberry"]

for i in range(0, 100):
    fruit_array = []
    length = random.randint(1, 100)
    for j in range(0, length):
    fruit_array.append(random.choice(fruit))
    answer = sol(fruit_array)
    Test.assert_equals(remove_rotten(fruit_array), answer)
