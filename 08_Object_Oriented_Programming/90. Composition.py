# In this problem, you'll practice composition, an important object-oriented programming concept.
# 1. Problem description
# Create two classes:
# - Engine: Represents a car's engine.
# - Car: Represents a car that contains an Engine object.
# A car has an engine. Rather than putting all engine-related functionality directly inside the Car class, we'll create a separate Engine class and make it part of the Car object.

class Engine:
    def __init__(self, horsepower, fuel_type):
        self.horsepower = horsepower
        self.fuel_type = fuel_type

    def start_engine(self):
        print('Engine started!')

    def stop_engine(self):
        print('Engine stopped!')

class Car:
    def __init__(self, make, model, hp, ft):
        self.make = make
        self.model = model
        self.engine = Engine(horsepower = hp, fuel_type=ft)

    def start_car(self):
        self.engine.start_engine()
        print(f'{self.make} {self.model} started!')

    def stop_car(self):
        self.engine.stop_engine()
        print(f'{self.make} {self.model} stopped!')

car1 = Car("Toyota", "Camry", 203, "Gasoline")
car2 = Car("Tesla", "Model 3", 283, "Electric")

car1.start_car()
car2.start_car()

car1.stop_car()
car2.stop_car()
