def palind(num):
    n = num
    result = 0
    while num> 0:
        result = (result*10) + num%10
        num = num //10

    if result == n:
        return "Palindrome"
    else:
        return "Nope"
    
print(palind(98189))
