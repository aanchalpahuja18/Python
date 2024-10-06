# Shopping Cart Program

foods = []
prices = []
total = 0


while True:
    food = input("Enter the food you would like to have! (q to quit): ")
    if food.lower() == 'q':
        break
    else:
        price = int(input(f"Enter the price of the {food} Rs: "))
        foods.append(food)
        prices.append(price)


print("------YOUR CART------")
for food in foods:
    print(food, end = " ")

for price in prices:
    total += price

print()
print(f"Your total amount is: {total}")    