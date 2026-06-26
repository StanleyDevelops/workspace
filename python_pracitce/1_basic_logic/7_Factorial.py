# Non-recursive factorial
# You should add an exception for negatives too
try:
    number = int(input("Enter a number to find Factorial: "))
    if number < 0:
        print("Factorial doesn't exist for Negatives")
    elif number == 0:
        print(1)
    else:
        fact = 1
        for i in range(1,number+1):
            fact *= i
        print(fact)
except ValueError:
    print("Enter integers man")





