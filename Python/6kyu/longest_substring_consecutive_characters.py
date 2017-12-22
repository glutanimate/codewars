#!/usr/bin/python3

"""
Character with longest repetition

For a given string s find the character c with longest consecutive repetition and return a tuple (c, l) (in Haskell Just (Char, Int), in C# Tuple<char?, int>, in Shell a String of comma-separated values c,l, in JavaScript [c,l]) where l is the length of the repetition. If there are two or more characters with the same l return the first.

For empty string return ('', 0) (in Haskell Nothing, in C# Tuple<char, int>(null, 0), in Shell ,0, in JavaScript ["",0])

https://www.codewars.com/kata/character-with-longest-repetition
"""

from operator import itemgetter

def longest_repetition(chars):
    if not chars:
        return ("", 0)

    streaks = []
    count = 1

    for idx, base in enumerate(chars):
        try:
            nxt = chars[idx + 1]
        except IndexError:
            nxt = ""
        if nxt == base:
            count += 1
        else:
            streaks.append((base, count))
            count = 1
    
    return max(streaks, key=itemgetter(1))

print(longest_repetition("bbbaaabaaaa"))

"""
Issues with implementation above: 

- performance: looping twice (for, and max). Could solve this without creating a streak array,
  instead keeping track of current max streak and character.

"""



# Interesting solutions:

def longest_repetition(chars):
    """
    Solution using itertools.groupby
    """
    from itertools import groupby
    return max(((char, len(list(group))) for char, group in groupby(chars)),
               key=lambda char_group: char_group[1], default=("", 0))