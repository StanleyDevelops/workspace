# An anonymous function

# a lmbda that squares a number

square = lambda x: x*x
print(square(2))

# example with functions as argument

def apply(func, value):
    return func(value)

result = apply(lambda x: x*10, 10)

print(result)

# labmda that converts strings to uppercase

str_convert = lambda x: x.upper()
print(str_convert("stanley"))

# sort and lambda

players = [("Virat", 18), ("Rohit", 45), ("Dhoni", 7)]
players.sort(key = lambda player: player[1])
print(players)