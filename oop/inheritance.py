# Inheritance in Python

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating!")
    
    def sleep(self):
        print(f"{self.name} is sleeping!")


class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Mouse(Animal):
    def speak(self):
        print("Squeek!")

dog = Dog("Ricky")
cat = Cat("Minnie")
mouse = Mouse("Jack")

dog.name
dog.is_alive
dog.eat()
dog.sleep()
dog.speak()