# Unpacking a vector of the form [[x1,y1], [x2,y2]]:
(x1,y1),(x2,y2) = vector

# cycling between different objects in loop invocations with itertools.cycle

from itertools import cycle

def capitalize(s):
    func = cycle((str.upper, str.lower))
    result = ''.join(next(func)(a) for a in s)
    return [result, result.swapcase()]

# Important lesson: max() can take an iterator as an argument,
# meaning that you don't actually have to calculate an entire list
# beforehand before invoking max on it. ⇒ generator comprehensions are
# valid options when calculating the max/min is needed, e.g.:


def solution(dd):
    return max(int(dd[i:i + 5]) for i in range(len(dd) - 4))

# instead of:


def solution(digits):
    largest = 0
    for idx, digit in enumerate(digits[:-4]):
        number = int(digits[idx:idx + 5])
        if number > largest:
            largest = number
    return largest


# Sorting lists case-insensitively can be done by passing the str.lower
# method as a key to sorted() or .sort(), e.g.:

def sorter(textbooks):
    return sorted(textbooks, key=str.lower)

# N.B.: This works out of the box on python3. On python2 you either have to use
# unicode.lower or make sure the strings you're dealing with aren't unicode


# True and False actually evaluate to 1 and 0, respectively, when used in
# calculations, e.g.

True * True = 1
True * False = 0

# Ceiling division in Python can be achieved using "upside-down" floor division:


def ceildiv(a, b):
    return -(-a // b)

# NB: This works in Python because it's doing an actual floor division, so
# for negative numbers the floor points towards -∞. In other languages like C
# this does not work because integer division simply truncates the fractional
# part

# For replacing multiple characters simultaneously in a string, you should use
# the maketrans method. In Python3:

def nerdify(txt):
    trans = str.maketrans("AaEel", "44331")
    return txt.translate(trans)

# In Python2:

import string

def nerdify(txt):
    trans = string.maketrans("AaEel", "44331")
    return txt.translate(trans)

