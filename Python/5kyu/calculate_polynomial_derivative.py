#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Derivative!

Calculate a polynomial derivative, here is how:

-Polynomial is an expression like 3x^4+2x^2+x+10 
-Derivative:
    +The first step is to take any exponent and bring it down, multiplying it times the coefficient. 
    +Reducing the exponent by 1 : the expression above will be 12x^3+4x+1

-Rules:
    +The derivative of number(constant) is 0
    +The derivative of the sum of two function is the sum of the derivatives.
-Example : 3x^2 is 6x or 6 is 0 or 10x^9 is 90x^8
-Another example : 3x^2-4x+1 is 6x-4

You should write a function that calculates the derivative:

def derivative(eq):
  pass
To be considered:
-The expressions may contain "+" or "-" like : 2x^2-3x or -x^2+3x 
-The first expression have no sign if it's a "+", but "-" is used for it like : (no + here)3x^4+4x and -3x^4+4x are ok
-Exponents are always integers and they are >=0 
-Exponents are written only if they're >1 so there is no test case like 10x^1, it's 10x

https://www.codewars.com/kata/derivative
"""

import re

minus_pattern = r"(?<!\^)(?<!^)-"  # "-" that associate polynomial subterms
minus_re = re.compile(minus_pattern)


def get_derivative(string):
    """
    Convert string representation of ax^b term into its derivative
    """

    try:
        factor_str, exp_str = string.split("x^")
    except ValueError:
        if string[-1] != "x":
            return ""
        else:
            if string == "x":
                return "1"
            return string[:-1]

    exp = int(exp_str)

    if not factor_str:
        factor = 1
    elif factor_str == "-":
        factor = -1
    else:
        factor = int(factor_str)

    new_exp = exp - 1
    new_factor = factor * exp

    if new_factor == 1:
        nf_str = ""
    elif new_factor == -1:
        nf_str = "-"
    else:
        nf_str = str(new_factor)

    if new_exp == 1:
        ne_str = "x"
    else:
        ne_str = "x^" + str(new_exp)

    return nf_str + ne_str


def derivative(eq):
    """
    Convert string representation of polynomial term into its derivative
    """
    canonical_eq = minus_re.sub("+-", eq)
    terms = canonical_eq.split("+")
    partials = []
    for term in terms:
        derived = get_derivative(term)
        if derived:
            partials.append(derived)

    res = "+".join(partials) or "0"

    return res.replace("+-", "-")


print(derivative("x^2+2x+1+x"))
print(derivative("-x^2+3x+4"))
print(derivative("-1000x^7+200x^4+6x^2+x+1000"))


############################

"""

Top-voted solution:

Notes:

- actually seems to have a lot of limitations, now that I dive into it more deeply
    - not working for negative exponents
    - only seems to work fine for given test cases

"""

# ?P<sign>, etc. demark named capture groups
# note how "x" is not optional → author decided to just
# skip all purely numerical terms that fall away during derivation
# anyway
my_regexp = (r'(?P<sign>[+\-]?)'
             r'(?P<coeff>\d*)'
             r'x'
             r'(?:\^(?P<exp>\d+))?')


def as_int(s): return int(s) if s else 1

def derivative(eq):
    result = ''
    # ↓ re.finditer provides an iterable that yields the next
    # non-overlapping MatchObject in each iteration
    for monom in re.finditer(my_regexp, eq):
        # Q: Why use named capture groups if not using them here?
        # perhaps to increase readability?
        sign, coeff, exp = monom.groups()
        # ↓ used map to save a few characters ⚡performance
        coeff, exp = map(as_int, (coeff, exp))
        # alt.: coeff,exp = as_int(coeff), as_int(exp)
        # ↓ elegant solution for calculating values of derived term
        coeff *= exp
        exp -= 1
        # ↓ I had no idea you could expand ternary terms like that!
        # very cool solution to address multiple different output format
        # depending on a control variable
        result += ('{sign}{coeff}' if exp == 0 else
                   '{sign}{coeff}x' if exp == 1 else
                   '{sign}{coeff}x^{exp}'
                   ).format(sign=sign, coeff=coeff, exp=exp)
        # ↑ ⚡performance: it would be slightly faster to construct an array 
        # with the results instead of constantly concatenating to a result string
    
    # ↓ alt.: return result or "0"
    return result if result else '0'
