""" Stop gninnipS My sdroW!

Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.


Examples:

spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test"

Tags: ALGORITHMS STRINGS FORMATTING

Link: Link
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


def spin_words(sentence):
    # Your code goes here
    res = []
    for i in sentence.split():
        if len(i) >= 5:
            res.append(i[::-1])
        else:
            res.append(i)
    return ' '.join(res)


#############################################################
#             OTHER INTERESTING SOLUTIONS & REMARKS         #
#############################################################

def spin_words2(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])



#############################################################
#                           TESTS                           #
#############################################################


test.describe("Single word")
test.assert_equals(spin_words("Welcome"), "emocleW")
test.assert_equals(spin_words("to"), "to")
test.assert_equals(spin_words("CodeWars"), "sraWedoC")

test.describe("Multiple words")
test.assert_equals(spin_words("Hey fellow warriors"), "Hey wollef sroirraw")

test.describe("Random testing")


def known_good(sentence):
    words = [word for word in sentence.split(" ")]
    words = [word if len(word) < 5 else word[::-1] for word in words]
    return " ".join(words)


import random
source = "Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present."


def is_valid(c): return 'a' <= c <= 'z' or 'A' <= c <= 'Z' or c == ' '


source = "".join([c for c in source if is_valid(c)])
source = [w for w in source.split(" ")]

for _ in xrange(20):
    words = []
    for _ in xrange(random.randrange(1, 30)):
        words.append(random.choice(source))
    words = " ".join(words)
    test.assert_equals(spin_words(words), known_good(words))
