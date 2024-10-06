# Nested loops in Python: Any loop can be inside any other loop. No restriction in the type of the loop is required!


for i in range(3):
    for j in range(1,10):
        print(j ,end = "")
    print()

# Print a rectangle using nested loops: 

rows = int(input("Enter the no of rows: "))
cols = int(input("Enter the no of cols: "))
symbol = input("Enter the symbol which you want to insert: ")

for x in range(rows):
    for y in range(cols):
        print(symbol, end = " ")
    print()