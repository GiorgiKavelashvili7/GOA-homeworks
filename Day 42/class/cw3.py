"""
Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.
"""

def replace_exclamation(st):
    res = ""
    for i in st:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
            res += "!"
        else:
            res += i
    return res