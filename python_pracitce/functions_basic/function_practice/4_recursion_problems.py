# A function that calls itself
# Base Case
# Recursive Case

str = "Stan"
print(str[:-1])

# reversing a string 
def reverse_string (text):  
    char_list = list(text)
    if len(char_list) == 1:    # bug if str = " "
        print(char_list[0])
    else: 
        print(char_list[-1], end = "")
        char_list.pop()
        reverse_string(char_list)

print(reverse_string('POSTGRESQL'))    # None at the end

def reverse_string(text):
    # Base Case: If the string is empty or a single letter, it's already reversed!
    if len(text) <= 1:
        return text
    
    # Recursive Case: Take the last character + reverse the remaining hidden string
    return text[-1] + reverse_string(text[:-1])

reversed_result = reverse_string('POSTGRESQL')
print(reversed_result)

# A countdown function
def countdown(n):
    if n == 1:
        print(n)
    else:
        print(n)
        countdown(n-1)

countdown(5)

# factorial of a number using recursion
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fact(n-1)
    
print(fact(6))

# sum of numbers using recursion
def total(n):
    if n == 1:
        return 1
    else:
        return n+total(n-1)
print(total(5))

# recursive function to calculate power of a number
def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base*power(base,(exponent-1))

print(power(2,8))

# function to calculate digits
def count_digits(n):
    count = len(str(n))
    return count

print(count_digits(1234231))