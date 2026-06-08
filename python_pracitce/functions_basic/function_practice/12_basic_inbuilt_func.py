# 1 - convert every item to an integer using map()
str_num = ["1", "2", "3"]
new_list = list(map(lambda s: int(s), str_num))
print(new_list)

# 2 Given a list of names, capitalize each one using map()
my_list = ["Stanley", "Niral", "Kerketta", "Master", "Lee"]
the_list = list(map(lambda x: x.upper(), my_list))
print(the_list)

# Given two lists [1,2,3] and [4,5,6], produce [5,7,9] using map() with two arguments
a = [1,2,3]
b = [4,5,6]
c = list(map(lambda x, y: x+y, a,b))
print(c)

# 1 - Filter out all empty strings from ["hello", "", "world", "", "!"]
list_2 = ["hello", "", "world", "", "!"]
filtered = list(filter(lambda x: x != "",list_2))
print(filtered)

# 2 - From a list of numbers, keep only those greater than 10
list_3 = [12,3,1,4,6,73]
new_lis = list(filter(lambda x: x > 10, list_3))
print(new_lis)

# 3 - From a list of words, keep only words that start with the letter "a"
list_4 = ["apple", "banana", "anaar", "kiwi", "aam"]
new_li = list(filter(lambda x: x.startswith("a"), list_4))
print(new_li)

# 1 - Print each item in a list with its position starting from 1
fruits = ["aaple", "pomegranet", "watermelon"]
for index, value in enumerate(fruits):
    print(f"{index}: {value}")

# 2 - Find the index of the first item that is greater than 10 in a list
nums = [2,0,4,11,8]
for i, val in enumerate(nums):
    if val > 10:
        print(f"{i}: {val}")
        break

# 3 - Build a dict from a list where the key is the index and value is the item
ano_list = [10,20,30,40,50]
my_dic = {}
for index, value in enumerate(ano_list):
    my_dic[index] = value 

print(my_dic)

