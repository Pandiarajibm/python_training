"""
Functions with POSITIONAL and KEYWORD arguments:

Here,
Case-2: How to pass values to variables present inside the function

3 ways, we can pass values to variables present inside the function
1-way: Passing only values to function or passing values in the form argument_name=value
    - These type of functions are called Functions with POSITIONAL and KEYWORD arguments
2-way: RESTRICT to pass only values
    - These type of functions are called Functions with POSITIONAL arguments
3-way: RESTRICT  passing values in the form argument_name=value
    - These type of functions are called Functions with KEYWORD arguments
"""

print("""
1-way: Passing only values to function or passing values in the form argument_name=value
    - These type of functions are called Functions with POSITIONAL and KEYWORD arguments
""")
print("-"*20)
# ----------------

def employee_function(name, company):
    print("Name:", name)
    print("Company:", company, end="\n\n")
    # Step-1: use 'return-statement' inside the function specify values to send
    return {"name": name, "company": company}


received_value = employee_function("emp-1", "comp-1")
print("received_value:", received_value)

# OR we can also specify argument name
received_value = employee_function(name="emp-2", company="comp-2")
print("received_value:", received_value)


print("#"*40, end="\n\n")
#########################


print("""
2-way: RESTRICT to pass only values
    - These type of functions are called Functions with POSITIONAL arguments
""")
print("-"*20)
# ----------------

# / -> is just a syntax to tell it is ONLY POSITIONAL argument
# / -> is not counted as argument
# / -> We are not passing any values to slash

def employee_function(name, company, /):
    print("Name:", name)
    print("Company:", company, end="\n\n")
    # Step-1: use 'return-statement' inside the function specify values to send
    return {"name": name, "company": company}


received_value = employee_function("emp-1", "comp-1")
print("received_value:", received_value)

# This WILL NOT WORK
# received_value = employee_function(name="emp-2", company="comp-2")
# print("received_value:", received_value)


print("#"*40, end="\n\n")
#########################

print("""
3-way: RESTRICT  passing values in the form argument_name=value
    - These type of functions are called Functions with KEYWORD arguments
""")
print("-"*20)
# ----------------

# * -> is just a syntax to tell it is ONLY KEYWORD argument
# * -> is not counted as argument
# * -> We are not passing any values to *

def employee_function(*, name, company):
    print("Name:", name)
    print("Company:", company, end="\n\n")
    # Step-1: use 'return-statement' inside the function specify values to send
    return {"name": name, "company": company}


# # This WILL NOT WORK
# received_value = employee_function("emp-1", "comp-1")
# print("received_value:", received_value)

received_value = employee_function(name="emp-2", company="comp-2")
print("received_value:", received_value)

print("#"*40, end="\n\n")
#########################

print("Some example")
print("-"*20)
# ----------------

x = "emp-2"
y = "comp-2"
received_value = employee_function(name=x, company=y)
print("received_value:", received_value)

print("#"*40, end="\n\n")
#########################


print()
print(10)
print(10, "Hello", [10,20], "Java", "python")
