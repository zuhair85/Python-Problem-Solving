# Create a Person class with name, age, and a method that introduces the person.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(f'Hi, I am {self.name}. I am {self.age} years old.')

person1 = Person('Zuhair', 25)
person1.intro()