# 1 - Sort a list of names alphabetically, then reverse alphabetically
name = ["stanley", "niral", "kerketta", "master"]
print(sorted(name))
print(sorted(name, reverse = True))

# 2 - Sort ["banana", "fig", "apple"] by the last letter of each word
fruit = ["banana", "fig", "apple"]
print(sorted(fruit, key=lambda x: x[-1]))

# 3 - Given a list of dicts like [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}], sort by age
lis_dic = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
print(sorted(lis_dic, key = lambda index: index["age"]))

# 4 - Sorting a strings give you list
string_1 = "python"
print(sorted(string_1))

# sort is a list method and modifies the orginial list, works only on lists
# sorted in global built-in function works on any iterable


