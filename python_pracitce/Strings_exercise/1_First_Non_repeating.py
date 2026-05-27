# Program to find the first non repeating character
# We use count()
# could do when told to use count()

# My way
string = "aabbccdpe"
store = {}
for item in string:
    if string.count(item) > 1:
        continue
    else:
        print(item)
        break

# Standard flag way
string = "swiss"
found = False
for char in string:
    if string.count(char) == 1:
        print(f"The first non-repeating is: {char}")   # Here the loops runs for every character even when found True
        found = True                                   # runs very slow for large data
        break

if not found:
    print(f"The word has repeating characters or empty string")

# A backend performer
text = "hhaallelujah"
dict = {}
for char in text:
    dict[char] = dict.get(char, 0) + 1

for char in text:
    if dict[char] == 1:
        print(f"The first Non-repeating is: {char}")
        break
