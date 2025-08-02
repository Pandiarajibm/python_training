'''
Write decorator function outside the above class, decorator function name will be ‘my_company_decorator’. Use this decorator on top of all 3 get-methods deﬁned inside the class. Details of the decorator has been provided below these examples. Please check

Expected output:

E1.get_emp_name() Should print:

Company Name Is: “XYZ Company” ‘emp-1’
Address: XYZ Address

E1.get_emp_id() Should print:

Company Name Is: “XYZ Company” 100
Address: XYZ Address


E1.get_emp_salary() Should print:

Company Name Is: “XYZ Company” 1000
Address: XYZ Address


Decorator Requirement: As we observed above, all get methods are using some common functionality which is
Company Name Is: “XYZ Company” Address: XYZ Address
Write a decorator for this common functionality and make use in all get methods
'''

class EmployeeClass:
    CompanyName ="XYZ Company"
    Address = "ABC Address"
    def __init__(self, emp_name, emp_id, emp_salary):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary

   def get_emp_name(self):
        print("Company Name is: ", EmployeeClass.CompanyName)
        self.emp_name = emp_name

    def get_emp_id(self):
        print("Employee Name: {self.emp_name}")
        print("Employee id: {self.emp_id}", end="\n\n")

    def get_emp_salary(self):
        print("Employee Name: {self.emp_name}")
        print("Employee Name: {self.emp_name}")
        print("Employee Salary: {self.emp_salary}",end="\n\n")

E1=EmployeeClass("Krishnan", 4393, 20000)
E2=EmployeeClass("Saravanan",5838,40000)

E1.get_emp_name()
E2.get_emp_name()
E1.get_emp_id()
E2.get_emp_salary()