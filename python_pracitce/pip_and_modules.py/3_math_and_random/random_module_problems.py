# 1 - Simulate rolling two dice and print the sum. Run it a few times to see different results.
import random

def sum_dice():
    num_1 = random.randint(1,6)
    num_2 = random.randint(1,6)

    return f"The first dice {num_1} and second dice {num_2} sum is: {num_1 + num_2}"

print(sum_dice())

# 2 -Use random.random() to simulate a coin flip — 
# print "Heads" if the value is above 0.5, "Tails" if below.
def coin_toss():
    value = random.random()
    print({value})
    if value > 0.5:
        return "Head"
    else:
        return "Tail"

print(coin_toss())



