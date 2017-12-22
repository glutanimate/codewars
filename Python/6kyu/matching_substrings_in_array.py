""" Which are in?

Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.

#Example 1: a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns ["arp", "live", "strong"]

#Example 2: a1 = ["tarp", "mice", "bull"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns []

Notes:

Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.

In Shell bash a1 and a2 are strings. The return is a string where words are separated by commas.

Beware: r must be without duplicates.

Tags: REFACTORING, ARRAYS, SEARCH, ALGORITHMS, LISTS, DATA

Link: https://www.codewars.com/kata/which-are-in
"""

#############################################################
#                       TEST FRAMEWORK                      #
#############################################################

import sys, os
sys.path.append(os.path.abspath(
                os.path.join(os.path.dirname(__file__), '..', "tests")))
from Test import *


#############################################################
#                         SOLUTIONS                         #
#############################################################

def in_array(array1, array2):
    return sorted(set(i for i in array1 if any(s.find(i) != -1 for s in array2)))


#############################################################
#                           TESTS                           #
#############################################################

a1 = ["live", "arp", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
r = ['arp', 'live', 'strong']
test.assert_equals(in_array(a1, a2), r)

a1 = ["arp", "mice", "bull"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
r = ['arp']
test.assert_equals(in_array(a1, a2), r)

a1 = ["cod", "code", "wars", "ewar"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong", "codewars"]
r = ["cod", "code", "ewar", "wars"]
test.assert_equals(in_array(a1, a2), r)

a1 = ["cod", "code", "wars", "ewar", "ar"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong", "codewars"]
r = ["ar", "cod", "code", "ewar", "wars"]
test.assert_equals(in_array(a1, a2), r)

a1 = ["cod", "code", "wars", "ewar", "ar"]
a2 = []
r = []
test.assert_equals(in_array(a1, a2), r)

a1 = ["1295", "code", "1346", "1028", "ar"]
a2 = ["12951295", "ode", "46", "10281066", "par"]
r = ["1028", "1295", "ar"]
test.assert_equals(in_array(a1, a2), r)

a1 = ["&()", "code", "1346", "1028", "ar"]
a2 = ["12&()95", "coderange", "46", "1066", "par"]
r = ["&()", "ar", "code"]
test.assert_equals(in_array(a1, a2), r)

a1 = ["ohio", "code", "1346", "1028", "art"]
a2 = ["Carolina", "Ohio", "4600", "NY", "California"]
r = []
test.assert_equals(in_array(a1, a2), r)

a1 = ["duplicates", "duplicates"]
a2 = ["duplicates", "duplicates"]
r = ["duplicates"]
test.assert_equals(in_array(a1, a2), r)


#############################################################
#                      COMMENTS, ETC.                       #
#############################################################



