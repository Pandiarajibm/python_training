"""
How to store data in each cubicle or object

2 terminalogies here
1. CLASS VARIABLES
2. INSTANCE VARIABLES
"""

print("Our Own Class Definition")
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

# Total we have 3 objects/cubicle
# ----------------
# 1. CLASS OBJECT: 'Employee' which is getting creating automatically to store common data
# 2. INSTANCE OBJECTS: 'e1' and 'e2' which we are creating
#########################

print("Store data in all 3 cubicles/objects")
print("-"*20)
# ----------------

Employee.company_name = "XYZ Company"
Employee.company_head = "ABC Head"
Employee.corporate_office = "ABC Location"
# Inside cubicle 'Employee', 3 variables will get created and store values in each variable

e1.name = "Emp-1"
e1.email = "Emp-1@abcxyz.com"
# Inside cubicle 'e1', 2 variables will get created and store values in each variable

e2.name = "Emp-2"
e2.email = "Emp-2@abcxyz.com"
e2.phone = "0123456789"
# Inside cubicle 'e2', 3 variables will get created and store values in each variable

print("#"*40, end="\n\n")
#########################

print("Access all values present in each cubicle or object")
print("-"*20)
# ----------------

print("Company Name:", Employee.company_name)
print("Company Head:", Employee.company_head)
print("Corporate Office:", Employee.corporate_office)

print("Employee - 1 Name:", e1.name)
print("Employee - 1 Email:", e1.email)

print("Employee - 2 Name:", e2.name)
print("Employee - 2 Email:", e2.email)
print("Employee - 2 Phone:", e2.phone)

print("#"*40, end="\n\n")
#########################