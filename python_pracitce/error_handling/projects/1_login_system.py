# Login System With Retry Limits

class AccountLockedError(Exception):
    pass

# correct username and password
correct_user = "ABCD"
correct_pass = "1234" 

attempt = 0
max_attempt = 3

# run a loop

while attempt < max_attempt:
    print(f"------------------Attempt: {attempt + 1}---------------")
    input_user = input("Enter Username: ")
    input_pass = input("Enter Password: ")

    if input_user == correct_user and input_pass == correct_pass:
        print(f"Welcome!!")
        break
    else: 
        print(f"Worng Password/Username")
        attempt += 1

if attempt == max_attempt:
        raise AccountLockedError("The Account is Locked!")
    








        





    
