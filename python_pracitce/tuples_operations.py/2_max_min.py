# simple operation to find maximum and minimum

tuple_1 = (12,25,7,3,44)
maximum = tuple_1[0]
for num in tuple_1:
    if num > maximum:
        maximum = num

smallest = tuple_1[0]
for num in tuple_1:
    if num < smallest:
        smallest = num

print(f"The Largest element: {maximum}\nThe Smallest elemnt: {smallest}")