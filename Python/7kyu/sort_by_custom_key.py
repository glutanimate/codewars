"""
Order of weight

Given an array of strings, sort the array into order of weight from light to heavy.

Weight units are grams(G), kilo-grams(KG) and tonnes(T).

Arrays will always contain correct and positive values aswell as uppercase letters.

https://www.codewars.com/kata/order-of-weight/train/python
"""


def weight_sort(weight):
    if weight.endswith("KG"):
        return int(weight[:-2])
    elif weight.endswith("G"):
        return 0.001 * int(weight[:-1])
    elif weight.endswith("T"):
        return 1000 * int(weight[:-1])


def arrange(arr):
    return sorted(arr, key=weight_sort)


def arrange(arr):
    return sorted(arr, key=weight_sort)


print(arrange(["100KG", "100G", "150T", "150KG"]))
