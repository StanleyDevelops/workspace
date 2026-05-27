# List Operation to reverse a list

# One way
list_1  = [11,22,33,44,55] 
list_2 = []

# -4 for start value, -1 for stopping at last, -1 for step back
for i in range(len(list_1) - 1, -1, -1):
    list_2.append(list_1[i])

print(list_2)

# Another way
list_3 = [55,44,33,22,11]
list_4  = list_3[::-1]
print(list_4)

# python reversed method
list_3 = [55,44,33,22,11]
list_4 = []
for num in reversed(list_3):
    list_4.append(num)

print(list_4)
