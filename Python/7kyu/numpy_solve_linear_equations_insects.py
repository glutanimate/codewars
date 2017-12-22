"""
Jungerstein's Math Training Room: 2. How many bugs?

There are several (or no) spiders, butterflies, and dragonflies.

In this kata, a spider has eight legs. A dragonfly or a butterfly has six legs. A dragonfly has two pairs of wings, while a butterfly has one pair of wings. I am not sure whether they are biologically correct, but the values apply here.

Given the number of total heads, legs, and pairs of wings, please calculate numbers of each kind of bugs. Of course they are integers. However, I do not guarantee that they are positive in the test cases. Please regard the minus numbers as cases that does not make sense.

If answers make sense, return [n_spider, n_butterfly, n_dragonfly]; else, please return [-1, -1, -1].

Example:

cal_n_bug(3, 20, 3) = [1, 1, 1] One spider, one butterfly, one dragonfly in total have three heads, twenty legs (8 for the spider, 6 for the butterfly, and 6 for the dragonfly), and three pairs of wings (1 for the butterfly and 2 for the dragonfly).

https://www.codewars.com/kata/jungersteins-math-training-room-2-how-many-bugs/train/python

cf.: https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.linalg.solve.html
"""

import numpy as np

# heads: x + y + z = n(heads)
# legs: 8x + 6y + 6z = n(legs)
# wings: y + 2z = n(wings)
# where x, y, z: spiders, butterflies, dragonflies
coefficients = np.array([[1, 1, 1], [8, 6, 6], [0, 1, 2]])


def cal_n_bug(n_head, n_leg, n_wing):
    dependents = np.array([n_head, n_leg, n_wing])
    res = np.linalg.solve(coefficients, dependents)
    if all(i >= 0 and i.is_integer() for i in res):
        return [int(i) for i in res]
    return [-1, -1, -1]


print(cal_n_bug(40, 320, 0))
