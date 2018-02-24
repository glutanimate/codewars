# -*- coding: utf-8 -*-
""" Inertial Array

An array is defined to be inertialif the following conditions hold:

a. it contains at least one odd value  
b. the maximum value in the array is even 
c. every odd value is greater than every even value that is not the maximum value.
eg:-

So [11, 4, 20, 9, 2, 8] is inertial because 
a. it contains at least one odd value [11,9] 
b. the maximum value in the array is 20 which is even 
c. the two odd values (11 and 9) are greater than all the even values that are not equal to 20 (the maximum), i.e., [4, 2, 8]
Write a function called isInertial that accepts an integer array and returns true if the array is inertial; otherwise it returns false.

Tags: FUNDAMENTALS, ARRAYS

Link: FUNDAMENTALSARRAYS
"""

#############################################################
#                        MY SOLUTIONS                       #
#############################################################

def is_inertial(arr):
    """Maximize performance by only iterating once over array"""
    maxnr_odd = minnr_odd = maxnr_even = maxnr2nd_even = None

    for nr in arr:
        if nr % 2 == 0:
            if maxnr_even is None:
                maxnr_even = nr
            elif nr > maxnr_even:
                maxnr2nd_even, maxnr_even = maxnr_even, nr
            elif maxnr2nd_even is None or maxnr2nd_even < nr:
                maxnr2nd_even = nr
        else:
            if minnr_odd is None or minnr_odd > nr:
                minnr_odd = nr
            if maxnr_odd is None or maxnr_odd < nr:
                maxnr_odd = nr

    return (maxnr_even is not None and maxnr_odd is not None and minnr_odd is not None
            and maxnr_odd < maxnr_even and (maxnr2nd_even is None or minnr_odd > maxnr2nd_even))



#############################################################
#             OTHER INTERESTING SOLUTIONS & REMARKS         #
#############################################################

# top-voted solution. Very succinct, but 6 times slower than the solution above
def is_inertial2(arr):
    mx = max(arr, default=1)
    miO = min((x for x in arr if x % 2 == 1), default=float("-inf"))
    miE2 = max((x for x in arr if x %
                2 == 0 and x != mx), default=float("-inf"))
    return mx % 2 == 0 and miE2 < miO



#############################################################
#                           TESTS                           #
#############################################################


import sys
import os
sys.path.append(os.path.abspath(
                os.path.join(os.path.dirname(__file__), '..', "tests")))
from Test import *

performance_test(is_inertial, [[581, -384, 140, -287]], 100000)
performance_test(is_inertial2, [[581, -384, 140, -287]], 100000)

import random
test.it("Basic tests")
test.assert_equals(is_inertial([]), False)
test.assert_equals(is_inertial([581, -384, 140, -287]), False)
test.assert_equals(is_inertial([11, 4, 20, 9, 2, 8]), True)


def sol51(arr):
    if arr == []:
        return False
    maxi, evens, odds = max(arr), list(filter(lambda x: x % 2 == 0, arr)), list(
        filter(lambda x: x % 2 == 1, arr))
    if evens == [] or maxi % 2 != 0 or odds == []:
        return False
    evens.sort()
    evens.pop()
    for i in range(len(odds)):
        for j in range(len(evens)):
            if odds[i] < evens[j]:
                return False
    return True


test.it("Random tests")
for i in range(0, 100):
    arr, arrLen = [], random.randrange(0, 100)
    for j in range(0, arrLen):
        arr.append(random.randrange(1, 600) *
                   (-1 if random.randrange(0, 2) == 0 else 1))
    expected = sol51(arr)
    print(expected)
    test.assert_equals(is_inertial(arr), expected)
