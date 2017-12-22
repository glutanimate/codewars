""" Find the Counterfeit

The Plot

The king is collecting taxes from his people, and he is receiving his payment in gold coins. He has a large bag of money, but he suspects that he might have been given a counterfeit coin! He turns to you for help. He needs to find if there are any fake coins, and if so, which coin is the fake one. However, the only tool you have at your disposal is a simple balancing scale. The king knows that if there is a fake coin, it will weigh a different amount than all of the other coins.

Your Code

Create a funciton find_counterfeit which takes a list of coins and returns the index of the counterfeit coin. If there are no fake coins, then it returns None. There will always be at least three coins in the input list, and there will be either one or no fake coins.

The Coins

A new class coin has already been created for you. Every coin has a weight attribute, but you can't directly access the value. The only way to determine a coin's weight is to use the pre-defined function balanced, which takes two inputs. Each input can either be a single coin or a list of coins. balanced returns True or False depending on if its two inputs have the same weight.

For example:

coins = [coin(1), coin(1), coin(1), coin(2), coin(1)]
    # The coin in position 3 has a different weight, so it is counterfeit.

balanced(coins[0], coins[1])
    # Returns True: The coins have the same weight.

balanced([coins[0], coins[1]], [coins[2], coins[4]])
    # Returns True: The coins 0 and 1 combined weigh the same as coins 2 and 4 combined.

balanced(coins[2], coins[3])
    # Returns False: The coins have different weights.

find_counterfeit(coins)
    # Returns 3: The coin in position 3 is counterfeit.


Tags: FUNDAMENTALS, LISTS, DATA STRUCTURES, CLASSES, BASIC LANGUAGE FEATURES, OBJECT-ORIENTED PROGRAMMING

Link: https://www.codewars.com/kata/find-the-counterfeit
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


def find_counterfeit(coins):
    unbalanced = False
    nr_of_coins = len(coins)
    for idx, coin in enumerate(coins):
        if idx == nr_of_coins - 1:
            next = 0
        else:
            next = idx + 1
        if not balanced(coin, coins[next]):
            if unbalanced:
                return idx
            unbalanced = True
        else:
            if unbalanced:
                return idx - 1
            unbalanced = False
    return None


#############################################################
#             OTHER INTERESTING SOLUTIONS & REMARKS         #
#############################################################


def find_counterfeit2(coins):
    real = coins[0] if balanced(coins[0], coins[1]) else coins[2]
    for i, coin in enumerate(coins):
        if not balanced(coin, real):
            return i
    return None


#############################################################
#                           TESTS                           #
#############################################################

test.describe('Basic Tests')

coins = [coin(1), coin(1), coin(1), coin(2), coin(1)]
test.assert_equals(find_counterfeit(coins), 3)

coins = [coin(1), coin(1), coin(1), coin(1), coin(1)]
test.assert_equals(find_counterfeit(coins), None)

coins = [coin(1), coin(2), coin(1)]
test.assert_equals(find_counterfeit(coins), 1)

coins = [coin(2), coin(1), coin(1), coin(1), coin(1)]
test.assert_equals(find_counterfeit(coins), 0)

coins = [coin(1)] * 100 + [coin(2)] + [coin(1)] * 22
test.assert_equals(find_counterfeit(coins), 100)

coins = [coin(1)] * 100
test.assert_equals(find_counterfeit(coins), None)

coins = [coin(2)] + [coin(1)] * 100
test.assert_equals(find_counterfeit(coins), 0)

coins = [coin(1)] * 100 + [coin(2)]
test.assert_equals(find_counterfeit(coins), 100)
