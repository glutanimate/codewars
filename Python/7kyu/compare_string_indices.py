"""
Alphabet symmetry

Consider the word "abode". We can see that the letter a is in position 1 and b is in position 2. In the alphabet, a and b are also in positions 1 and 2. Notice that d and e also occupy the positions they would occupy in the alphabet, which are positions 4 and 5.

Given an array of words, return an array of the number of letters that occupy their positions in the alpahabet for each word. For example, solve(["abode","ABc","xyzD"]) = [4,3,1]. See test cases for more examples.

Input will consist of alphabet characters, both uppercase and lowercase. No spaces.

Good luck!

If you like this Kata, please try:

Last digit symmetry

Alternate capitalization

https://www.codewars.com/kata/alphabet-symmetry/train/python
"""

alphabet = "abcdefghijklmnopqrstuvwxyz"


def solve(arr):
    res = []
    for word in arr:
        count = sum(c == alphabet[idx] for idx, c in enumerate(word[:26].lower()))
        res.append(count)
    return res


solve(["sadfb"])

# minified:


def solve(arr):
    return [sum(c == "abcdefghijklmnopqrstuvwxyz"[idx]
            for idx, c in enumerate(word[:26].lower())) for w in arr]
