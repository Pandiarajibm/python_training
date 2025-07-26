"""
How to create objects
    - Using class, we can create n number objects

2 types of objects
1. Class Object
2. Instance Objects
"""
print("Our Own Class Definition - 1")
print("-"*20)
# ----------------

class Employee:
    pass

# ----------------
# About empty class 'Employee'
# ----------------
# - Even though class 'Employee' is empty, it is valid class
# - valid class means, we can create object
# - valid class means, we can store values inside that created objects
# - BUT, since the class is empty, no functionalities
#########################

# ----------------
# about 'pass'
# ----------------
# pass: is dummy keyword
# pass: pass does NOTHING
# pass: Use pass to keep any block empty like if-block, for-block etc
#########################

print("#"*40, end="\n\n")
#########################

print("Our Own Class Definition - 2 : Same as above class")
print("-"*20)
# ----------------

class Employee(object):
    pass

print("#"*40, end="\n\n")
#########################

print("Create objects")
print("-"*20)
# ----------------

e1 = Employee()
e2 = Employee()

print("#"*40, end="\n\n")
#########################


# ----------------
# How many objects are present now?
# ----------------
# Total 3 cubicles/objects are present
# INSTANCE OBJECTS: e1, e2 which we created
# CLASS OBJECT: 'Employee', In the name of class also by default, one cubicle/object
#   will be created, in this cubicle/object we can store common data
#########################

