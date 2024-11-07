# Exception handling in python

try:
    num = int(input("Enter a number: "))
    print(1 / num)
except ValueError:
    print("Enter only numbers please!")
except ZeroDivisionError:
    print("You can't divide by ZERO IDIOT!")
except Exception:
    print("Something went wrong!")
finally:
    print("Do some clean up code here!")

