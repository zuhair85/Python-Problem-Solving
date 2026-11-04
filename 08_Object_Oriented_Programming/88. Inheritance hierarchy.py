# Task: Create a base Animal class and subclasses that override a sound-making method.

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        raise NotImplementedError

class Dog(Animal):
    def make_sound(self):
        return ('Woof')

class Cat(Animal):
    def make_sound(self):
        return ('Meow')

class Cow(Animal):
    def make_sound(self):
        return ("Moo")

dog = Dog("Scooby")
cat = Cat("Whiskers")
cow = Cow("Daisy")

animals = [dog, cat, cow]

for animal in animals:
    print(f"{animal.name} says: {animal.make_sound()}")