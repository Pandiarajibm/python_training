"""
Functions with variable arguments
1. Functions with variable positional arguments
2. Functions with variable keyword arguments
"""
print("1. Functions with variable positional arguments")
print("-"*20)
# ----------------

# *a = Variable positional arguments : args
def add_function(*a):
    print("Received all values and keeping all values in TUPLE:", a)


add_function()
add_function(10)
add_function(20, 30)
add_function(10, 20, 30, 40, 50, 60)

print("#"*40, end="\n\n")
#########################

print("2. Functions with variable keyword arguments")
print("-"*20)
# ----------------

# **a = Variable keyword argument : kwargs
def employee_profile(**a):
    print("Received all values and keeping all values in DICTIONARY:", a)

employee_profile()
employee_profile(name="emp-1")
employee_profile(name="emp-2", company="comp-2")
employee_profile(name="emp-3", company="comp-3", email="abc@abcxyz.com")

print("#"*40, end="\n\n")
#########################



# ----------------
# Taking input from console
# ----------------
# x = int(input("Enter a number: "))
# y = int(input("Enter another number: "))
# print(x, y)
#########################

