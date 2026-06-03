# Map - applies a function to every item in an iterable

# squaring items in a list
numbers = [1,2,3,4]
result = map(lambda x:x*2, numbers)
print(list(result))

# Filter - keeps only items that satisfy a condition

numbers = [12,24,5,65,23]
result = filter(lambda x: x%2 == 0, numbers)
print(list(result))

# Sort - important for real projects

# sorting strings by length

names = ["Stanley", "do", "love", "programming"]
result = sorted(names, key = lambda name: len(name))
print(result)


