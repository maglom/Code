from math import pi

class Shape:
    def __init__(self):
        pass

    def areal(self):
        return -1

    def perimeter(self):
        return -1

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def areal(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def areal(self):
        return self.width * self.height

    def perimeter(self):
        return self.width * 2 + self.height * 2

class Square(Rectangle):
    def __init__(self, side):
        self.height = side
        self.width = side

