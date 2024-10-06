# Python number guessing game
import random 

lowest_num = 1
highest_num = 100

answer = random.randint(lowest_num, highest_num)

guesses = 0
is_running = True

while is_running:
    guess = input(f"Enter a number within the range of {lowest_num} and {highest_num}: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        
        if guess < lowest_num or guess > highest_num:
            print("That number is out of range! ")
            print(f"Please enter a number within the range of {lowest_num} and {highest_num}: ")
        elif guess < answer:
            print("Number is toooo low!")
        elif guess > answer:
            print("Number is toooo high!")
        else:
            print(f"Correct! Answer is {answer}")
            print(f"The number of guesses you took: {guesses}")
            is_running = False


    else:
        print("That is not a number")
        print(f"Please enter a number within the range of {lowest_num} and {highest_num}: ")