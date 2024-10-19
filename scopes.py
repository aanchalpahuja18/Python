# variable scope

# Local Scope
def func1():
    x = 1
    print(x)

def func2():
    y = 2
    print(y)

func1()
func2()

# Scope Resolution in Python: Python checks for Local -> Enclosed -> Global -> Built-in
# Enclosed Scope

def func3():
    x = 10
    def func4():
        print(x)
    func4()

func3()


# Global scope

def my_func():
    print(x)

def my_func2():
    print(x)

x = 24

my_func()
my_func2()

# Built-in scope:

from math import e

def printe():
    print(e)

e = 55

printe()

# If we have built-in & global variables with the same variable name then according to the scope resolution order the global variables will be given priority over built-in variables.