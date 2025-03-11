"""
Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

If the input is an empty array or is null, return an empty array.
"""


def count_positives_sum_negatives(arr):
    positives = 0
    negatives = 0
    if len(arr) == 0:
        return arr
    for i in arr:
        if i > 0:
            positives = positives + 1
        elif i < 0:
            negatives = negatives + i
        
    return [positives, negatives]