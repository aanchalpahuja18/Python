

def show_balance(balance):
    print("**************************************")
    print(f"Your account balance is: Rs. {balance:.2f}")
    print("**************************************")

def deposit():
    amount = float(input("Enter the amount you want to deposit! "))

    if amount < 0:
        print("**************************************")
        print("This is an invalid amount!")
        print("**************************************")
        return 0
    else:
        return amount


def withdraw(balance):
    amount = float(input("Enter the amount you want to deposit! "))

    if amount > balance:
        print("**************************************")
        print("Insufficient Funds! ")
        print("**************************************")
        return 0
    elif amount < 0:
        print("**************************************")
        print("Invalid amount to be withdrawn! ")
        print("**************************************")
        return 0
    else:
        return amount


balance = 0
is_running = True

while is_running:
    print("**************************************")
    print("Banking Program!")
    print("**************************************")
    print("Enter the following for various tasks!")
    print("1. Show balance!")
    print("2. Deposit Amount!")
    print("3. Withdraw Amount!")
    print("4. Exit")

    choice = int(input("Enter your choice between (1-4): "))

    if choice == 1:
        show_balance(balance)
    elif choice == 2:
        balance += deposit()
    elif choice == 3:
        balance -= withdraw(balance)
    else:
        is_running = False

print("**************************************")
print("Thankyou for visiting!")
print("**************************************")

