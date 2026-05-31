# counting frequency of words

_string = 'python is easy and python is powerful'
my_dict = {}

for char in _string.split(" "):
    my_dict[char] = my_dict.get(char, 0) + 1
print(my_dict)