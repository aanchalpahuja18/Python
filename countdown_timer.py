import time

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    # Below time.sleep(1) will make our program sleep for 1 sec and then execute from where it left.
    time.sleep(1)

print("Time's Up!")