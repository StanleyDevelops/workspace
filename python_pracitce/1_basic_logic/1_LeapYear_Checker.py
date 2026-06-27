# Basic program to check if year is leap or not
try: 
    year = int(input("Enter a year: "))
    if year <= 0:
        print("Please Enter a positive value")
    elif (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
        print("It's a leap year!")
    else:
        print("Not a leap")
except ValueError:
    print("Enter a correct year!")