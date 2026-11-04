# Task: Create an Employee class with salary calculations and specialized subclasses for different payment arrangements.
#
# This problem introduces two important OOP concepts: inheritance and method overriding.
#
# You'll create a parent class called Employee, then create specialized employee classes that inherit from it but calculate their pay differently.

class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def calculate_salary(self):
        raise NotImplementedError

    def display_info(self):
        print(f'Name: {self.name}')
        print(f'Employee ID: {self.employee_id}')
        print(f'Salary: ${self.calculate_salary():.2f}')
        print('')

class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, monthy_salary):
        super().__init__(name, employee_id)
        self.monthly_salary = monthy_salary

    def calculate_salary(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

class ContractEmployee(Employee):
    def __init__(self, name, employee_id, contract_amount, months_worked):
        super().__init__(name,employee_id)
        self.contract_amount = contract_amount
        self.months_worked = months_worked

    def calculate_salary(self):
        return self.contract_amount * self.months_worked

employee1 = FullTimeEmployee("Alice", 101, 5000)
employee2 = PartTimeEmployee("Bob", 102, 20, 80)
employee3 = ContractEmployee("Charlie", 103, 3000, 4)

employees = [employee1, employee2, employee3]

for employee in employees:
    employee.display_info()