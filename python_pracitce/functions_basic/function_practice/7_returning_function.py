# Returning different Functions

def operations(choice):
    def add():
        print("Addition")

    def multiply():
        print("Multiply")

    if choice == "add":
        return add 
    
    return multiply

func = operations("add")
func()

# Example 1 
def get_hello():
    def hello():
        print("Hi, How are you?")

    return hello

greet = get_hello()
greet()

# Example 2

def choose(operations):
    def add():
        print("Adding..")

    def subtract():
        print("Subtracting")

    if operations == 'add':
        return add
    
    return subtract

math = choose('subtract')
math()