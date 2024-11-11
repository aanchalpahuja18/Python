# Multithreading in Python

import threading
import time


def walk_dog(first, last):
    time.sleep(8)
    print(f"You finished walking {first} {last}")

def clear_thrash():
    time.sleep(2)
    print("You cleared the thrash")

def get_mail():
    time.sleep(4)
    print("You got the mail!")

chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo"))
chore2 = threading.Thread(target=clear_thrash)
chore3 = threading.Thread(target=get_mail)

chore1.start()
chore2.start()
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All the chores have been completed!")