# 1 -  Divide two numbers safely

try:
    num_1 = int(input("Enter a number: "))
    num_2 = int(input("Enter another number: "))
    num_3 = float(num_1/num_2)
    print(f"The Division is: {num_3}")
except ValueError:
    print("Please enter a digit!")
except ZeroDivisionError:
    print("The denominator cannot be Zero!")

# 2 - Take integer input safely

try:
    int = int(input("Enter a digit: "))
    print(f"Chosen number: {int}")
except ValueError:
    print("Please enter an integer! Strings prohibited!")

# 3 - Access list index safely

try:
    list_1 = [12,32,43]
    print(list_1[2])
except IndexError:
    print("Why are you trying to access impossible?")

# 4 - Access dictionary key safely
 
try: 
    fruits = {"apple": 2, "banana": 1}
    print(fruits["apple"])
except KeyError:
    print("The Key doesn't exist.")   

# 5 - Safe calculator 
operation = input("Enter operator (+,-,*,/): ").strip()

operators = ['+','=','*','/']
if operation not in operators:
    print("Please enter correct operator!")
else:
    try:
        num_1 = int(input("Enter a number: "))
        num_2 = int(input("Enter another number"))

        if operation == "+":
            print(f"The sum: {num_1 + num_2}")
        elif operation == "-":
            print(f"The difference: {num_1 - num_2}")
        elif operation == "*":
            print(f"The product: {num_1 * num_2}")
        elif operation == "/":
            print(f"The division: {num_1 / num_2}")
        
    except ValueError:
        print("Please enter a digit")
    except ZeroDivisionError:
        print("Divison by Zero is prohibited!")


    
    






    
        



