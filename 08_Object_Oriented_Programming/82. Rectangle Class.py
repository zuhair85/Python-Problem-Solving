#Store width and height and provide methods for area and perimeter.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rectangle1 = Rectangle(8, 3)
print(rectangle1.area())
print(rectangle1.perimeter())