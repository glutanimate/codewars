#!/usr/bin/python3

"""
Simple fraction to mixed number converter

Task

Given a string representing a simple fraction x/y, your function must return a string representing the corresponding mixed fraction in the following format:

[sign]a b/c

where a is integer part and b/c is irreducible proper fraction. There must be exactly one space between a and b/c. Provide [sign] only if negative (and non zero) and only at the beginning of the number (both integer part and fractional part must be provided absolute).

If the x/y equals the integer part, return integer part only. If integer part is zero, return the irreducible proper fraction only. In both of these cases, the resulting string must not contain any spaces.

Division by zero should raise an error (preferably, the standard zero division error of your language).

Value ranges

-10 000 000 < x < 10 000 000
-10 000 000 < y < 10 000 000
Examples

Input: 42/9, expected result: 4 2/3.
Input: 6/3, expedted result: 2.
Input: 4/6, expected result: 2/3.
Input: 0/18891, expected result: 0.
Input: -10/7, expected result: -1 3/7.
Inputs 0/0 or 3/0 must raise a zero division error.
Note

Make sure not to modify the input of your function in-place, it is a bad practice.

https://www.codewars.com/kata/simple-fraction-to-mixed-number-converter/train/python
"""

# gcd is also available in pythons's stdlib
# for python < 3.5: from fractions import gcd
# for python >= 3.5: from math import gcd

def gcd(num1, num2):
    """Calculate greatest common denominator
    
    Uses Euclidean algorithm to calculate greatest common denominator of two
    integers (https://en.wikipedia.org/wiki/Euclidean_algorithm).
    
    Basic algorithm for two integers a, b, and the gcd g (iterative solution):

    <start>
    divide b by a, take the remainder r
    if r != 0:
        assign b = a
        assign a = r
        goto <start>
    else:
        g = a
    
    Arguments:
        
        `num1` {int} -- first integer
        
        `num2` {int} -- second integer
    
    Returns:
        int -- greatest common denominator
    """
    
    while num1 != 0:
        # no need to use a temporary variable for remainder because of
        # python tuple assignment / unpacking (all the expressions
        # on the right side of the equals sign are evaluated before
        # any assignments)
        num2, num1 = num1, num2 % num1
        
    return num2


def mixed_fraction(s):

    numerator, denominator = (int(i) for i in s.split("/"))
    if denominator == 0:
        raise ZeroDivisionError

    sign_s = "-" if numerator and ((numerator < 0) ^ (denominator < 0)) else ""
    
    numerator, denominator = abs(numerator), abs(denominator)
    integ = numerator // denominator
    if integ:
        int_s = str(integ)
        numerator %= denominator
    else:
        int_s = ""

    _gcd = gcd(numerator, denominator)
    numerator /= _gcd
    denominator /= _gcd

    if numerator:
        fract_s = str(numerator) + "/" + str(denominator)
        if int_s:
            fract_s = " " + fract_s
    else:
        fract_s = ""

    return "{0}{1}{2}".format(sign_s, int_s, fract_s) or "0"



print(mixed_fraction('0/7'))
