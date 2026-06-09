# 1 - validate age
age = -8
try:
    if age < 0:
        raise ValueError("The Age cannot be negative!")
except ValueError as e:
    print(f"OOPs: {e}")

# 2 - Validate password length
class LengthError(Exception):
    pass

def Enter_pass(password):
    if len(password) < 5:
        raise LengthError("The Password must be greater than 5 charracter")
    
    return password

try:
    print(Enter_pass("Love"))
except LengthError as e:
    print(f"{e}")

# 3 - Validate bank withdrawal amount
class Amount_Error(Exception):
    pass

def withdraw(amount):
    if amount >= 100:
        raise Amount_Error("The limit is 1000!")
    return amount

try:
    print(withdraw(9000))
except Amount_Error as e:
    print(f"{e}")

# 4 - Create two custom exceptions — EmptyNameError and TooLongNameError — 
# and write a validate_name(name) function that raises the right one depending on the problem
class EmptyNameError(Exception):
    pass
class TooLongNameError(Exception):
    pass

def validate_name(name):
    if len(name) > 10:
        raise TooLongNameError("The name cannot exceed 10 Characters!")
    
    elif not name:
        raise EmptyNameError("The name cannot be empty!")
    
    return name

try:
    print(f"{ validate_name("Ilikeprogramming213")}")
except EmptyNameError as e:
    print(f"{e}")
except TooLongNameError as f:
    print(f"{f}")