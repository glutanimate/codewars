#!/usr/bin/python3

"""
Consecutive strings

You are given an array strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.

#Example: longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

https://www.codewars.com/kata/consecutive-strings
"""


def longest_consec(strarr, k):
    n = len(strarr)
    if k <= 0 or k > n or n == 0:
        return ""

    last_start_idx = n - k

    longest_comp = ""
    longest_comp_length = 0

    for idx, substring in enumerate(strarr[:last_start_idx + 1]):
        composite = "".join(strarr[idx:idx + k])
        composite_length = len(composite)
        if composite_length > longest_comp_length:
            longest_comp, longest_comp_length = composite, composite_length

    return longest_comp


print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))

"""
Problems and optimizations:

joining the strings again and again is very expensive. Instead, one might opt 
to calculate and add the length of the constituent strings. In order to avoid
duplicate calculations you could generate an array with the lengths of each
substring beforehand → dynamic programming
"""
