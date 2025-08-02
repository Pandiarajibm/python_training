"""
In this program, we are keeping
- all variables
- all functions
- all classes
which we are planning to use in other programs

This file is also called as PYTHON-MODULE or PYTHON-LIBRARY
If someone says PYTHON-LIBRARY, some of the variables, functions , classes are present that we can reuse.

Modules are made available to other parts of a Python program using the import statement.
For example, import mymodule allows access to elements within mymodule.py using mymodule.function_name
or mymodule.variable_name.

A Python library is a collection of pre-written code, including modules, packages, functions, classes,
and constants, designed to provide specific functionalities and simplify development. These libraries
allow programmers to reuse code, avoid redundant work, and build more complex and robust applications efficiently.

"""

course = "Python"

def add(a, b):
    return a + b

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_score(self):
        return self.score
    def get_name(self):
        return self.name
'''
    x_1=10 - it is valid. It will work
    1_x=10 - not valid. it will not work as it starts with number.
    def 1_myfunction(); - it will fail
        pass
    def my_function_1();- it will work
        pass
    class 1_myClass: - it will fail
        pass
    class myClass_1: - it will work
        pass


'''
