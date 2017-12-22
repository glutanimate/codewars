""" Is a number prime?

Define a function isPrime/is_prime() that takes one integer argument and returns true/True or false/False depending on if the integer is a prime.

Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.

Example

isPrime(5)
=> true
Assumptions

You can assume you will be given an integer input.
You can not assume that the integer will be only positive. You may be given negative numbers as well (or 0).

Tags: ALGORITHMS, MATHEMATICS, NUMBERS

Link: https://www.codewars.com/kata/is-a-number-prime
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

def is_prime(num):
    if -1 <= num <= 1:
        return False
    for i in range(2, num):
        if not num % i:
            return False
    return True



#############################################################
#             OTHER INTERESTING SOLUTIONS & REMARKS         #
#############################################################

def is_prime2(num):
    return num > 1 and not any(num % n == 0 for n in range(2, num))


def is_prime3(num):
    import math

    # There's only one even prime: 2
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    """
    Property:
        Every number n that is not prime has at least one prime divisor p
        such 1 < p < square_root(n)
    """
    root = int(math.sqrt(num))

    # We know there's only one even prime, so with that in mind
    # we're going to iterate only over the odd numbers plus using the above property
    # the performance will be improved
    for i in xrange(3, root + 1, 2):
        if num % i == 0:
            return False

    return True

#############################################################
#                           TESTS                           #
#############################################################


test.assert_equals(is_prime(0), False, '0 is not prime')
test.assert_equals(is_prime(1), False, '1 is not prime')
test.assert_equals(is_prime(2), True, '2 is prime')
test.assert_equals(is_prime(3), True, '3 is prime')
test.assert_equals(is_prime(4), False, '4 is not prime')
test.assert_equals(is_prime(5), True, '5 is prime')
test.assert_equals(is_prime(6), False, '6 is not prime')
test.assert_equals(is_prime(7), True, '7 is prime')
test.assert_equals(is_prime(8), False, '8 is not prime')
test.assert_equals(is_prime(9), False, '9 is not prime')
test.assert_equals(is_prime(41), True, '41 is prime')
test.assert_equals(is_prime(45), False, '45 is not prime')
test.assert_equals(is_prime(73), True, '73 is prime')
test.assert_equals(is_prime(75), False, '75 is not prime')
test.assert_equals(is_prime(5099), True, '5099 is prime')
test.assert_equals(is_prime(-1), False, '-1 is not prime')
