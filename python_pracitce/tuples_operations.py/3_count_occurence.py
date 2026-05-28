# operation to count occurence of an element

tuple_1 = (1,2,2,3,2)

count = 0
for num in tuple_1:
    if num == 2:
        count += 1
    
print(count)