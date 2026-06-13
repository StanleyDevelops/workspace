import random
import math

# randint
print(random.randint(1,10))

# choice
list_1 = ["stanley", "niral", "kerketta", "Lee", "commander"]
print(random.choice(list_1))

# shuffle
card = ["ace", "spades", "diamond", "queen"]
result = random.shuffle(card)
print(result)
print(card)

# generates a number between 0.0 and 0.1
if random.random() > 0.30:
    print("Lucky event triggered!")
else:
    print("Probability is less than 30%")

value = 1 + random.random() * 9
print(value) 

# Coin toss
import random
def coin_toss():
    outcomes = ["head", "tail"]
    result = random.choice(outcomes)

    return result

# random dice roll
def dice_roll():
    the_number  = random.randint(1,6)

    return the_number

print(dice_roll())

# Circle Area Calculator
def area_cal(radius):
    result = math.pi*radius*radius

    return result

print(area_cal(5))
