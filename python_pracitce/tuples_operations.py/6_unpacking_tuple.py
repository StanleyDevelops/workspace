# Unpacking tuples

tuple_1 = ("stanley", 19, "male")

name, age, gender = tuple_1
print(name)
print(age)
print(gender)

# swapping variables using tuple unpacking 
a = 12
b = 44
print(f"Before: a = {a}, b = {b}")
a, b = b, a
print(f"After: a = {a}, b = {b}")

