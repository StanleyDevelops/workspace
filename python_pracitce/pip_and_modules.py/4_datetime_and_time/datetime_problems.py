# Calculate Days Until Birthday
from datetime import datetime

now = datetime.now()
my_next_birthday = datetime(2027,1,24)
result = (my_next_birthday - now)
print(result)

# calculating age
def age_calculator():
    try: 
        year = int(input("Enter Year: "))
        month = int(input("Enter month: "))
        day = int(input("Enter day: "))

        the_birth = datetime(year,month,day)
        now = datetime.now()
        age = now.year - the_birth.year

        has_birthday_passed = (now.month,now.day) < (the_birth.month, the_birth.day)
        if has_birthday_passed:
            age -= 1

        return age
    except ValueError:
        print("Please Enter Correct Input!")

print(f"Your Exact Age is: {age_calculator()} years")