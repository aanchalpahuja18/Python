
import random

def spin_row():
      slots = ['🥭', '🍉', '🍎', '🔔', '⭐']

      return [random.choice(slots) for _ in range(3)]

def print_row(row):
    print("*********************************")
    print(" | ".join(row))
    print("*********************************")


def give_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🥭':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍎':
            return bet*5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    else:
        return 0


def main():
    balance = 100
    print("*********************************")
    print("Welcome to Python Slot Game!")
    print("Symbols: 🥭 🍉 🍎 🔔 ⭐")
    print("*********************************")

    while balance > 0:

        print(f"Current balance: {balance}")
        bet = input("Enter your amount of bet: ")

        if not bet.isdigit():
            print("Enter a valid amount!")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient Funds!")
            continue
        elif bet <= 0:
            print("Your bet cannot be less than 0!")
            continue

        balance -= bet
        row = spin_row() 
        print("Spinning...")
        print_row(row)

        payout = give_payout(row, bet)

        if payout > 0:
            print(f"You won a payout of Rs. {payout}")
        else:
            print("Sorry you lost this round! ")
        balance += payout


        play_again = input("Do you wanna play again? (Y/N): ").upper()

        if play_again != 'Y':
            break

    print("*********************************")
    print(f"Game Over! Your final balance is: {balance}")
    print("*********************************")


if __name__ == '__main__':
    main()