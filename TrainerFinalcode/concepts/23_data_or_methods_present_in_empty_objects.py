"""
What data and methods present in each empty objects which we created
"""

print("Our Own Class Definition - 1")
print("-"*20)
# ----------------

class Employee:
    pass

# OR

class Employee(object):
    pass

# Both the classes are same

print("#"*40, end="\n\n")
#########################


print("Create 2 objects")
print("-"*20)
# ----------------

e1 = Employee()
e2 = Employee()

print("#"*40, end="\n\n")
#########################

print("DATA present in all three empty cubicles/objects")
print("-"*20)
# ----------------

print("DATA present in cubicle/class-object 'Employee':", Employee)
print("DATA present in cubicle/instance-object 'e1':", e1)
print("DATA present in cubicle/instance-object 'e2':", e2)

print("#"*40, end="\n\n")
#########################

print("METHODS present in all three empty cubicles/objects")
print("-"*20)
# ----------------

print("METHODS present in cubicle/class-object 'Employee':", dir(Employee), sep="\n", end="\n\n")
print("METHODS present in cubicle/instance-object 'e1':", dir(e1), sep="\n", end="\n\n")
print("METHODS present in cubicle/instance-object 'e2':", dir(e2), sep="\n", end="\n\n")

print("#"*40, end="\n\n")
#########################
