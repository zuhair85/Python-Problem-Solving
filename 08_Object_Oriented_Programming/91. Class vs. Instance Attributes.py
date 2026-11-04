# Create a class that tracks how many objects have been created and stores information that is either shared across all objects or unique to each object.
#
# Your program should demonstrate the difference between class attributes and instance attributes.

class Student:
    total_students = 0
    university = "University of Michigan-Dearborn"
    def __init__(self, name, student_ID):
        self.name = name
        self.student_ID = student_ID
        Student.total_students += 1

student1 = Student("Alice", 101)
student2 = Student("Bob", 102)
student3 = Student("Charlie", 103)

print(student1.name)
print(student2.name)

print(Student.total_students)
print(student1.total_students)

print(student1.university)
print(student2.university)