# -*- coding: utf-8 -*-
""" Adding Fractions

In most languages, division immediately produces decimal values, and therefore, adding two fractions gives a decimal result:

(1/2) + (1/4) #=> 0.75
But what if we want to be able to add fractions and get a fractional result?

(1/2) + (1/4) #=> 3/4
Task:

Your job here is to implement a function, add_fracs that takes any number of fractions (positive OR negative) as strings, and yields the exact fractional value of their sum in simplest form. If the sum is greater than one (or less than negative one), it should return an improper fraction. If there are no arguments passed, (add_fracs()), return an empty string. Inputs will always be valid fractions, and the output should also be a string. If the result is an integer, like '2/1', just return '2'. Input numerators (but NOT denominators) can be zero.

How the function will be called:

add_fracs(any_number_of_fractions1, any_number_of_fractions2, any_number_of_fractions3, ...) #=> a fraction as a string
Some examples (see example test cases for more):

add_fracs() #=> ''
add_fracs('1/2') #=> '1/2'
add_fracs('1/2', '1/4') #=> '3/4'
add_fracs('1/2', '3/4') #=> '5/4'
add_fracs('2/4', '6/4', '4/4') #=> '3'
add_fracs('2/3', '1/3', '4/6') #=> '5/3'
add_fracs('-2/3', '5/3', '-4/6') #=> '1/3'
If there are any issues with the description, test cases or anything else, please do let me know by commenting or marking an issue. Otherwise, make sure to rank and mark as ready. Enjoy!

Also check out my other creations — Split Without Loss, Random Integers, Implement String#transpose, Implement Array#transpose!, Arrays and Procs #1, and Arrays and Procs #2


Tags: FUNDAMENTALS

Link: https://www.codewars.com/kata/adding-fractions
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


from fractions import Fraction


def add_fracs(*fracs):
    if not fracs:
        return ""
    res = 0
    for i in fracs:
        res += Fraction(i)
    return str(res)


#############################################################
#             OTHER INTERESTING SOLUTIONS & REMARKS         #
#############################################################


import numpy as np


def gcd(a, b):
    '''Return greatest common divisor using Euclid's Algorithm.'''
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    '''Return lowest common multiple.'''
    return a * b // gcd(a, b)


def lcmm(*args):
    '''Return lcm of args.'''
    return reduce(lcm, args)


def add_fracs2(*fracs):
    '''Return sum of fractions as a fraction.'''
    fracs_lst = list(fracs)

    if not fracs_lst:
        return ''

    LCM = reduce(lcmm, [int(elem.split('/')[1]) for elem in fracs_lst])

    nums = np.array([int(elem.split('/')[0]) for elem in fracs_lst])
    denoms = np.array([int(elem.split('/')[1]) for elem in fracs_lst])

    numerator = sum(LCM * nums / denoms)
    denominator = LCM / gcd(numerator, LCM)

    if denominator == 1:
        return str(numerator / gcd(numerator, LCM))
    else:
        return '/'.join([str(i) for i in np.array([numerator, LCM]) / gcd(numerator, LCM)])


#############################################################
#                           TESTS                           #
#############################################################

import random
from fractions import Fraction


def test_add_fracs(*fracs):
    if fracs:
        s = str(sum(Fraction(frac) for frac in fracs))
        return s
    return ''


test.describe("Fixed cases")

test.it("Example (basic) cases")
tests = [
    [[], ''],
    [['1/2'], '1/2'],
    [['1/2', '1/4'], '3/4'],
    [['1/2', '3/4'], '5/4'],
    [['2/4', '6/4', '4/4'], '3'],
    [['2/3', '1/3', '4/6'], '5/3'],
    [['2/3', '1/4', '5/6'], '7/4'],
    [['-2/3', '5/3', '-4/6'], '1/3'],
    [['-7/3', '-1/3', '-2/3'], '-10/3'],
    [['1/4', '5/4', '-1/2', '-1/1'], '0']
]
for i, e in tests:
    test.assert_equals(add_fracs(*i), e)

test.it("More complex cases")
tests = [
    [['1/2', '1/5', '1/7'], "59/70"],
    [['1/2', '3/4', '5/6'], "25/12"],
    [['2/4', '6/3', '4/2'], "9/2"],
    [['2/3', '1/8', '4/1'], "115/24"],
    [['2/8', '1/9', '5/10'], "31/36"],
    [['-1/2', '-1/5', '-1/7'], "-59/70"],
    [['-1/2', '3/4', '-5/6'], "-7/12"],
    [['2/4', '-6/3', '-4/2'], "-7/2"],
    [['-2/3', '1/8', '-4/1'], "-109/24"],
    [['-2/8', '1/9', '-5/10'], "-23/36"],
]
for i, e in tests:
    test.assert_equals(add_fracs(*i), e)


def generate_test():
    fs = random.choice(range(2, 10))
    nl = [("%s/%s" % (random.choice(range(-10, 11)), random.choice(range(1, 11))))
          for i in range(fs)]
    return [nl, test_add_fracs(*nl)]


test.describe("Random cases")
for i in range(80):
    i, e = generate_test()
    test.it("Input = %s" % i)
    test.assert_equals(add_fracs(*i), e)
