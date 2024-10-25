# Polymorphism in Python

from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, width):
        self.width = width

    def area(self):
        return self.width ** 2
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5
    
class Pizza(Circle):
    def __init__(self, radius, toppings):
        super().__init__(radius)
        self.toppings = toppings

shapes = [Circle(3), Square(4), Triangle(6,7), Pizza(3,"oregano")]

for shape in shapes:
    print(f"{shape.area()}cm^2")