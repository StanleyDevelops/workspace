# It simply tells the type of data parameter is 
# we can also specify what function returns
# but do not enforce type too 

def add(a: int, b: int) -> float:
    return a + b

print(add("Hello ", "World"))
print(add(12,12))

# type hints to print full name
def full_name(first: str, last: str) -> str:
    return first + last

print(full_name("Stanley ", "Kerketta"))

# return average 
def average(numbers: list[int]) -> float:
    sum = 0
    for i in numbers:
        sum += i

    avg = sum/len(numbers)
    return avg

print(average([12,23,14]))






