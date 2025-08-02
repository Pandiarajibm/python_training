"""
Variable Scope: Accessbility of declared variable

4 Scopes:
1. Local Scope
2. Enclosed Scope
3. Global Scope
4. Builtin Scope
"""

print("1. Local Scope: Accessibility is within function")
print("-"*20)
# ----------------

def my_function():
    x = 100 # Local Scope: We can access within this function
    print("Value of x in my_function:", x)

my_function()

print("#"*40, end="\n\n")
#########################

print("2. Enclosed Scope: Accessibility is within function and nested functions")
print("-"*20)
# ----------------

def my_function():
    x = 100 # Local Scope: We can access within this function and in nested function can acces
    print("Value of x within my_function:", x) # We can access here
    def my_nested_function():
        nonlocal x # Refer outer function variable, don't create local variable
        # x = 10000
        print("Value of x within nested function:", x)
    my_nested_function()
    print("Value of x within my_function:", x)  # We can access here

my_function()

print("#"*40, end="\n\n")
#########################

print("3. Global Scope: We can access anywhere/in any block in the program")
print("-"*20)
# ----------------
x = 1200
y = "Python"
def my_function():
    global y
    print("Access y inside my_function:", y)
    y = "Java"
    print("Chaining value of y to java,  inside my_function:", y)

my_function()
print("Value of y outside my_function:", y)

print("#"*40, end="\n\n")
#########################

# ----------------
# 4. builtin-scope
# ----------------
# - If variable not found in local, enclosed, global then
#   only it will look in builtin
#   if it is not present in builtins then it will throw error
#########################

