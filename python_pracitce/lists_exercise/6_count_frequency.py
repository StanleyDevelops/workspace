# Count frequency of one element

list_1 = [1,1,2,3,3,4,4,4,5]
find_frequency = int(input("Enter a number to find frequency: "))

count = 0
for num in list_1:
        if num == find_frequency:
            count += 1

print(f"The count of {find_frequency}, {count}")

    
# The dictionary Way
list_1 = [1,1,2,3,3,4,4,4,5]
dictionary_1 = {}

for num in list_1:
      dictionary_1[num] = dictionary_1.get(num, 0) + 1

print(f"The Frequencies: {dictionary_1}")
