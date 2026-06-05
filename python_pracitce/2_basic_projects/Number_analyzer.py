# Program to find min, max, average and count of odd/even/zero's

numbers = []

while True:
    try:
        num = int(input("Enter your number: "))
        numbers.append(num)

        more = input("Add more number? (yes/no): ").lower()
        if more != "yes":
            break
    except ValueError:
        print("Please enter a valid number!")

if len(numbers) == 0:
    print("No numbers entered!")
    exit()

max_val = max(numbers)
min_val = min(numbers)

print("Maximum:", max_val)
print("Minimum:", min_val)

total = 0
for num in numbers:
    total += num

average = total / len(numbers)
print("Average:", average)


#logic to count no of odds,evens and zeroes
count_even = 0
count_odd = 0
count_zero = 0

for num in numbers:
    if num == 0:
        count_zero += 1
    elif num % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print("Even:", count_even)
print("Odd:", count_odd)
print("Zero:", count_zero)