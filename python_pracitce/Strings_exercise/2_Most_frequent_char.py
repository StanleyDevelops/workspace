# Program to find most repeating character

# My way
string =  "Mississippi"

most_repeating = string[0]
for char in string[1:]:
    if string.count(char) > string.count(most_repeating):
        most_repeating = char     # never put equal operator here

print(f"Most Repeating: {most_repeating}")


# Using The Frequency dictionary

text = "Mississippi"
dictionary = {}
for char in text:
    dictionary[char] = dictionary.get(char, 0) + 1   # maps only once

most_frequent = text[0]
for char in dictionary:    # 
    if dictionary[char] > dictionary[most_frequent]:  # Only compares values 
        most_frequent = char

print(f"Most frequent: {most_frequent}")