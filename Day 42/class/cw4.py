"""
Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

If the input is an empty array or is null, return an empty array.
"""

def count_positives_sum_negatives(arr):
    if not arr:
        return []
    pos = 0
    neg = 0
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += i
    return [pos, neg]
