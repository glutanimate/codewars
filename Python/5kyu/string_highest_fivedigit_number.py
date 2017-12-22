""" Largest 5 digit number in a series

In the following 6 digit number:

283910
91 is the greatest sequence of 2 digits.

In the following 10 digit number:

1234567890
67890 is the greatest sequence of 5 digits.

Complete the solution so that it returns the largest five digit number found within the number given. The number will be passed in as a string of only digits. It should return a five digit integer. The number passed may be as large as 1000 digits.

Adapted from ProjectEuler.net

https://www.codewars.com/kata/largest-5-digit-number-in-a-series/python
"""

# import test framework
import sys, os

sys.path.append(os.path.abspath(
                os.path.join(os.path.dirname(__file__), '..', "tests")))
from Test import *


# standard solution:

def solution1(digits):
    upper_bound = len(digits) - 5
    highest = 0

    for idx in range(upper_bound + 1):
        number = int(digits[idx:idx + 5])
        if number > highest:
            highest = number

    return highest

# shorthand solution using generator expression:

def solution2(digits):
    return max(int(digits[idx:idx + 5]) for idx in range(len(digits) - 5 + 1))

# TESTS

solution = solution1

number = "7316717653133062491922511967442657474235534919493496983520368542506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753123457977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257540920752963450"
actual = solution(number)

test.expect(actual != 0, 'solution returned zero')
test.expect(actual, 'solution did not return a value')
test.assert_equals(actual, 99890, 'solution did not return correct value')
test.assert_equals(solution('1234567898765'), 98765,
                   'Failed when max 5 digits is at end of number')


performance_test(solution1, [number])
performance_test(solution2, [number])
