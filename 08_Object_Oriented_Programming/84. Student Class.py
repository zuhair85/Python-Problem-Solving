# Task: Create a Python class called Student that stores a student's name and grades. Implement methods to add grades and calculate the student's average.

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        total_grade = 0
        count = 0
        for grade in self.grades:
            total_grade += grade
            count += 1
        avg = total_grade / count
        return avg

student1 = Student("Alice")

student1.add_grade(90)
student1.add_grade(85)
student1.add_grade(95)

print(student1.name)
print(student1.grades)
print(student1.calculate_average())