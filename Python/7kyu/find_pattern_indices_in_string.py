#!/usr/bin/python3
"""
Find the motif in DNA sequence.

In genetics, a sequence’s motif is a nucleotides (or amino-acid) sequence pattern. Sequence motifs have a biological significance. For more information you can take a look here.

For this kata you need to complete the function motif_locator. This function receives 2 arguments - a sequence and a motif. Both arguments are strings.

You should return an array that contains all the start positions of the motif (in order). A sequence may contain 0 or more repetitions of the given motif. Note that the number of the first position is 1, not 0.

Some examples:

For the sequence "ACGTGGGGACTAGGGG" and the motif "GGGG" the result should be [5, 13].
For the sequence "ACCGTACCAAGGGACC" and the motif "AAT" the result should be []
For the sequence "GGG" and the motif "GG" the result should be [1, 2]

https://www.codewars.com/kata/find-the-motif-in-dna-sequence/train/python
"""


def motif_locator(sequence, motif):
    mot_length = len(motif)
    max_start = len(sequence) - mot_length
    match_starts = []
    for idx, base in enumerate(sequence[:max_start + 1]):
        substring = sequence[idx:idx + mot_length]
        if substring == motif:
            match_starts.append(idx + 1)
    return match_starts


print(motif_locator("TTCCGGAACC", "CC"))


# Better solutions:


def motif_locator(sequence, motif):
    res, i = [], 0
    while True:
        i = sequence.find(motif, i) + 1
        if not i: return res
        res.append(i)

# TODO: rework into generator