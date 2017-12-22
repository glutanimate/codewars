"""
Letterss of natac: build or buy

Letterss of Natac

In a game I just made up that doesn’t have anything to do with any other game
that you may or may not have played, you collect resources on each turn and then
use those resources to build settlements, roads, and cities or buy a
development. Other kata about this game can be found here.

Task

This kata asks you to implement the function build_or_buy(hand) , which takes as
input a hand, the resources you have (a string of letters representing the
resources you have), and returns a list of the unique game objects you can build
or buy given your hand.

There are five different resources, 'b', 'w', 'g', 's', and 'o'.

Game objects and the resources required to build or buy them are as follows:

'road': bw 'settlement': bwsg 'city': ooogg 'development': osg Examples

build_or_buy("bwoo")  => ['road'] build_or_buy("bwsg")  => ['road',
'settlement'] or ['settlement', 'road'] build_or_buy("")      => []
build_or_buy("ogogoogogo")  => ['city'] Notes:

Don't mutate the hand The order of the returned list doesn't matter You do not
have to test for whether a hand is valid. The list will be interpreted to mean
'you can build any of these objects,' not 'you can build all these objects in
one play'. See example 2 above, even though there is only one 'b' and one 'w' in
hand, both Road() and Settlement() are in the list. A hand can be empty. In the
event a hand is empty, you can't build or buy anything, so return an empty list,
see example 3 above. Hand are between 0 and 39 in length.

https://www.codewars.com/kata/letterss-of-natac-build-or-buy/train/python
"""

from collections import Counter

requirements = {
    "road": Counter("bw"),
    "settlement": Counter("bwsg"),
    "city": Counter("ooogg"),
    "development": Counter("osg")
}


def build_or_buy(hand):
    res = Counter(hand)

    fulfillable = []
    for name, req in requirements.items():
        if all(res[i] >= req[i] for i in req.keys()):
            fulfillable.append(name)
    return fulfillable


print(build_or_buy("bwsg"))
print(build_or_buy("bwoo"))
print(build_or_buy(""))
print(build_or_buy("ogogoogogo"))



# "Goldstandard solutions"

from collections import Counter

reqs = {"road": Counter("bw"), "settlement": Counter("bwsg"),
        "city": Counter("ooogg"), "development": Counter("osg")}


def build_or_buy(hand):
    # ↓ you can actually subtract one Counter object from another,
    # producing a new Counter of the result
    return list(filter(lambda obj: not reqs[obj] - Counter(hand), reqs.keys()))
