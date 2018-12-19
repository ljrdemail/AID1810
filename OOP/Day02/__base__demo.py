class Human:
    pass


class Student(Human):
    pass


class Teacher(Student):
    pass


print(Teacher.__bases__)
print(Student.__bases__)
print(Human.__bases__)
print(object.__bases__)
