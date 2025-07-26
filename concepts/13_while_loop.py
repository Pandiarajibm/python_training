"""
while-loop: We can execute the loop providing some condition
"""
print("while-loop example")
print("-"*20)
# ----------------

x = 0
while x < 5:
    print("Statement-1 - Value of x is:", x)
    print("Statement-2 - Value of x is:", x)
    print("Statement-3 - Value of x is:", x, end="\n\n")
    x = x + 1


print("#"*40, end="\n\n")
#########################

print("break-statement: We can end while-loop in between")
print("-"*20)
# ----------------

employees_list = ["emp-1", "emp-2", "emp-3", "emp-4", "emp-5"]
print("employees", employees_list, end="\n\n")

# end while-loop if employee name is 'emp-3'
index_no = 0
while index_no < len(employees_list):
    j = employees_list[index_no]
    index_no = index_no + 1
    if j == "emp-4":
        break
    print("Employee", j)


# end for-loop if employee name is 'emp-3'
# for j in employees_list:
#     if j == "emp-4":
#         break
#     print("Employee", j)

print("#"*40, end="\n\n")
#########################

print("continue-statement: We can skip current iteration and go for next iteration")
print("-"*20)
# ----------------

employees_list = ["emp-1", "emp-2", "emp-3",  "emp-2", "emp-4", "emp-2", "emp-5"]
print("employees", employees_list, end="\n\n")

index_no = 0
while index_no < len(employees_list):
    j = employees_list[index_no]
    index_no = index_no + 1
    if j != "emp-2":
        continue
    # Execute below statement only for emp-2
    print("Employee statement-1", j)
    print("Employee statement-2", j)
    print("Employee statement-3", j, end="\n\n")


# for j in employees_list:
#     # Here, values other than emp-2 are not required, Only value 'emp-2' is required.
#     # so directly we can proceed for next iteration if value is other than emp-2
#     if j != "emp-2":
#         continue
#     # Execute below statement only for emp-2
#     print("Employee statement-1", j)
#     print("Employee statement-2", j)
#     print("Employee statement-3", j, end="\n\n")

print("#"*40, end="\n\n")
#########################
print("USING while-else block")
print("-"*20)
# ----------------

employees_list = ["emp-1", "emp-2", "NEWemp-1", "emp-2", "NEWemp-2", "emp-2", "emp-5"]
print("employees", employees_list, end="\n\n")

# Requirement is:
#   - Check are there any new employees present in the list.
#   - if one new employee found in the list then it is found, no need to check remaining values
#   - if found then print "FOUND" else print "NOT FOUND"

index_no = 0
while index_no < len(employees_list):
    each_employee = employees_list[index_no]
    index_no = index_no + 1
    if each_employee.startswith("NEWemp"):
        # my_flag = 1 # NO NEED
        print("New Employee Found")
        break
else:
    print("New Employee NOT Found")


# for each_employee in employees_list:
#     if each_employee.startswith("NEWemp"):
#         # my_flag = 1 # NO NEED
#         print("New Employee Found")
#         break
# else:
#     print("New Employee NOT Found")

# how for-else works?
# - if for-loop ended without using break then execute for-else block
# - if for-loop ended using break then skip for-else block
# other way to say
#   'break' statement will come out from for & else block both


print("#"*40, end="\n\n")
#########################

print("USING while-else block")
print("-"*20)
# ----------------

employees_list = ["emp-1", "emp-2", "emp-1", "emp-2", "emp-2", "emp-2", "emp-5"]
print("employees", employees_list, end="\n\n")

# Requirement is:
#   - Check are there any new employees present in the list.
#   - if one new employee found in the list then it is found, no need to check remaining values
#   - if found then print "FOUND" else print "NOT FOUND"

index_no = 0
while index_no < len(employees_list):
    each_employee = employees_list[index_no]
    index_no = index_no + 1
    if each_employee.startswith("NEWemp"):
        # my_flag = 1 # NO NEED
        print("New Employee Found")
        break
else:
    print("New Employee NOT Found")


# for each_employee in employees_list:
#     if each_employee.startswith("NEWemp"):
#         # my_flag = 1 # NO NEED
#         print("New Employee Found")
#         break
# else:
#     print("New Employee NOT Found")

# how for-else works?
# - if for-loop ended without using break then execute for-else block
# - if for-loop ended using break then skip for-else block
# other way to say
#   'break' statement will come out from for & else block both


print("#"*40, end="\n\n")
#########################
