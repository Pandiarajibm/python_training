class EmployeeClass:
    def __init__(self, emp_name, emp_salary):
            self.emp_name = emp_name
            self.emp_salary = emp_salary

    def get_emp_name(self):
        print(f"Employee Name: {self.emp_name}", end="\n\n")

    def get_emp_salary(self):
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Salary: {self.emp_salary}", end="\n\n")
        return self.emp_salary

def calculate_average_salary(*salaries):
      total_salary = sum(salaries)
      average_salary = total_salary / len(salaries)
      return average_salary

E1=EmployeeClass("Krishnan", 30000)
E2=EmployeeClass("Saravanan",40000)
E3=EmployeeClass("Pandian",50000)

getsalaries = [E1.get_emp_salary(),E2.get_emp_salary(),E3.get_emp_salary()]
print("Average salary of all employees :", calculate_average_salary(*getsalaries),end="\n\n")



