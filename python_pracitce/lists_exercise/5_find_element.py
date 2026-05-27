# Program to find an element in list

list_1 = [11,22,33,44,55]
number = int(input("Enter a number to find: "))
found = False
for num in list_1:
    if num == number:
        print(f"Yes {num} is in the list")
        found = True
        break

if not found:
    print(f"The number {number} doesn't exist in list.")
    
