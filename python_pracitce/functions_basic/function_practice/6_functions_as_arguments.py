# "Functions" as first-class objects Becoming Powerful

# Example 1
def greet():
    print("Hello")

def execute(func):
    func()

execute(greet)                  # not greet()

# Example 2 Calculator
def add(a,b):
    return a + b

def multiply(a,b):
    return a*b

def calculate(operation, a,b):
    return operation(a,b)

print(calculate(add,23,45))
print(calculate(multiply,12,12))

# Callbacks
def process(callback):
    print("Processsing")
    callback()

def done():
    print("Finished")

process(done)

# Example 1
def square(x):
    return x*x

def cube(x):
    return x*x*x

def apply(func,value):
    return func(value)

print(apply(square,8))
print(apply(cube,3))

# Example 2
def uppercase(text):
    return text.upper()

def lowercase(text):
    return text.lower()

def transform(func, text):
    return func(text)

print(transform(uppercase,"Stanley"))
print(transform(lowercase, "KERKETTA"))
