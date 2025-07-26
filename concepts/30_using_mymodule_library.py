"""
In this program, we are accessing
- variables
- functions
- classes
present in mymodule library
"""

print("1-way: import using 'import-statement'")
print("-"*20)
# ----------------

import mymodule

print("Course:", mymodule.course, end="\n\n")

add_result = mymodule.add(1, 2)
print("add_result:", add_result, end="\n\n")

s1 = mymodule.Student("Student-1", 100)
print("Student - 1 Name:", s1.get_name())
print("Student - 1 Score:", s1.get_score(), end="\n\n")

print("#"*40, end="\n\n")
#########################

print("2-way: import using 'from-import-statement'")
print("-"*20)
# ----------------

from mymodule import course, add, Student

print("Course:", course, end="\n\n")

add_result = add(1, 2)
print("add_result:", add_result, end="\n\n")

s1 = Student("Student-1", 100)
print("Student - 1 Name:", s1.get_name())
print("Student - 1 Score:", s1.get_score(), end="\n\n")

print("#"*40, end="\n\n")
#########################


print("SHORTCUT: 1-way: import using 'import-statement'")
print("-"*20)
# ----------------

import mymodule as mm

print("Course:", mm.course, end="\n\n")

add_result = mm.add(1, 2)
print("add_result:", add_result, end="\n\n")

s1 = mm.Student("Student-1", 100)
print("Student - 1 Name:", s1.get_name())
print("Student - 1 Score:", s1.get_score(), end="\n\n")

print("#"*40, end="\n\n")
#########################

print("SHORTCUT: 2-way: import using 'from-import-statement'")
print("-"*20)
# ----------------

from mymodule import course as c, add as a, Student as S

print("Course:", c, end="\n\n")

add_result = a(1, 2)
print("add_result:", add_result, end="\n\n")

s1 = S("Student-1", 100)
print("Student - 1 Name:", s1.get_name())
print("Student - 1 Score:", s1.get_score(), end="\n\n")

print("#"*40, end="\n\n")
#########################