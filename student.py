from module import *
from moduleElement import *


class Student(object):
    def __init__(self, name):
        self.name = name  # c) 1. name instance variable
        self.modules = []  # c) 2. modules list instance variable
        self.grades = {}  # c) 3. grades dictionary instance variable

    # c) 4. Create a method called add_module which takes a Module instance as an argument,
    # which should be appended to the list modules.
    def add_module(self, title):
        self.modules.append(title)
        # c) 5. Within the method add_module the Module instance should also be added as a key to the dictionary grades
        # with its corresponding value being the grade of that Module instance.
        # The grade is accessed from get_grade from Module.
        self.grades[title] = title.get_grade


    def get_list_modules(self):
        # c) 6. Create a method called get_list_modules. When called, the method should iterate over
        # all modules in the modules list and print them one after the other.
        print("Modules of the Student {0:s}:".format(self.name))
        for element in self.modules:
            print("\t", element)

    def get_grades(self):
        # c) 7. Create a method called get_grades. When called, the method should iterate over all items in the
        # grades dictionary and print every module followed by its corresponding grade.
        print("Grades of the Student {0:s}:" .format(self.name))
        for element in self.grades:
            print("\t {}, Grade {}" .format(element, element.grade))


### test cases ###

me = Student("FirstName LastName")
me.add_module(info1)
me.add_module(math1)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1
print("-------")
me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6
