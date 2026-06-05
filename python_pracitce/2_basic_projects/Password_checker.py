password = input("Enter your Password: ")
has_length = len(password) >=8
has_digit = False
has_lowercase = False
has_uppercase = False

for char in password:   # Don't get confused on classic for loop expression
    if char.isdigit():     #checks if item is digit for every iteration
        has_digit = True
    elif char.islower():
        has_lowercase = True
    elif char.isupper():         # checks all the 3 cases for each item. 
        has_uppercase = True
    
score = 0
if has_length:
    score += 1
if has_digit:
    score += 1
if has_lowercase:
    score +=1
if has_uppercase:
    score += 1

if score <= 2:
    print("Weak Password")
elif score == 3:
    print("Medium Password")
else: 
    print("Strong Password Man!")



