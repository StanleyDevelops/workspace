# *args Arbitrary argument collects positonal arguments into one tuple

# Summing any number of number
def addition(*args):
    sum = 0
    for num in args:
        sum += num

    return sum

print(addition(12,2,4,32))

# Unpacking *args 
def add(*args):
    print(args)

numbers = [1,2,3]
add(*numbers)   # returns a tuple

# Using *args to find average
def avg(*args):
    sum = 0
    for i in args:
        sum += i

    avg = sum/(len(args))
    return avg 

print(avg(12,16,18))

# **kwargs Keyword arguments collects extra keywords arguments into a dictionary

# looping through the **kwargs
def show(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

show(Name= "Stanley", branch = "CSE", age = 19)

# Unpacking Dictionary
data = {"name": "Stanley", 
        "hobby": ("gaming", "coding", "vibing"),
        "girlfriend": None,
        "grades": {"maths": "O",
                   "english": "D",
                   "cs": "A"},
        "love": ["Java", "C++", "Python"]}

def show(**kwargs):
    print(kwargs)

print(data["love"][0])
print(data["hobby"][2])
show(**data)
print(data["hobby"][0])






