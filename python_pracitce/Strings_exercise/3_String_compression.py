# String Compression

string = "aaabbcccc"
dictionary = {}
for char in string:
    dictionary[char] = dictionary.get(char, 0) + 1
for char in dictionary:
    print(f"{char}{dictionary[char]}", end="")
    
    