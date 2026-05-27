# simple program to find count of even and odds

numbers = [-1,0,3,-2,5]
odd_count = 0
even_count = 0
zero_count = 0

for num in numbers:
    if num == 0:
        zero_count += 1
    elif num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1 

print(f"The number of odds:  {odd_count}")
print(f"The number of evens: {even_count}")
print(f"The number of zero: {zero_count}")
