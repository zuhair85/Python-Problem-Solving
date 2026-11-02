# -	Another way to achieve polymorphism besides inheritance
# -	Objects can be treated as if they are different type as long as they meet the necessary attributes/methods required of them
# -	It follows this adage: “If it looks like a duck, and quacks like a duck, it must be a duck”
# Key idea: As long as an object resembles another, it could be treated as that type
class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print('WOOF!')

class Cat(Animal):
    def speak(self):
        print('MEOW!')

class Car:
    alive = True

    def speak(self):
        print('HONK!')

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)
