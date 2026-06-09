# 1 - Safe age input
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Please enter correct input!")
else:
    print(age)
finally: 
    print("I'll gte excecuted nevertheless")

# 2 - Division calculator
try:
    num_1 = int(input("Enter first number: "))
    num_2 = int(input("Enter second number: "))
    print(float(num_1/num_2))
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Please enter an integer")



