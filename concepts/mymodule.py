"""
In this program, we are keeping
- all variables
- all functions
- all classes
which we are planning to use in other programs

This file is also called as PYTHON-MODULE or PYTHON-LIBRARY
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

    