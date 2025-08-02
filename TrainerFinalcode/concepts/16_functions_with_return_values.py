"""
2 Cases:
Case-1: How to access variables present inside the function
Case-2: How to pass values to variables present inside the function

Here,
Case-1: How to access variables present inside the function
"""
from idlelib.debugobj import myrepr

print("Function with single return value")
print("-"*20)
# ----------------

# 2 steps we need to follow
# Step-1: use 'return-statement' inside the function specify values to send
# Step-2: Assign function-call to variable so that return value will be stored

def employee_function():
    name = "emp-1"
    company = "comp-1"
    print("Name:", name)
    print("Company:", company, end="\n\n")
    # Step-1: use 'return-statement' inside the function specify values to send
    return name


# Step-2: Assign function-call to variable so that return value will be stored
received_value = employee_function()
print("received_value:", received_value)

print("#"*40, end="\n\n")
#########################

print("Function with multiple return values : TUPLE")
print("-"*20)
# ----------------

# 2 steps we need to follow
# Step-1: use 'return-statement' inside the function specify values to send
# Step-2: Assign function-call to variable so that return value will be stored

def employee_function():
    name = "emp-1"
    company = "comp-1"
    print("Name:", name)
    print("Company:", company, end="\n\n")
    # Step-1: use 'return-statement' inside the function specify values to send
    return (name, company)


# Step-2: Assign function-call to variable so that return value will be stored
received_value = employee_function()
print("received_value:", received_value)

print("#"*40, end="\n\n")
#########################

print("Function with multiple return values : LIST")
print("-"*20)
# ----------------

# 2 steps we need to follow
# Step-1: use 'return-statement' inside the function specify values to send
# Step-2: Assign function-call to variable so that return value will be stored

def employee_function():
    name = "emp-1"
    company = "comp-1"
    print("Name:", name)
    print("Company:", company, end="\n\n")
    # Step-1: use 'return-statement' inside the function specify values to send
    return [name, company]


# Step-2: Assign function-call to variable so that return value will be stored
received_value = employee_function()
print("received_value:", received_value)

print("#"*40, end="\n\n")
#########################

print("Function with multiple return values : DICTIONARY")
print("-"*20)
# ----------------

# 2 steps we need to follow
# Step-1: use 'return-statement' inside the function specify values to send
# Step-2: Assign function-call to variable so that return value will be stored

def employee_function():
    name = "emp-1"
    company = "comp-1"
    print("Name:", name)
    print("Company:", company, end="\n\n")
    # Step-1: use 'return-statement' inside the function specify values to send
    return {"name": name, "company": company}


# Step-2: Assign function-call to variable so that return value will be stored
received_value = employee_function()
print("received_value:", received_value)

print("#"*40, end="\n\n")
#########################
