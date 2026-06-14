from datetime import datetime, timedelta
from time import sleep

now = datetime.now()
print(now)

print(now.strftime("%Y-%m-%d"))

# playing with my birthday
my_birthday = datetime(2007,1,24)
print(my_birthday.strftime("%B"))
print(my_birthday.strftime("%A-%M-%S"))
print(my_birthday.strftime("%d/%m/%Y"))

# Calculating 37 days from now
last_python_day = (now + timedelta(days = 37))
print(last_python_day)

# diffrence in minutes from now to 12
print(now + timedelta(minutes = 200))  # time after 200 minutes

# making a countdown
print("Completing in 3 Sec..")
sleep(1)
print("3")
sleep(1)
print("2")
sleep(1)
print("1")
sleep(1)
print("Done!!") 
