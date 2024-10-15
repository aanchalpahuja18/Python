# Default Arguments of a Function

def net_price(list_price, discount = 0, tax = 0.05):
    return list_price * (1 - discount ) * (1 + tax)

print(net_price(500, 0.1))


import time 

def count(start, end = 10):
    for i in range(start, end + 1):
        print(i)
        time.sleep(1)
    print("Done!")

count(7)