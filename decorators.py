# Decorators in Python

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("You added sprinkles")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You added fudge 🍫")
        func(*args, **kwargs)
    return wrapper


@add_fudge
@add_sprinkles
def get_icecream(flavor):
    print(f"Here is your {flavor} icecream")

get_icecream("chocolate")