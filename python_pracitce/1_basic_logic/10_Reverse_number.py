# Program to reverse a number mathematically

try:
    num = int(input("Enter a number to reverse: "))
    
    # Store the original sign (positive or negative)
    sign = -1 if num < 0 else 1
    num = abs(num) # Work with the positive version of the number
    
    reversed_num = 0
    while num != 0:
        last_digit = num % 10
        reversed_num = (reversed_num * 10) + last_digit
        num = num // 10  # Floor division to drop the last digit
        
    # Restore the sign to the reversed number
    final_result = reversed_num * sign
    print("Reversed number:", final_result)

except ValueError:
    print("Please enter a valid integer!")




# Reverse a number using Python string slicing
num_str = input("Enter a number to reverse: ")

if num_str.startswith('-'):
    # Reverse everything after the minus sign, then re-attach it
    reversed_str = '-' + num_str[1:][::-1]
else:
    reversed_str = num_str[::-1]

print("Reversed number:", int(reversed_str))
