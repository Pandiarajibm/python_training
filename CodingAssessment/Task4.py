"""
Task-4:
Make this ‘EmployeeClass’ iterable where if we iterate, in every iteration, it should return
each character of emp_name.

Example:

E1 = EmployeeClass(‘emp-1’, 100, 1000)

for c in E1:
print(“Each Char:”, c)

Then output should be Each Char: e
Each Char: m Each Char: p Each Char: - Each Char: 1

"""

class EmployeeClass:
    def __init__(self, emp_name, emp_id, emp_salary):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
    #----------------
print("Iterate string")
print("-"*20)
# ----------------
E1=EmployeeClass("Krishnan", 4393, 20000)
E2=EmployeeClass("Saravanan", 4394, 21000)

for i in E1.emp_name:
    print("Each Char :",i)

print("-"*20)

for i in E2.emp_name:
    print("Each Char :",i)

print("#"*40, end="\n\n")
#########################

