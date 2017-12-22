"""My Very Own Python's Split Function

Quite recently it happened to me to join some recruitment interview, where my first task was to write own implementation of built-in split function. It's quite simple, is it not?

However, there were the following conditions:

- the function cannot use, in any way, the original split or rsplit functions,
- the new function must be a generator,
- it should behave as the built-in split, so it will be tested that way -- think of split() and split('')
This Kata will control if the new function is a generator and if it's not using the built-in split method, so you may try to hack it, but let me know if with success, or if something would go wrong!

Enjoy!


https://www.codewars.com/kata/my-very-own-pythons-split-function/train/python

"""

# import test framework
import sys, os
sys.path.append(os.path.abspath(
                os.path.join(os.path.dirname(__file__), '..', "tests")))
from Test import *


# SOLUTIONS


import string

def my_very_own_split(mystring, delimiter=None):
    
    yield mystring



# TESTS

s, d = 'abc,def,ghi', ','
test.assert_equals(list(my_very_own_split(s, d)), ['abc', 'def', 'ghi'])

s, d = 'This is a test', ' '
test.assert_equals(list(my_very_own_split(s, d)), ['This', 'is', 'a', 'test'])

s, d = 'This is a test', ','
test.assert_equals(list(my_very_own_split(s, d)), ['This is a test'])
