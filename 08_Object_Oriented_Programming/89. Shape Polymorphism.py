# Task: Create Circle, Rectangle, and Triangle classes with a common area interface.
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return self.base * self.height * 0.5

circle = Circle(5)
rectangle = Rectangle(10, 4)
triangle = Triangle(8, 6)
# shape = Shape()
shapes = [circle, rectangle, triangle]

for shape in shapes:
    print(f"Area: {shape.calculate_area():.2f}")
