"""
'object' class
- 'object' class is builtin class
- 'object' class is 1st python-class
    OR
    super class for all classes present in python
    OR
    all python-classes are inherited from this super class 'object'

- Inside 'object' - class, we have BASIC functionalities/methods required for
    each every python-classes like constructing the object method __new__,
    initializing the object __init__ etc

- By default, whatever there in 'object'-class will come to each and every
    python-classes, even our Employee-class: Called INHERITANCE
"""

print("Inside 'object' class")
print("-"*20)
# ----------------

print(dir(object))

print("#"*40, end="\n\n")
#########################

print("Employee class")
print("-"*20)
# ----------------

# We can write
class Employee: # Internally it is inheriting from object-class, whatever there in object class will come to employee class
    pass

# OR
# We can also write
class Employee(object): # Explicitly specifying super-class name, This is same as above lcass
    pass

print("#"*40, end="\n\n")
#########################

print("Creating objects")
print("-"*20)
# ----------------

e1 = Employee()
e2 = Employee()

print("#"*40, end="\n\n")
#########################


print("Methods inside class object 'Employee' which is coming from object class")
print("-"*20)
# ----------------

print(dir(Employee))

print("#"*40, end="\n\n")
#########################

print("Methods inside instance object 'e1'")
print("-"*20)
# ----------------

print(dir(e1))

print("#"*40, end="\n\n")
#########################


print("Methods inside instance object 'e2'")
print("-"*20)
# ----------------

print(dir(e2))

print("#"*40, end="\n\n")
#########################
