""" Sum of a nested list
Implement a function to calculate the sum of the numerical values in a nested list. For example :

sum_nested([1, [2, [3, [4]]]]) -> 10

https://www.codewars.com/kata/sum-of-a-nested-list/train/python
"""

def sum_nested(lst):
    res = 0
    # traverse list recursively, adding values as we go
    for i in lst:
        # use duck-typing to identify iterators:
        try:
            res += i
        except TypeError:
            # NOTE: no explicit type checking performed, so strings
            # and other unforeseen list elements could cause problems
            res += sum_nested(i)
    return res


assert(sum_nested([1, [1], [[1]], [[[1]]]]) == 4)
assert(sum_nested([1, [2, [3, [4]]]]) == 10)


""" Alternate solutions """

# top-answer on codewars using recursive sum() calls:

def sum_nested2(lst):
    return sum(sum_nested2(x) if isinstance(x, list) else x for x in lst)


# using a generator:

def traverse(lst):
    try:
        for i in iter(lst):
            for j in traverse(i):
                yield j
    except TypeError:
        yield lst

def sum_nested3(lst):
    return sum(traverse(lst))

print(sum_nested3([1, [2, [3, [4]]]]))

# Comparison

import timeit

print(timeit.timeit(lambda x=[1, [2, [3, [4]]]]: sum_nested(x)))  # 5 secs
print(timeit.timeit(lambda x=[1, [2, [3, [4]]]]: sum_nested2(x)))  # 3 secs
print(timeit.timeit(lambda x=[1, [2, [3, [4]]]]: sum_nested3(x)))  # 8 secs (!)
