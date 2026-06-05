# Too High - Too Low - Guess Game
import random

# randint is inclusive, so this correctly picks a number from 1 to 10
number = random.randint(1, 10)
count = 0

print("I'm thinking of a number between 1 and 10.")

while True:
    try:
        guess = int(input("Guess a number: "))
        count += 1  # Increment the attempt immediately when a valid number is entered
        
        if guess < 1 or guess > 10:
            print("Please stay within the range of 1 to 10!")
            continue  # Skips the rest of the loop and asks again
            
        if guess < number:
            print("Too Low!")
        elif guess > number:
            print("Too High!")
        else:
            print("Hooray!! You won.")
            print(f"Total number of attempts: {count}")
            break  # Break out of the infinite loop because they won!
            
    except ValueError:
        print("Invalid input! Enter an actual integer (1-10) man.")



        
