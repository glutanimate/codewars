# -*- coding: utf-8 -*-
""" Fruit Machine

Introduction

Slot machine (American English), informally fruit machine (British English), puggy (Scottish English slang), the slots (Canadian and American English), poker machine (or pokies in slang) (Australian English and New Zealand English) or simply slot (American English), is a casino gambling machine with three or more reels which spin when a button is pushed. Slot machines are also known as one-armed bandits because they were originally operated by one lever on the side of the machine as distinct from a button on the front panel, and because of their ability to leave the player in debt and impoverished. Many modern machines are still equipped with a legacy lever in addition to the button. (Source Wikipedia)
 
Task

You will be given three reels of different images and told at which index the reels stop. From this information your job is to return the score of the resulted reels.

Rules

1. There are always exactly three reels
2. Each reel has 10 different items.
3. The three reel inputs may be different.
4. The spin array represents the index of where the reels finish.
5. The three spin inputs may be different
6. Three of the same is worth more than two of the same
7. Two of the same plus one "Wild" is double the score.
8. No matching items returns 0.

Scoring:

Item                                Wild    Star    Bell    Shell   Seven   Cherry  Bar     King    Queen   Jack
Three of the same                   100     90      80      70      60      50      40      30      20      10
Two of the same                     10      9       8       7       6       5       4       3       2       1
Two of the same plus one Wild       N/A     18      16      14      12      10      8       6       4       2

Returns

Return an integer of the score.

Example

Initialise

reel1 = ["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]
reel2 = ["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]
reel3 = ["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]
spin = [5,5,5]
result = fruit([reel1,reel2,reel3],spin)

Scoring

reel1[5] == "Cherry"
reel2[5] == "Cherry"
reel3[5] == "Cherry"

Cherry + Cherry + Cherry == 50

Tags: FUNDAMENTALS, ARRAYS, GAMES

Link: https://www.codewars.com/kata/fruit-machine
"""

#############################################################
#                        MY SOLUTIONS                       #
#############################################################

from collections import Counter

score_by_image = {"Jack": 1, "Queen": 2, "King": 3, "Bar": 4,
                  "Cherry": 5, "Seven": 6, "Shell": 7, "Bell": 8,
                  "Star": 9, "Wild": 10}

def fruit(reels, spins):
    images = [reel[spin] for reel, spin in zip(reels, spins)]
    
    counts = Counter(images)
    counts_len = len(counts)
    if counts_len == 1:
        multiplier = 10
    elif counts_len == 2 and counts["Wild"] == 1:
        multiplier = 2
    elif counts_len == 2:
        multiplier = 1
    else:
        return 0
    
    winning_image = counts.most_common(1)[0][0]
    
    return score_by_image[winning_image] * multiplier
    
    



#############################################################
#             OTHER INTERESTING SOLUTIONS & REMARKS         #
#############################################################


# Clever, succinct solution that malfunctions when 2 "Wild" are struck:
def fruit(reels, spins):
    fruits = {"Wild": 10, "Star": 9, "Bell": 8, "Shell": 7, "Seven": 6,
              "Cherry": 5, "Bar": 4, "King": 3, "Queen": 2, "Jack": 1}
    # depends on alphabetic sorting of image names. Thus would stop
    # working if we were to add "Zebra" to the list:
    spin = sorted(reels[i][spins[i]] for i in range(3))
    matches = len(set(spin))

    if matches == 1:
        return fruits[spin[0]] * 10

    if matches == 2:
        # return fruits[spin[0]] * 2 if spin[2] == "Wild" else fruits[spin[1]]
        # fix for 2 wild:
        return fruits[spin[0]] * 2 if (spin[2] == "Wild" and spin[1] != "Wild") else fruits[spin[1]]

    return 0



#############################################################
#                           TESTS                           #
#############################################################

import sys, os
sys.path.append(os.path.abspath(
                os.path.join(os.path.dirname(__file__), '..', "tests")))
from Test import *


reel = ["Wild", "Star", "Bell", "Shell", "Seven",
        "Cherry", "Bar", "King", "Queen", "Jack"]
spin = [0, 0, 1]
test.it("Should return: '10'")
test.assert_equals(fruit([reel, reel, reel], spin),
                   10, "Should return: '10'")

reel1 = ["Wild", "Star", "Bell", "Shell", "Seven",
         "Cherry", "Bar", "King", "Queen", "Jack"]
reel2 = ["Bar", "Wild", "Queen", "Bell", "King",
         "Seven", "Cherry", "Jack", "Star", "Shell"]
reel3 = ["Bell", "King", "Wild", "Bar", "Seven",
         "Jack", "Shell", "Cherry", "Queen", "Star"]
spin = [5, 4, 3]
test.it("Should return: '0'")
test.assert_equals(fruit([reel1, reel2, reel3], spin), 0, "Should return: '0'")

reel1 = ["King", "Cherry", "Bar", "Jack", "Seven",
         "Queen", "Star", "Shell", "Bell", "Wild"]
reel2 = ["Bell", "Seven", "Jack", "Queen", "Bar",
         "Star", "Shell", "Wild", "Cherry", "King"]
reel3 = ["Wild", "King", "Queen", "Seven", "Star",
         "Bar", "Shell", "Cherry", "Jack", "Bell"]
spin = [0, 0, 1]
test.it("Should return: '3'")
test.assert_equals(fruit([reel1, reel2, reel3], spin), 3, "Should return: '3'")

reel1 = ["King", "Jack", "Wild", "Bell", "Star",
         "Seven", "Queen", "Cherry", "Shell", "Bar"]
reel2 = ["Star", "Bar", "Jack", "Seven", "Queen",
         "Wild", "King", "Bell", "Cherry", "Shell"]
reel3 = ["King", "Bell", "Jack", "Shell", "Star",
         "Cherry", "Queen", "Bar", "Wild", "Seven"]
spin = [0, 5, 0]
test.it("Should return: '6'")
test.assert_equals(fruit([reel1, reel2, reel3], spin), 6, "Should return: '6'")


def fruitSolveIt(reels, spins):
    reel = ["Wild", "Star", "Bell", "Shell", "Seven",
            "Cherry", "Bar", "King", "Queen", "Jack"]
    items = [reels[0][spins[0]]][0], [
        reels[1][spins[1]]][0], [reels[2][spins[2]]][0]
    if items[0] == items[1] and items[0] == items[2]:
        return (10 - reel.index(items[0])) * 10
    item = ""
    extra = ""
    if items[0] == items[1]:
        item = items[0]
        extra = items[2]
    if items[0] == items[2]:
        item = items[0]
        extra = items[1]
    if items[1] == items[2]:
        item = items[1]
        extra = items[0]
    if item != "":
        num = 10 - reel.index(item)
        if extra == "Wild":
            num = num * 2
        return num
    return 0


assert False

import random
test.describe("Random tests")
reelz = ["Wild", "Star", "Bell", "Shell", "Seven",
         "Cherry", "Bar", "King", "Queen", "Jack"]
for cwtests in range(0, 96):
    reel1z = random.sample(reelz, len(reelz))
    reel2z = random.sample(reelz, len(reelz))
    reel3z = random.sample(reelz, len(reelz))
    spinsz = [random.randint(0, len(
        reelz)-1), random.randint(0, len(reelz)-1), random.randint(0, len(reelz)-1)]
    print("Reel 1 = " + str(reel1z))
    print("Reel 2 = " + str(reel2z))
    print("Reel 3 = " + str(reel3z))
    print("Testing for " + str(spinsz))
    resultz = fruitSolveIt([reel1z, reel2z, reel3z], spinsz)
    print("Expecting result = "+str(resultz))
    test.assert_equals(fruit([reel1z, reel2z, reel3z], spinsz),
                       resultz, "Should return: '"+str(resultz)+"'")
