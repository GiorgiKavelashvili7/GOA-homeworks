# Complete the function that takes two integers (a, b, where a < b) and return an array of all integers between the input parameters, including them.

def between(a, b):
    BOMBASTIC = []
    for bombastic in range(a, b):
        BOMBASTIC.append(bombastic)
    BOMBASTIC.append(b)
    return BOMBASTIC