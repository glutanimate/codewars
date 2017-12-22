""" Delete occurrences of an element if it occurs more than n times

Alice and Bob were on a holiday. Both of them took many pictures of the places they've been, and now they want to show Charlie their entire collection. However, Charlie doesn't like this sessions, since the motive usually repeats. He isn't fond of seeing the Eiffel tower 40 times. He tells them that he will only sit during the session if they show the same motive at most N times. Luckily, Alice and Bob are able to encode the motive as a number. Can you help them to remove numbers such that their list contains each number only up to N times, without changing the order?

Task

Given a list lst and a number N, create a new list that contains each number of lst at most N times without reordering. For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].

Example

  delete_nth ([1,1,1,1],2) # return [1,1]

  delete_nth ([20,37,20,21],1) # return [20,37,21]


Tags: FUNDAMENTALS, LISTS, DATA STRUCTURES

Link: https://www.codewars.com/kata/delete-occurrences-of-an-element-if-it-occurs-more-than-n-times
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

def delete_nth(order, max_e):
    occ = {}
    delcnt = 0
    print max_e
    for idx in range(0, len(order)):
        idx = idx - delcnt
        i = order[idx]
        if i not in occ:
            occ[i] = 1
        else:
            occ[i] += 1
        print i, occ[i]
        if occ[i] > max_e:
            del order[idx]
            delcnt += 1
    return order



#############################################################
#             OTHER INTERESTING SOLUTIONS & REMARKS         #
#############################################################

def delete_nth2(order, max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e:
            ans.append(o)
    return ans


def delete_nth3(order, max_e):
    d = {}
    res = []
    for item in order:
      n = d.get(item, 0)
      if n < max_e:
        res.append(item)
        d[item] = n + 1
    return res



#############################################################
#                           TESTS                           #
#############################################################


test.describe("Basic tests")
test.assert_equals(delete_nth([20, 37, 20, 21], 1), [
                   20, 37, 21], "From list [20,37,20,21],1 you get")
test.assert_equals(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3), [
                   1, 1, 3, 3, 7, 2, 2, 2], "From list [1,1,3,3,7,2,2,2,2],3 you get ")
test.assert_equals(delete_nth([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], 3), [
                   1, 2, 3, 1, 1, 2, 2, 3, 3, 4, 5], "From list [1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1],3 you get ")
test.assert_equals(delete_nth([1, 1, 1, 1, 1], 5), [
                   1, 1, 1, 1, 1], "From list [1,1,1,1,1],5 you get ")
test.assert_equals(delete_nth([], 5), [], "From list [],5 you get")

test.describe("Random tests")
from random import randint, shuffle


def sol_nth(order, max_e):
    d = []
    for i in order:
        if d.count(i) < max_e:
            d.append(i)
    return d


for _ in range(40):
  order = reduce(lambda x, y: x + y,
                 [[randint(1, 50)] * randint(1, 10)for i in range(randint(3, 10))])
  shuffle(order)
  max_e = randint(1, 10)
  solution = sol_nth([] + order, max_e)
  test.it("Testing for delete_nth(" + str(order) + "," + str(max_e) + ")")
  test.assert_equals(delete_nth(order, max_e), solution,
                     "It should work on random inputs too!")
