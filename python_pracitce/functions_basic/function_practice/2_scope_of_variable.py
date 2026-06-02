# Trying to access a variable outside the function

def show():
    city = "New Delhi"
    print(city)

# using global keyword to increment inside function

counter = 0
def increment():
    global counter
    counter += 1
    return counter 

print(counter)
print(increment())    # value persists
print(increment())
print(counter)

# global and local scope
name = "global"
def write():
    global name
    print(name)

write()
print(name)