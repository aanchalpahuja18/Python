# 2D Collections: Collections made up of collections

# Numpad made with 2D collections:

num_pad = ((1,2,3), 
           (4,5,6),
           (7,8,9),
           ("*", 0, "-"))

for row in num_pad:
    for num in row:
        print(num, end = " ")
    print()

# Example of 2D lists

fruits =  ["apple", "banana", "mango"]
food = ["pizza", "burger", "noodles"]
groceries = [fruits, food]

for g in groceries:
    for food in g:
        print(food, end = " ")
    print()
