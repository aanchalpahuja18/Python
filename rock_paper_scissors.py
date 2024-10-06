import random

options = ("rock", "paper", "scissors")
is_playing = True

while is_playing: 

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissor): ")

    print(f"Player {player}")
    print(f"Computer {computer}")

    if player == computer:
        print("Its a tie")
    elif player == "rock" and computer == "scissors":
        print("You win")
    elif player == "paper" and computer == "rock":
        print("You win")
    elif player == "scissors" and computer == "paper":
        print("You win")
    else:
        print("You loose!")

    play_again = input("Play Again ? (y/n): ").lower()

    if not play_again == 'y':
        is_playing = False  

print("Thanks for playing")