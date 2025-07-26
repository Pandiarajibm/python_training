'''
Write a class named ‘EmployeeClass’ which is having 	init	() method with 3 arguments
 emp_name, emp_id, emp_salary
   Example:
E1 = EmployeeClass(‘emp-1’, 100, 1000)

'''

class EmployeeClass:
    def __init__(self, emp_name, emp_id, emp_salary):
            self.emp_name = emp_name
            self.emp_id = emp_id
            self.emp_salary = emp_salary

    def get_all_details(self):
            """
            Prints the details of the employee.
            """
            print(f"Employee Name: {self.emp_name}")
            print(f"Employee ID: {self.emp_id}")
            print(f"Employee Salary:{self.emp_salary}")

    def get_emp_name(self):
        print(f"Employee Name: {self.emp_name}", end="\n\n")

    def get_emp_id(self):
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee id: {self.emp_id}", end="\n\n")

    def get_emp_salary(self):
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Salary: {self.emp_salary}",end="\n\n")

E1=EmployeeClass("Krishnan", 4393, 20000)
E2=EmployeeClass("Saravanan",5838,40000)

E1.get_emp_name()
E2.get_emp_name()
E1.get_emp_id()
E2.get_emp_salary()