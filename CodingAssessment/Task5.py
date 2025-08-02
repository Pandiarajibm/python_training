"""
Task-5:
Write 2 class-methods where one method to set company head name and another method to get
company head name


Example:
EmployeeClass.set_company_head_name(‘head-1’)
print(EmployeeClass.get_company_head_name) # output  ‘head-1’

"""

print("Class EmployeeClass")
print("-"*20)
# ----------------

class EmployeeClass:
    @classmethod
    def set_company_head_name(cls,company_head_name,):
        cls.company_head_name = company_head_name
    @classmethod
    def get_company_head_name(cls):
        return cls.company_head_name

EmployeeClass.set_company_head_name("head1")
print(EmployeeClass.get_company_head_name())

#EmployeeClass.set_company_head_name(Head1) = "Head1"

#print( EmployeeClass.company_head_name, end="\n\n")

print("#"*40, end="\n\n")
#########################


