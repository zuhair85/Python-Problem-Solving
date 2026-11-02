# Instance methods = Best for operations on instances of the class (objects)
# -	For instance method, you access an object, then call the instance method
# -	E.g: employee1.get_info()
# Static methods = Best for utility functions that do not need access to class data
# -	For static method, you only need to access the class to call the static method
# -	E.g: Employee.is_valid_position(“Cook”)

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions

employee1 = Employee("Eugene", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")

print(Employee.is_valid_position('Cook'))
print(Employee.is_valid_position('Rocket Scientist'))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
