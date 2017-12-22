"""
Numbers in strings

In this Kata, you will be given a string that has lowercase letters and numbers. Your task is to compare the number groupings and return the largest number.

For example, solve("gh12cdy695m1") = 695, because this is the largest of all number groupings.

Good luck!

https://www.codewars.com/kata/numbers-in-strings/train/python
"""

import re

def solve(s):
    numbers = re.findall(r"\d+", s)
    return max(int(i) for i in numbers)

print(solve('f7g42g16hcu5'))
