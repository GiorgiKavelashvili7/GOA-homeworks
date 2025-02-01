# Task: Format a String
# Write a Python program that takes a user's name and age as input. Use the format() function to create a sentence that says, "Hello, [Name]! You are [Age] years old."

name = input()
age = input()
info = "Hello, {name}! You are {age} years old."
formated_info = info.format(name="NAME", age="AGE")
print(formated_info)