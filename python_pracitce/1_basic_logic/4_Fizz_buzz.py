# Frizz-Buzz progam to check numbers divisible by 3, 5 and both

for num in range(1,51):    # Actually nailed in first attempt
    if num % 3 == 0 and num % 5 == 0:
        print("Frizz-Buzz", num)
    elif num % 3 == 0:
        print("Frizz", num)
    elif num % 5 == 0:
        print("Buzz", num)
    
       
