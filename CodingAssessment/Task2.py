"""
Task-2:
Write instance methods to get emp_name, emp_id, emp_salary


Expected output:
E1.get_emp_name()
Should print:
‘emp-1’


E1.get_emp_id()
Should print: 100

E1.get_emp_salary()
Should print:
1000

"""

"""
Write a class named ‘EmployeeClass’ which is having 	init	() method with 3 arguments
 emp_name, emp_id, emp_salary
   Example:
E1 = EmployeeClass(‘emp-1’, 100, 1000)
"""
#----------------
print("###"*20)
# ----------------

class EmployeeClass:
    def __init__(self, emp_name, emp_id, emp_salary):
            self.emp_name = emp_name
            self.emp_id = emp_id
            self.emp_salary = emp_salary

    def get_emp_name(self):
        print(f"Employee Name: {self.emp_name}")

    def get_emp_id(self):
        print(f"Employee id: {self.emp_id}")

    def get_emp_salary(self):
        print(f"Employee Salary: {self.emp_salary}",end="\n\n")

E1=EmployeeClass("Krishnan", 4393, 20000)
E2=EmployeeClass("Saravanan",5838,40000)

E1.get_emp_name()
E1.get_emp_id()
E1.get_emp_salary()
E2.get_emp_name()
E2.get_emp_id()
E2.get_emp_salary()
