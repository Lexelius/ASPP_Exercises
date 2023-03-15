"""
Usage:
    from classroom_day3 import Person
    print(Person('Rebecka', 'Lexelius').get_full_name())

    from classroom_day3 import Student
    me = Student('Rebecka', 'Lexelius', 'physics')
    me.print_name_subject()

    from classroom_day3 import Teacher
    you = Teacher('Filipe', 'Maia', 'Advanced scientific python programming')
    you.print_name_course()
"""

class Person:
    """
    a. Create a "Person" class which takes firstname and lastname as arguments to
    the constructor (___init___) and define a method that returns the full name
    of the person as a combined string.
    """
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_full_name(self):
        return str(self.firstname + ' ' + self.lastname)


class Student(Person):
    """
    b. Create a "Student" class which inherits from the "Person" class, takes the
    subject area as an additional argument to the constructor and define a method
    that prints the full name and the subject area of the student.
    """
    def __init__(self, firstname, lastname, subject_area):
        super(Student, self).__init__(firstname, lastname)
        self.subject_area = subject_area

    def print_name_subject(self):
        print(self.get_full_name() + ', ' + self.subject_area)


class Teacher(Person):
    """
    d. Create a "Teacher" class which also inherits from "Person", takes the name
    of the course (e.g. Python programming) as an argument and define a method
    that prints the full name of the teacher and the course he teaches.
    """
    def __init__(self, firstname, lastname, course):
        super(Teacher, self).__init__(firstname, lastname)
        self.course = course

    def print_name_course(self):
        print(self.get_full_name() + ', ' + self.course)