""" Can these three numbers form a date?

You are given three integers in the range [0-99]. You must determine if any ordering of the numbers forms a date from the 20th century.

If no ordering forms a date, return the string "invalid".
If multiple distinct orderings form dates, return the string "ambiguous".
If only one ordering forms a date, return that date as a string with format "YY/MM/DD".
Examples

unique_date(13, 12, 77) == '77/12/13' # only the ordering (77, 12, 13) forms a date
unique_date(13, 77, 12) == '77/12/13' # argument order is irrelevant

unique_date(1, 2, 3) == 'ambiguous' # 01/02/03, 02/01/03, ...
unique_date(3, 2, 1) == 'ambiguous'

unique_date(50, 40, 60) == 'invalid' # no ordering could form a date
unique_date(40, 50, 60) == 'invalid'
Note

This kata was inspired by my encounter with google.com/foobar


Tags: ALGORITHMS DATES/TIME FORMATTING PERMUTATIONS

Link: https://www.codewars.com/kata/can-these-three-numbers-form-a-date
"""

#############################################################
#                       TEST FRAMEWORK                      #
#############################################################

import sys, os
sys.path.append(os.path.abspath(
                os.path.join(os.path.dirname(__file__), '..', "tests")))
from Test import *


#############################################################
#                         SOLUTIONS                         #
#############################################################

from itertools import permutations
from datetime import datetime


def checkDate(date):
    try:
        date = list(date)
        date[0] = 1900 + date[0]
        datetime(*date)
        return True
    except ValueError:
        return False


def uniqueDate(*numbers):
    valid = []
    for date in permutations(numbers):
        if checkDate(date):
            valid.append(date)
    if not valid:
        return "invalid"
    elif len(set(valid)) > 1:
        return "ambiguous"
    else:
        return "/".join(str('{0:02d}'.format(v)) for v in valid[0])


#############################################################
#                           TESTS                           #
#############################################################

# for backward compatibility
try:
    unique_date = uniqueDate
except NameError:
    pass


import random
from calendar import isleap


def uni_ambig():
  from collections import Counter

  t = []
  daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

  for year in range(0, 100):
    for month in range(1, 13):
      daysInMonth[1] = 29 if isleap(1900 + year) else 28
      for day in range(1, daysInMonth[month - 1] + 1):
        t.append(tuple(sorted([year, month, day])))

  unique = []
  ambiguous = []

  for item, count in Counter(t).items():
    if count == 1:
      unique.append(item)
    else:
      ambiguous.append(item)

  return [unique, ambiguous]


unique, ambiguous = uni_ambig()

simple_tests = [[(11, 24, 41), '41/11/24'],
                [(5, 23, 67), '67/05/23'],
                [(4, 26, 62), '62/04/26'],
                [(10, 23, 33), '33/10/23'],
                [(5, 6, 35), 'ambiguous'],
                [(3, 30, 5), 'ambiguous'],
                [(14, 20, 89), 'invalid'],
                [(1, 2, 3), 'ambiguous'],
                [(13, 12, 77), '77/12/13'],
                [(40, 50, 60), 'invalid']]

test.describe("Simple Tests")

for inp, outp in simple_tests:
  test.assert_equals(unique_date(*inp), outp)

test.describe("General Tests")

test.it("should correctly identify ambiguous dates")

for _ in range(100):
  a = random.choice(ambiguous)
  test.assert_equals(unique_date(*a), 'ambiguous')

test.it('should correctly identify unique dates')

for _ in range(100):
  u = random.choice(unique)
  y, m, d = (u[0], u[1], u[2]) if u[0] == 0 else (u[2], u[0], u[1])
  test.assert_equals(unique_date(*u), '{:02d}/{:02d}/{:02d}'.format(y, m, d))

test.it('should correctly identify invalid dates')

inv = list(range(32, 100))
for _ in range(100):
  d = [random.choice(inv) for _ in range(3)]
  test.assert_equals(unique_date(*d), 'invalid')


#############################################################
#                      COMMENTS, ETC.                       #
#############################################################



