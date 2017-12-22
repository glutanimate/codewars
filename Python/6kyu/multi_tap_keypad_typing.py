# -*- coding: utf-8 -*-
""" Multi-tap Keypad Text Entry on an Old Mobile Phone

Prior to having fancy iPhones, teenagers would wear out their thumbs sending SMS messages on candybar-shaped feature phones with 3x4 numeric keypads.

------- ------- -------
|     | | ABC | | DEF |
|  1  | |  2  | |  3  |
------- ------- -------
------- ------- -------
| GHI | | JKL | | MNO |
|  4  | |  5  | |  6  |
------- ------- -------
------- ------- -------
|PQRS | | TUV | | WXYZ|
|  7  | |  8  | |  9  |
------- ------- -------
------- ------- -------
|     | |space| |     |
|  *  | |  0  | |  #  |
------- ------- -------
Prior to the development of T9 (predictive text entry) systems, the method to type words was called "multi-tap" and involved pressing a button repeatedly to cycle through the possible values.

For example, to type a letter "R" you would press the 7 key three times (as the screen display for the current character cycles through P->Q->R->S->7). A character is "locked in" once the user presses a different key or pauses for a short period of time (thus, no extra button presses are required beyond what is needed for each letter individually). The zero key handles spaces, with one press of the key producing a space and two presses producing a zero.

In order to send the message "WHERE DO U WANT 2 MEET L8R" a teen would have to actually do 47 button presses. No wonder they abbreviated.

For this assignment, write a module that can calculate the amount of button presses required for any phrase. Punctuation can be ignored for this exercise. Likewise, you can assume the phone doesn't distinguish between upper/lowercase characters (but you should allow your module to accept input in either for convenience).

Hint: While it wouldn't take too long to hard code the amount of keypresses for all 26 letters by hand, try to avoid doing so! (Imagine you work at a phone manufacturer who might be testing out different keyboard layouts, and you want to be able to test new ones rapidly.)


Tags: FUNDAMENTALS

Link: https://www.codewars.com/kata/multi-tap-keypad-text-entry-on-an-old-mobile-phone
"""

#############################################################
#                       TEST FRAMEWORK                      #
#############################################################

import sys, os
sys.path.append(os.path.abspath(
                os.path.join(os.path.dirname(__file__), '..', "tests")))
from Test import *


#############################################################
#                        MY SOLUTIONS                       #
#############################################################

kg = ["1", "ABC2", "DEF3", "GHI4", "JKL5", "MNO6", "PQRS7",
      "TUV8", "WXYZ9", "*", " 0", "#"]


def presses(p):
    return sum(g.find(i) + 1 for g in kg for i in p.upper())



#############################################################
#             OTHER INTERESTING SOLUTIONS & REMARKS         #
#############################################################





#############################################################
#                           TESTS                           #
#############################################################



keys = ["1", "ABC2", "DEF3", "GHI4", "JKL5", "MNO6",
        "PQRS7", "TUV8", "WXYZ9", "*", " 0", "#"]
test.describe("Basic Tests")
test.it("should work for simple words")
test.assert_equals(presses("LOL"), 9)
test.it("should work for phrases with spaces")
test.assert_equals(presses("HOW R U"), 13)
test.it("should work for phrases with numbers")
test.assert_equals(presses("WHERE DO U WANT 2 MEET L8R"), 47)
test.it("should allow input in lowercase")
test.assert_equals(presses("lol"), 9)
test.it("should handle the 0 digit")
test.assert_equals(presses("0"), 2)
test.assert_equals(presses("ZER0"), 11)
test.it("should handle the 1 digit")
test.assert_equals(presses("1"), 1)
test.assert_equals(presses("IS NE1 OUT THERE"), 31)
test.it("should handle non-alphabetic characters")
test.assert_equals(presses("#"), 1)
test.assert_equals(presses("#codewars #rocks"), 36)

test.describe("Random Tests")
from random import randint
keystrokes = {' ': 1, '#': 1, '*': 1, '1': 1, '0': 2, '3': 4, '2': 4, '5': 4, '4': 4, '7': 5, '6': 4, '9': 5, '8': 4, 'A': 1, 'C': 3, 'B': 2, 'E': 2, 'D': 1, 'G': 1,
              'F': 3, 'I': 3, 'H': 2, 'K': 2, 'J': 1, 'M': 1, 'L': 3, 'O': 3, 'N': 2, 'Q': 2, 'P': 1, 'S': 4, 'R': 3, 'U': 2, 'T': 1, 'W': 1, 'V': 3, 'Y': 3, 'X': 2, 'Z': 4}


def solmobile(phrase): return sum(
    map(lambda letter: keystrokes[letter], phrase.upper()))


for _ in range(40):
    phrase = "".join(["".join(keys)[randint(0, 38)]
                      for x in range(randint(5, 25))])
    test.it("Testing for " + phrase)
    test.assert_equals(presses(phrase), solmobile(phrase),
                       "It should work for random inputs too")
