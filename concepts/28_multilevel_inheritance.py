"""
Inheritance:
1. Multilevel inheritance
2. Multiple inheritance
"""

print("1. Multilevel inheritance: Example-1")
print("-"*20)
# ----------------

# Requirement: add below method to builtin list-class
# 1. add_course_name
# 2. get_course_name

class MyList(list):

    def add_my_course_name(self, name):
        self.append(name)

    def get_my_course_name(self):
        return self.pop()



my_list = MyList([100, 200, "Java", "C++"])
print("my_list:", my_list)

my_list.append("C")
print("my_list after adding C using append():", my_list)

# Add course name
my_list.add_my_course_name("Python")
print("my_list after adding 'python' using add_my_course_name_method():", my_list)
print("Get course name using get_my_course_name_method():", my_list.get_my_course_name())

print("#"*40, end="\n\n")
#########################

print("1. Multilevel inheritance: Example-2")
print("-"*20)
# ----------------

# Assume below class is already present
class Salary:
    def add_salary(self, salary):
        self.salary = salary
    def get_salary(self):
        return self.salary

# New Requirement: Add below functionalities to existing class salary
# 1. add_tax
# 2. get_tax
# 3. modify get_salary to return (salary-tax)
# 4. provide option to get old_scheme_salary

class NewSalaryClass(Salary):
    # 1. add_tax
    def add_tax(self, t):
        self.tax= t

    # 2. get_tax
    def get_tax(self):
        return self.tax

    # 3. modify get_salary to return (salary-tax)
    # polymorphism: We can rewrite function in the same name as super-class
    def get_salary(self): # Override super class method
        return (self.salary-self.tax)

    # 4. provide option to get old_scheme_salary
    def get_old_scheme_salary(self):
        # 1-way to access super-class method
        old_scheme_salary = super().get_salary() # Immediate super class
        # OR
        # 2-way to access super-class method using class name
        old_scheme_salary = Salary.get_salary(self)
        return old_scheme_salary


e1 = NewSalaryClass()
e1.add_salary(10000)
e1.add_tax(1000)

print("Salary:", e1.get_salary())
print("Tax:", e1.get_tax())
print("Old Salary:", e1.get_old_scheme_salary())

print("#"*40, end="\n\n")
#########################

print("1. Multilevel inheritance: Method Resolution Order")
print("Which Means, when we call method, in what order it will search in inherited classes")
print("-"*20)
# ----------------

print(NewSalaryClass.mro())

print("#"*40, end="\n\n")
#########################

print("2.multiple Inheritance example")
print("-"*20)
# ----------------

# Existing Class-1
class Salary:
    def add_salary(self, salary):
        self.salary = salary
    def get_salary(self):
        return self.salary

# Existing Class-2
class Tax:
    def add_tax(self, t):
        self.tax= t
    def get_tax(self):
        return self.tax

# NEW REQUIREMENT: Write class with below functionalities
# 1. add_salary
# 2. get_salary
# 3. add_tax
# 4. get_tax
# 5. add_name
# 6. get_name

# So, requirement 1 to 6 are present in 2 classes, we can use that
# and remaining 2 methods we can provide implementation

# multiple inheritance
class Employee(Salary, Tax):
    def add_name(self, name):
        self.name = name
    def get_name(self):
        return self.name


e1 = Employee()
e1.add_name("emp-1")
e1.add_salary(10000)
e1.add_tax(1000)

print("name:", e1.get_name())
print("salary:", e1.get_salary())
print("tax:", e1.get_tax())

print("#"*40, end="\n\n")
#########################

print("2. Multiple inheritance: Method Resolution Order")
print("Which Means, when we call method, in what order it will search in inherited classes")
print("-"*20)
# ----------------

print(Employee.mro())

print("#"*40, end="\n\n")
#########################
