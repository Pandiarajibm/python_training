"""
for-loop: Iterate any collection
"""
print("Iterate string")
print("-"*20)
# ----------------

my_string = "Python"
print("my_string", my_string, end="\n\n")

for i in my_string:
    print("statement-1 - Value of i is:",i)
    print("statement-2 - Value of i is:",i)
    print("statement-3 - Value of i is:",i)
    print("statement-4 - Value of i is:",i)
    print("statement-5 - Value of i is:",i)

print("#"*40, end="\n\n")
#########################

print("Iterate list/tuple/any-other-collection")
print("-"*20)
# ----------------

employees_list = ["emp-1", "emp-2", "emp-3", "emp-4", "emp-5"]
print("employees", employees_list, end="\n\n")

for j in employees_list:
    print("Employee", j)

print("#"*40, end="\n\n")
#########################

print("Iterate Dictionary")
print("-"*20)
# ----------------

my_dictionary = {"course": "python", "mode": "online"}
print("my_dictionary", my_dictionary, end="\n\n")

for k in my_dictionary: # Iterate key
    print("Key:", k)
    print("Value:", my_dictionary[k], end="\n\n")

print("#"*40, end="\n\n")
#########################

print("Execute for-loop for 5 times")
print("-"*20)
# ----------------

# range(5) # produce the 0 to 4
# range(2,5) # produce the 2 to 4
# range(1, 10, 2) # produce the 1, 3, 5, 7, 9
# range(0, 10, 2) # produce the 0, 2, 4, 6, 8

for i in range(5): # produce the 0 to 4
    print(i)

print("#"*40, end="\n\n")
#########################

print("break-statement: We can end for-loop in between")
print("-"*20)
# ----------------

employees_list = ["emp-1", "emp-2", "emp-3", "emp-4", "emp-5"]
print("employees", employees_list, end="\n\n")

# end for-loop if employee name is 'emp-3'
for j in employees_list:
    if j == "emp-4":
        break
    print("Employee", j)

print("#"*40, end="\n\n")
#########################

print("continue-statement: We can skip current iteration and go for next iteration")
print("-"*20)
# ----------------

employees_list = ["emp-1", "emp-2", "emp-3",  "emp-2", "emp-4", "emp-2", "emp-5"]
print("employees", employees_list, end="\n\n")

for j in employees_list:
    # Here, values other than emp-2 are not required, Only value 'emp-2' is required.
    # so directly we can proceed for next iteration if value is other than emp-2
    if j != "emp-2":
        continue
    # Execute below statement only for emp-2
    print("Employee statement-1", j)
    print("Employee statement-2", j)
    print("Employee statement-3", j, end="\n\n")

print("#"*40, end="\n\n")
#########################

print("Example-1: print 1st three employees")
print("-"*20)
# ----------------

employees_list = ["emp-1", "emp-2", "emp-3",  "emp-2", "emp-4", "emp-2", "emp-5"]
print("employees", employees_list, end="\n\n")

count = 0
for j in employees_list:
    if count <3:
        print("Employee Name:", j)
        count += 1

print("#"*40, end="\n\n")
#########################

print("Example-2: print only emp-2, 4, 5")
print("-" * 20)
# ----------------

employees_list = ["emp-1", "emp-2", "emp-3", "emp-2", "emp-4", "emp-2", "emp-5", "emp-2", "emp-5"]
print("employees", employees_list, end="\n\n")

records_count = 0
# print only emp-2, 4, 5
for j in employees_list:
    if (j == "emp-2") or (j == "emp-4") or (j == "emp-5"):
        print("Name is :", j)
    if records_count  > 6 : # iterate only till 7 records then end the for-loop
        break
    records_count += 1

print("#" * 40, end="\n\n")
#########################

print("SOME Example: WITHOUT using for-else block")
print("-"*20)
# ----------------

employees_list = ["emp-1", "emp-2", "emp-1", "emp-2", "emp-2", "emp-2", "emp-5"]
print("employees", employees_list, end="\n\n")

# Requirement is:
#   - Check are there any new employees present in the list.
#   - if one new employee found in the list then it is found, no need to check remaining values
#   - if found then print "FOUND" else print "NOT FOUND"
my_flag = 0
for each_employee in employees_list:
    if each_employee.startswith("NEWemp"):
        my_flag = 1
        print("New Employee Found")
        break

if my_flag == 0:
    print("New Employee NOT Found")

print("#"*40, end="\n\n")
#########################

print("Same Example: USING for-else block")
print("-"*20)
# ----------------

employees_list = ["emp-1", "emp-2", "emp-1", "emp-2", "emp-2", "emp-2", "emp-5"]
print("employees", employees_list, end="\n\n")

# Requirement is:
#   - Check are there any new employees present in the list.
#   - if one new employee found in the list then it is found, no need to check remaining values
#   - if found then print "FOUND" else print "NOT FOUND"

# my_flag = 0 # NO NEED
for each_employee in employees_list:
    if each_employee.startswith("NEWemp"):
        # my_flag = 1 # NO NEED
        print("New Employee Found")
        break
else:
    print("New Employee NOT Found")

# how for-else works?
# - if for-loop ended without using break then execute for-else block
# - if for-loop ended using break then skip for-else block
# other way to say
#   'break' statement will come out from for & else block both

# NO NEED
# if my_flag == 0:
#     print("New Employee NOT Found")

print("#"*40, end="\n\n")
#########################
