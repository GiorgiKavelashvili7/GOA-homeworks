# String Formatting
# Create a string named template with the following content: "Hello, {name}. Welcome to {place}."
# Use the format() function to replace {name} with "Alice" and {place} with "Wonderland". Store the result in a variable named formatted_string and print it.

template = "Hello, {name}. Welcome to {place}."
formatted_string = template.format(name="alice", place="wonderland")
print(formatted_string)