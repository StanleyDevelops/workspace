# List operation to find maximum and minimum

list = [1,2,3,4,5]

#for maximum
maximum = list[0]
for num in list[1:]:
    if num > maximum:
        maximum = num

print(maximum)

#for minimum
minimum = list[0]
for num in list[1:]:
    if num < minimum:
        minimum = num

print(minimum)