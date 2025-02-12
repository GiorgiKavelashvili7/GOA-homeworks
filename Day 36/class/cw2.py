"""
Given a non-empty array of integers, return the result of multiplying the values together in order. Example:
"""

def grow(arr):
    sum = 1
    for i in arr:
        sum *= i
    return sum