# Count frequency of elements in a dictionary

your_dict = {}
for char in 'banana':
    your_dict[char] = your_dict.get(char, 0) + 1

print(your_dict)

# counting frequencies from inside dictionary

user_favorites = {
    "Siddarth": "banana",
    "Amit": "apple",
    "Rahul": "banana",
    "Priya": "mango",
    "Sneha": "apple",
    "Karan": "banana"
}

fruits_frequency = {}
for fruits in user_favorites.values():
    fruits_frequency[fruits] = fruits_frequency.get(fruits, 0) + 1

print(fruits_frequency)