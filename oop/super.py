# super() in python


class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {"Filled" if self.is_filled else "Not Filled"}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f"Area of the circle is: {3.14 * self.radius * self.radius}cm^2")


class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        super().describe()
        print(f"Area of the square is: {self.width * self.width}cm^2")


class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        super().describe()
        print(f"Area of the triangle is: {self.width * self.height / 2}cm^2")

circle = Circle("blue", True, 5)
square = Square("red", False, 6)
triangle = Triangle("pink", True, 3, 5)

circle.describe()
square.describe()
triangle.describe()