""" Title Case

A string is considered to be in title case if each word in the string is either (a) capitalised (that is, only the first letter of the word is in upper case) or (b) considered to be an exception and put entirely into lower case unless it is the first word, which is always capitalised.

Write a function that will convert a string into title case, given an optional list of exceptions (minor words). The list of minor words will be given as a string with each word separated by a space. Your function should ignore the case of the minor words string -- it should behave in the same way even if the case of the minor word string is changed.

###Arguments (Haskell)

First argument: space-delimited list of minor words that must always be lowercase except for the first word in the string.
Second argument: the original string to be converted.
###Arguments (Other languages)

First argument (required): the original string to be converted.
Second argument (optional): space-delimited list of minor words that must always be lowercase except for the first word in the string. The JavaScript/CoffeeScript tests will pass undefined when this argument is unused.
###Example

title_case('a clash of KINGS', 'a an the of') # should return: 'A Clash of Kings'
title_case('THE WIND IN THE WILLOWS', 'The In') # should return: 'The Wind in the Willows'
title_case('the quick brown fox') # should return: 'The Quick Brown Fox'

Tags: FUNDAMENTALS, STRINGS, PARSING, ALGORITHMS

Link: https://www.codewars.com/kata/title-case
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


def title_case(t, m=None):
    res = []
    t = [i.lower() for i in t.split()]
    if m:
       m = [i.lower() for i in m.split()]
    else:
       m = []
    return " ".join([w.capitalize() if w not in m or idx == 0 else w for idx, w in enumerate(t)])


#############################################################
#             OTHER INTERESTING SOLUTIONS & REMARKS         #
#############################################################

def title_case2(title, minor_words=''):
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    return ' '.join([word if word in minor_words else word.capitalize() for word in title])



#############################################################
#                           TESTS                           #
#############################################################


def my_test(title, minor_words, expect):
  answer = title_case(title) if minor_words is None else title_case(
      title, minor_words)
  message = "Gave title={0}{1}. Expected {2} but got {3}.".format(
      repr(title),
      '' if minor_words is None else ', minor_words=' + repr(minor_words),
      repr(expect),
      repr(answer))
  test.expect(answer == expect, message)


my_test('', '', '')
my_test('aBC deF Ghi', None, 'Abc Def Ghi')
my_test('ab', 'ab', 'Ab')
my_test('a bc', 'bc', 'A bc')
my_test('a bc', 'BC', 'A bc')
my_test('First a of in', 'an often into', 'First A Of In')
my_test('a clash of KINGS', 'a an the OF', 'A Clash of Kings')
my_test('the QUICK bRoWn fOX', 'xyz fox quick the', 'The quick Brown fox')
