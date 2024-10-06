import random

low = 1 
high = 100

# Below is used to choose a random integer from the given range
number = random.randint(low, high)
print(number)

# Below is used to choose a random float from the given range
number2 = random.random()
print(number2)


# Below is used to give random choice from the tuples
options = ("rock", "paper", "scissors")
option = random.choice(options)
print(option)


# Below is used to give random choice from the list
cards = ["2", "3","4","5","6","7","8","9","J","K","Q","A"]
random.shuffle(cards)
print(cards)

