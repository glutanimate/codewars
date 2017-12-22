""" Your order, please

Your task is to sort a given string. Each word in the String will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input String is empty, return an empty String. The words in the input String will only contain valid consecutive numbers.

For an input: "is2 Thi1s T4est 3a" the function should return "Thi1s is2 3a T4est"

your_order("is2 Thi1s T4est 3a")
[1] "Thi1s is2 3a T4est"


Tags: FUNDAMENTALS STRINGS

Link: https://www.codewars.com/kata/your-order-please
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


def order(sentence):
    words = {}
    for word in sentence.split():
        for l in word:
            try:
                l = int(l)
                words[l] = word
            except ValueError:
                pass
    return " ".join(words[i] for i in sorted(words.keys()))


#############################################################
#             OTHER INTERESTING SOLUTIONS & REMARKS         #
#############################################################

# very clever approach: sort words to make them sortable
def order2(words):
    return ' '.join(sorted(words.split(), key=lambda w: sorted(w)))


# although it would be more succint and efficient to instead use sorted
# as a key directly:
def order3(words):
    return ' '.join(sorted(words.split(), key=sorted))


#############################################################
#                           TESTS                           #
#############################################################

order = order3

test.assert_equals(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
test.assert_equals(order("4of Fo1r pe6ople g3ood th5e the2"),
                   "Fo1r the2 g3ood 4of th5e pe6ople")
test.assert_equals(order("d4o dru7nken sh2all w5ith s8ailor wha1t 3we a6"),
                   "wha1t sh2all 3we d4o w5ith a6 dru7nken s8ailor")
test.assert_equals(order(""), "")
test.assert_equals(order("3 6 4 2 8 7 5 1 9"), "1 2 3 4 5 6 7 8 9")
