# -	 Decorator used to define a method as a property (it can be accessed like an attribute)
# -	Benefit: Add additional logic when read, write, or delete attributes
# -	Give you getter, setter, and deleter method
# Pass
class Rectangle:
    def __init__(self, width, height):
        self._width = width         #that '_' makes the width private (self._width)
        self._height = height       #that '_' makes the height private

    #getter method basically
    @property
    def width(self):
        return f"{self._width:.1f}cm"

    #getter method basically
    @property
    def height(self):
        return f"{self._height:.1f}cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")

    @width.deleter
    def width(self):
        del self._width
        print('Width has been deleted')

    @height.deleter
    def height(self):
        del self._height
        print('Height has been deleted')

rectangle = Rectangle(3, 4)

print(rectangle._width)     #We could still access them directly without the getter methods but that defeats the purpose of making them private

rectangle.width = 5
rectangle.height = 6

print(rectangle.width)
print(rectangle.height)

del rectangle.width
del rectangle.height
