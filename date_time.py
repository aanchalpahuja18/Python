#Date time in python

import datetime

# Working with dates
date = datetime.date(2024, 11, 11)
today = datetime.date.today()
print(date)
print(today)

# Working with time

time = datetime.time(1,15,20)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %d-%m-%Y")
print(time)
print(now)

# Exercise to check if our current datetime has passed our target datetime

target_datetime = datetime.datetime(2025,1,2, 2,20,0)

current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed!")
else:
    print("Target date has NOT passed")
