"""
Calculate Derivative #1 - Single Integer Equation

I need some help with my math homework. I have a number of problems I need to
return the derivative for.

They will all be of the form: ax^b, A and B are both integers, but can be
positive or negative. Note:

if b is 1, then the equation will be ax.
if b is 0, then the equation will be 0.
Examples: 3x^3 -> 9x^2 3x^2 -> 6x 3x -> 3 3 -> 0 3x^-1 -> -3x^-2 -3x^-2 -> 6x^-3

If you don't remember how derivatives work, here's a link with some basic rules:
 https://www.mathsisfun.com/calculus/derivatives-rules.html

-------

Note: the solutions below also work for terms without "a"

https://www.codewars.com/kata/calculate-derivative-number-1-single-integer-equation/train/python

"""

import re

term_pattern = r"((-)?[0-9]+)?(x?)(\^)?((-)?[0-9]+)?"
term_re = re.compile(term_pattern)


def get_derivative(string):
    """
    Convert string representation of ax^b term into its derivative

    #1 RegEx solution
    """

    result = term_re.match(string)
    factor_str, _, hasBase, hasExp, exponent_str, _ = result.groups()

    if not hasBase:
        return "0"

    factor = int(factor_str) if factor_str else 1
    exponent = int(exponent_str) if exponent_str else 1

    new_factor = factor * exponent
    new_exponent = exponent - 1

    if not hasExp:
        return str(new_factor)

    if new_factor == 1:
        nf_str = ""
    elif new_factor == -1:
        nf_str = "-"
    else:
        nf_str = str(new_factor)

    if new_exponent == 0:
        ne_str = ""
    elif new_exponent == 1:
        ne_str = "x"
    else:
        ne_str = "x^{}".format(new_exponent)

    return nf_str + ne_str


def get_derivative2(string):
    """
    Convert string representation of ax^b term into its derivative

    #2 Non-RegEx solution
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
    new_exp = exp - 1
    new_factor = int(factor_str or "1") * exp

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


print(get_derivative("2x"))
print(get_derivative("-2x^2"))
print(get_derivative("2x^3"))
print(get_derivative("3"))
print(get_derivative("5x^-1"))
print(get_derivative("-x^-1"))

# ↓ adapted from third-party solution
# seems to have some issues with corner cases (e.g. negative exponents)

term_pattern = (r'(?P<sign>\-?)'
                r'(?P<coeff>\d*)'
                r'x'
                r'(?:\^(?P<exp>\-?\d+))?')

term_re = re.compile(term_pattern)


def as_int(s):
    return int(s) if s else 1


def get_derivative3(eq):
    monomer = term_re.match(eq)
    if not monomer:
        return "0"
    sign, coeff, exp = monomer.groups()
    coeff, exp = map(as_int, (coeff, exp))
    coeff *= exp
    exp -= 1
    result = ('{sign}{coeff}' if exp == 0 else '{sign}{coeff}x'
              if exp == 1 else '{sign}{coeff}x^{exp}').format(
                  sign=sign, coeff=coeff, exp=exp)

    return result or '0'


print(get_derivative3("2x"))
print(get_derivative3("-2x^2"))
print(get_derivative3("2x^3"))
print(get_derivative3("3"))
print(get_derivative3("5x^-1"))
print(get_derivative3("-x^-1"))
