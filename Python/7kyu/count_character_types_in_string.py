# -*- coding: utf-8 -*-
""" Simple string characters

In this Kata, you will be given a string and your task will be to return a list of ints detailing the count of uppercase letters, lowercase, numbers and special characters, as follows.

solve("*'&ABCDabcde12345") = [4,5,5,3]. 
--the order is: uppercase letters, lowercase, numbers and special characters.
More examples in the test cases.

Good luck!


Tags: FUNDAMENTALS

Link: https://www.codewars.com/kata/simple-string-characters/train/python
"""

#############################################################
#                        MY SOLUTIONS                       #
#############################################################

# Using RegEx

# TODO: find way to combine into one re call
def solve(s):
    caps = len(re.findall(r"[A-Z]", s))
    low = len(re.findall(r"[a-z]", s))
    num = len(re.findall(r"[0-9]", s))
    return [caps, low, num, len(s) - caps - low - num]


# Using loop
from string import ascii_lowercase, ascii_uppercase, digits

def solve(s):
    upper = lower = dig = special = 0
    
    for char in s:
        if char in ascii_uppercase:
            upper += 1
        elif char in ascii_lowercase:
            lower += 1
        elif char in digits:
            dig += 1
        else:
            special += 1
    
    return [upper, lower, dig, special]



#############################################################
#             OTHER INTERESTING SOLUTIONS & REMARKS         #
#############################################################

# Clever succinct solution using string methods and list indexes:
# seems to be a bit slower, however
def solve2(s):
    res = [0, 0, 0, 0]
    for c in s:
        i = 0 if c.isupper() else 1 if c.islower() else 2 if c.isdigit() else 3
        res[i] += 1
    return res


#############################################################
#                           TESTS                           #
#############################################################


import sys
import os
sys.path.append(os.path.abspath(
                os.path.join(os.path.dirname(__file__), '..', "tests")))
from Test import *


performance_test(solve, ["P*K4%>mQUDaG$h=cx2?.Czt7!Zn16p@5H"], 1000000)
performance_test(solve2, ["P*K4%>mQUDaG$h=cx2?.Czt7!Zn16p@5H"], 1000000)


assert False

test.it("Basic tests")
test.assert_equals(solve("Codewars@codewars123.com"), [1, 18, 3, 2])
test.assert_equals(solve("bgA5<1d-tOwUZTS8yQ"), [7, 6, 3, 2])
test.assert_equals(solve("P*K4%>mQUDaG$h=cx2?.Czt7!Zn16p@5H"), [9, 9, 6, 9])
test.assert_equals(
    solve("RYT'>s&gO-.CM9AKeH?,5317tWGpS<*x2ukXZD"), [15, 8, 6, 9])
test.assert_equals(solve("$Cnl)Sr<7bBW-&qLHI!mY41ODe"), [10, 7, 3, 6])
test.assert_equals(solve("@mw>0=QD-iAx!rp9TaG?o&M%l$34L.nbft"), [7, 13, 4, 10])


import random

def solver9_8(s):
    n, up, low, sp = 0, 0, 0, 0
    for i in range(0, len(s)):
        temp = ord(s[i])
        if temp >= 48 and temp <= 57:
            n += 1
        elif temp >= 97 and temp <= 122:
            low += 1
        elif temp >= 65 and temp <= 90:
            up += 1
        else:
            sp += 1
    return [up, low, n, sp]


def randSt():
    res = []
    for i in range(33, 47):
        res.append(chr(i))
    for i in range(60, 65):
        res.append(chr(i))
    for i in range(97, 123):
        res.append(chr(i))
    for i in range(48, 58):
        res.append(chr(i))
    random.shuffle(res)
    r = random.randrange(15, len(res))
    return ''.join(res[0:r])

test.it("Random tests")
for i in range(0, 100):
    arr = randSt()
    expected = solver9_8(arr)
    test.assert_equals(solve(arr), expected)
