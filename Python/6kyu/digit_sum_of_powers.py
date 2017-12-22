# -*- coding: utf-8 -*-
""" Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....¡Eureka!!

The number 89 is the first integer with more than one digit that fulfills the property partially introduced in the title of this kata. What's the use of saying "Eureka"? Because this sum gives the same number.

In effect: 89 = 8^1 + 9^2

The next number in having this property is 135.

See this property again: 135 = 1^1 + 3^2 + 5^3

We need a function to collect these numbers, that may receive two integers a, b that defines the range [a, b] (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.

Let's see some cases:

sum_dig_pow(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

sum_dig_pow(1, 100) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
If there are no numbers of this kind in the range [a, b] the function should output an empty list.

sum_dig_pow(90, 100) == []
Enjoy it!!

Tags: FUNDAMENTALS, CONTROL FLOW, BASIC LANGUAGE FEATURES, MATHEMATICS, ALGORITHMS, NUMBERS, FUNCTIONS, SORTING, DECLARATIVE PROGRAMMING

Link: https://www.codewars.com/kata/take-a-number-and-sum-its-digits-raised-to-the-consecutive-powers-and-dot-dot-dot-eureka
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

def sum_dig_pow(a, b):
    res = []
    for num in range(a, b + 1):
        summed = sum(int(d) ** (idx + 1) for idx, d in enumerate(str(num)))
        if summed == num:
            res.append(num)
    return res



#############################################################
#             OTHER INTERESTING SOLUTIONS & REMARKS         #
#############################################################


def dig_pow(n):
    return sum(int(x)**y for y, x in enumerate(str(n), 1))


def sum_dig_pow(a, b):
    return [x for x in range(a, b + 1) if x == dig_pow(x)]


#############################################################
#                           TESTS                           #
#############################################################

test.describe("Basic Tests")
test.assert_equals(sum_dig_pow(1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9])
test.assert_equals(sum_dig_pow(1, 100), [1, 2, 3, 4, 5, 6, 7, 8, 9, 89])
test.assert_equals(sum_dig_pow(10, 89),  [89])
test.assert_equals(sum_dig_pow(10, 100),  [89])
test.assert_equals(sum_dig_pow(90, 100), [])
test.assert_equals(sum_dig_pow(90, 150), [135])
test.assert_equals(sum_dig_pow(50, 150), [89, 135])
test.assert_equals(sum_dig_pow(10, 150), [89, 135])
test.assert_equals(sum_dig_pow(89, 135), [89, 135])

test.describe("Random Tests")
from random import randint


def pow_dig(lst):
    exp = 1
    sumL = []
    for dig in lst:
        sumL.append(dig ** exp)
        exp += 1
    return sumL


def list_dig(n):
    nStrL = list(str(n))
    digL = map(int, list(str(n)))
    return digL


def assoc_pow_digit(n):
    nStr = str(n)
    sumL = pow_dig(list_dig(nStr))
    if n == sum(sumL):
        return True


def sum_dig_pow_mine_rand(a, b):
    solL = []
    for n in range(a, b + 1):
        if assoc_pow_digit(n):
            solL.append(n)
    return solL


for h in range(40):
    a = randint(100, 500)
    b = randint(510, 1500)
    test.it("a = " + str(a))
    test.it("b = " + str(b))
    result = sum_dig_pow_mine_rand(a, b)
    test.assert_equals(sum_dig_pow(a, b), result)
    print "result -----> " + str(result)
    print

for h in range(20):
    a = randint(10, 1999)
    b = randint(2000, 3000)
    test.it("a = " + str(a))
    test.it("b = " + str(b))
    result = sum_dig_pow_mine_rand(a, b)
    test.assert_equals(sum_dig_pow(a, b), result)
    print "result -----> " + str(result)
    print

for h in range(5):
    a = randint(2620000, 2640000)
    b = randint(2647000, 2648000)
    test.it("a = " + str(a))
    test.it("b = " + str(b))
    result = sum_dig_pow_mine_rand(a, b)
    test.assert_equals(sum_dig_pow(a, b), result)
    print "result -----> " + str(result)
    print

for h in range(3):
    a = randint(12157692622039623000,  12157692622039625500)
    b = randint(12157692622039625600, 12157692622039625700)
    test.it("a = " + str(a))
    test.it("b = " + str(b))
    result = sum_dig_pow_mine_rand(a, b)
    test.assert_equals(sum_dig_pow(a, b), result)
    print "result -----> " + str(result)
    print
