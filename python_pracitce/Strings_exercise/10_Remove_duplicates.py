# Method 1
word = "Hallelujah"

new_word = ""     # a simple standard logic
for char in word:
    if char not in new_word:
        new_word += char

print(new_word)

# Method 2

text = "extraordinary"
result = "".join(dict.fromkeys(text))
print(result)

# Using set - random - no duplicates
letter = "casualities"
new_text = "".join(set(letter))
print(new_text)
