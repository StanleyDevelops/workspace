# 3 Methods to check frequency of a character using Dictionary and string operations

## Method I
string = "Kerketta"

frequency_dict = {}
for char in string:
    if char in frequency_dict:
        frequency_dict[char] += 1
    else:
        frequency_dict[char] = 1

print("The Frequency Dictionary: ")
for char, count in frequency_dict.items():
    print(f"{char}: {count}")

# Method II
string = "Ashish"

diction = {}
for char in string:      # .get(key, default) looks for a key
    diction[char] = diction.get(char, 0) + 1

print("Ye Another Frequency Dictionary: ")
for char, count in diction.items():
    print(f"{char}: {count}")

# Methof III  [Industry Standard]
from collections import Counter

text = "Interstellar"
new_text = Counter(text)
print(new_text)


