# Concatenating two tuples

tuple_1 = (1,2,3,4)
tuple_2 = (5,6,7,8)

list_1 = list(tuple_1)
list_2 = list(tuple_2)
list_1.extend(list_2)
print(list_1)
