""" Who likes it?

You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. It must return the display text as shown in the examples:

likes [] // must be "no one likes this"
likes ["Peter"] // must be "Peter likes this"
likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"
For more than 4 names, the number in and 2 others simply increases.

Tags: FUNDAMENTALS FORMATTING ALGORITHMS STRINGS

Link: https://www.codewars.com/kata/who-likes-it
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

def likes(names):
    length = len(names)
    if not length:
        return "no one likes this"
    elif length == 1:
        return "%s likes this" % names[0]
    elif length == 2:
        return "%s and %s like this" % (names[0], names[1])
    elif length == 3:
        return "%s, %s and %s like this" % (names[0], names[1], names[2])
    else:
        return "%s, %s and %i others like this" % (names[0], names[1], length - 2)



#############################################################
#             OTHER INTERESTING SOLUTIONS & REMARKS         #
#############################################################

# using a dictionary to deal with multiple possible formatting
# templates:
def likes2(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n - 2)



#############################################################
#                           TESTS                           #
#############################################################

test.describe('Basic tests')
test.assert_equals(likes([]), 'no one likes this')
test.assert_equals(likes(['Peter']), 'Peter likes this')
test.assert_equals(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
test.assert_equals(likes(['Max', 'John', 'Mark']),
                   'Max, John and Mark like this')
test.assert_equals(likes(['Alex', 'Jacob', 'Mark', 'Max']),
                   'Alex, Jacob and 2 others like this')

test.describe("Random tests")
from random import randint, shuffle


def sol(n): return 'no one likes this' if len(n) == 0 else n[0] + ' likes this' if len(n) == 1 else n[0] + ' and ' + n[1] + ' like this' if len(
    n) == 2 else n[0] + ', ' + n[1] + ' and ' + n[2] + ' like this' if len(n) == 3 else n[0] + ', ' + n[1] + ' and ' + str(len(n) - 2) + ' others like this'


base = ["Sylia Stingray", "Priscilla S. Asagiri", "Linna Yamazaki", "Nene Romanova", "Nigel", "Macky Stingray",
        "Largo", "Brian J. Mason", "Sylvie", "Anri", "Leon McNichol", "Daley Wong", "Galatea", "Quincy Rosenkreutz"]

for _ in xrange(40):
    shuffle(base)
    names = base[:randint(0, len(base) - 1)]
    test.it("Testig for %s" % (", ".join(names) if len(names) > 0 else "none"))
    test.assert_equals(likes(names), sol(
        names), "It should work for random inputs too")
