# Finding sum of digits of a number

num = int(input("Enter a number: "))
result = 0 
while (num != 0):
    result += num%10
    num = num//10   # here we need to use floor not simple division

print(result)

# Also Reversing the number


