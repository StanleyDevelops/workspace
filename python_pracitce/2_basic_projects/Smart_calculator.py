# A Smart calculator that can take numbers continuously and perform Operations Accordingly 

# Function to Take numbers as input 
def getnumbers():
    numbers = []

    while True:
        try:
            add_number = float(input("Enter a number to add: "))
            numbers.append(add_number)

            choice = input("Want to continue add number (yes/no): ").lower()
            if choice != 'yes':
                break
            
        except ValueError:
            print("Please Enter a valid number!")

    return numbers
    
# Function to calculate through numbers and Operator
def calculate(numbers, operator):

    if operator == '+':
        result = sum(numbers)

    elif operator == '-':
        result = numbers[0]
        for num in numbers[1:]:
            result -= num

    elif operator == '*':
        result = 1
        for num in numbers:
            result *= num

    elif operator == '/':
        result = numbers[0]
        for num in numbers[1:]:
            if num == 0:
                print("Error: Division by Zero")
                break
            else:
                  result /=num
          
    else:
        return "Value error! Enter Valid Operator"

    return result

# Main Program
while True:
        operator = input("Enter an Operator(+,-,*,/): ")
        numbers = getnumbers()
        
        if len(numbers) < 2:
            print("Please enter at least two numbers")
            continue

        result = calculate(numbers,operator)
 
        print("The Result is: ", result)

        again = input("Do you want to continue Calculator(yes/no): ").lower()
        if again != 'yes':
            print("Exiting The Calculator")
            break