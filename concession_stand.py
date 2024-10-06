# Concession Stand Program

menu = {"pizza": 120,
        "popcorn": 150,
        "coke": 90,
        "burger": 180,
        "fries":200,
        "samosa": 40,
        "chips": 20,
        "nachos": 90}

cart = []
total = 0


print("--------MENU----------")
for key,value in menu.items():
    print(f"{key:10} {value:.2f}")
print("----------------------")

while True:
    food = input('Enter your food (q to quit): ')
    if food.lower() == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("-----------YOUR ORDER---------------")

for food in cart:
    total += menu.get(food)
    print(food, end = " ")

print()
print(f"Total is: {total:.2f}")