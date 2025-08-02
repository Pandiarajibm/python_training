"""
Trying __ (Double Underscore names)
which is system defined names
these names are given to
 - some operators
    Example:
        for +, system defined name is __add__
 - some functions
        for builtin len(), system defined name is __len__
"""

print("Class Employee")
print("-"*20)
# ----------------

class Employee:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


e1 = Employee("Emp-1")
e2 = Employee("Emp-2")

print("Employee-1 Name:", e1.get_name())
print("Employee-2 Name:", e2.get_name(), end="\n\n")

print("#"*40, end="\n\n")
#########################


print("Supporting + operator")
print("-" * 20)
# ----------------

class Employee:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __add__(self, second_object): # self=e1, second_object=e2
        first_employee_name = self.name
        second_employee_name = self.name
        return first_employee_name + second_employee_name

e1 = Employee("Emp-1")
e2 = Employee("Emp-2")

print("Employee-1 Name:", e1.get_name())
print("Employee-2 Name:", e2.get_name(), end="\n\n")

# Requirement: if we add 2 objects of Employee class then
#   it should concatinate both names and return
add_result = e1+e2 # Internally e1.__add__(e2)
print("add_result:", add_result, end="\n\n") # "Emp-1Emp-2"

print("#" * 40, end="\n\n")
#########################

print("Supporting len() function")
print("-" * 20)
# ----------------

class Employee:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __add__(self, second_object): # self=e1, second_object=e2
        first_employee_name = self.name
        second_employee_name = second_object.name
        return first_employee_name + second_employee_name

    def __len__(self): # self=e1, e2
        # 1-WAY: Without using len() with string
        count = 0
        for i in self.name:
            count += 1
        return count
        # 2-WAY: Using len() with string
        # result = len(self.name)
        # return result

e1 = Employee("Emp-1")
e2 = Employee("Emp-2")

print("Employee-1 Name:", e1.get_name())
print("Employee-2 Name:", e2.get_name(), end="\n\n")

# Requirement: if we add 2 objects of Employee class then
#   it should concatinate both names and return
add_result = e1+e2 # Internally e1.__add__(e2)
print("add_result:", add_result, end="\n\n") # "Emp-1Emp-2"

print("Length of e1:", len(e1)) # e1.__len__()
print("Length of e2:", len(e2), end="\n\n")  # e2.__len__()

print("#" * 40, end="\n\n")
#########################


print("Supporting Iteration")
print("-" * 20)
# ----------------

class Employee:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __add__(self, second_object): # self=e1, second_object=e2
        first_employee_name = self.name
        second_employee_name = second_object.name
        return first_employee_name + second_employee_name

    def __len__(self): # self=e1, e2
        # 1-WAY: Without using len() with string
        count = 0
        for i in self.name:
            count += 1
        return count
        # 2-WAY: Using len() with string
        # result = len(self.name)
        # return result

    def __iter__(self): # 1st time only, one time only, before starting iteration it will call.
        self.index_no = 0
        return self

    def __next__(self): # This will be called every iteration, This will give value for each iteration
        current_index = self.index_no
        self.index_no += 1
        if current_index < len(self):
            return self.name[current_index]
        else:
            raise StopIteration

e1 = Employee("Emp-1")
e2 = Employee("Emp-2")

print("Employee-1 Name:", e1.get_name())
print("Employee-2 Name:", e2.get_name(), end="\n\n")

# Requirement: if we add 2 objects of Employee class then
#   it should concatinate both names and return
add_result = e1+e2 # Internally e1.__add__(e2)
print("add_result:", add_result, end="\n\n") # "Emp-1Emp-2"

print("Length of e1:", len(e1)) # e1.__len__()
print("Length of e2:", len(e2), end="\n\n")  # e2.__len__()

# REQUIREMENT: Iterate each char
for i in e1:
    print("Each char in e1:", i)

# E
# m
# p
# -
# 1

print("\n")

for j in e2:
    print("Each char in e2:", j)

# E
# m
# p
# -
# 2

print("#" * 40, end="\n\n")
#########################

