# Property Decorator in Python


class Rectangle:
    def __init__(self, height, width):
        self._height = height
        self._width = width

    
    @property
    def width(self):
        return f"Width of the rectangle is {self._width:.1f}cm"

    @property
    def height(self):
        return f"Height of the rectangle is {self._height:.1f}cm"
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than 0!")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than 0!")

    @width.deleter
    def width(self):
        del self._width
        print("Width attribute has been deleted!")

    @height.deleter
    def height(self):
        del self._height
        print("height attribute has been deleted!")

rectangle = Rectangle(3,4)

print(rectangle.width)
print(rectangle.height)

rectangle.width = 5
rectangle.height = 6

print(rectangle.width)
print(rectangle.height)

del rectangle.width
del rectangle.height