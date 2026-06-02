def greet():
    print("Hello")

say_hello = greet  #assigning variables to a function
say_hello()  

# Functions inside lists
def add_one(x):
    return x + 1

def add_two(x):
    return x + 2

operation = [add_one, add_two]

print(operation[0](5))
print(operation[1](-3))

# Function inside dictionaries

def multiply(a,b):
    return a*b

calculator = {"add": add_two,
              "multiply": multiply}

print(calculator["multiply"](13,45))

# looping through the list and execute function
def morning():
    print("Good Morning")

def evening():
    print("Good Evening")

the_list = [morning, evening]

for i in the_list:
    (i())