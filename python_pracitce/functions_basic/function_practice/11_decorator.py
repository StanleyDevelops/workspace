# A simplle decorator

def decorator(func):

    def wrapper():
        print("starting...")
        func()

    return wrapper

def greet():
    print("Hello")

greet = decorator(greet)
greet()

# Example 
def logger(func):
    def wrapper():
        print("Function Called")
        func()

    return wrapper

@logger
def hello():
    print("Hello!")

hello()

# @app.get("/") and @login_required

# create a decorator that prints: Welcome before running  a function
def my_decorator(func):
    def my_wrapper():
        print("Welcome")
        func()
    
    return my_wrapper

@my_decorator
def greet():
    print("running the application")

greet()

# Creating a decorator that prints "Function finished" after the function executes.
def decorator(func):
    def wrapper():
        func()
        print("Function Finished.")
       

    return wrapper

@decorator
def my_function():
    print("Function Processing")

my_function()

