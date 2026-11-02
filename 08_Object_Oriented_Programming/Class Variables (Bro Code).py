class Student:

    studentNumber = 0   #class variable
    class_year = 2025

    def __init__(self, name, age):
        self.name = name    #instance variable
        self.age = age      #instance variable
        Student.studentNumber += 1

student1 = Student('Spongebob', 25)
student2 = Student('Patrick', 30)
print(student1.name)
print(student1.age)
print(student2.name)
print(student2.age)
print(student1.studentNumber)
print(student2.studentNumber)
print(Student.studentNumber)

print(f'My graduating class of {Student.class_year} has {Student.studentNumber} students')
