"""
Variable Scope: Accessbility of declared variable

4 Scopes:
1. Local Scope
2. Enclosed Scope
3. Global Scope
4. Builtin Scope
"""

print("1. Local Scope: Accessibility is within function")
print("-" * 20)


# ----------------

def my_function():
    x = 100  # Local Scope: We can access within this function
    print("Value of x in my_function:", x)


my_function()

print("#" * 40, end="\n\n")
#########################

print("2. Enclosed Scope: Accessibility is within function and nested functions")
print("-" * 20)


# ----------------

def my_function():
    x = 100  # Local Scope: We can access within this function and in nested function can acces
    y=150
    print("Value of x,y within my_function:", x,y )  # We can access here
    # note this my_function and the below nested function follow same indentation of my_function().
    def my_nested_function():
        nonlocal x  # Refer outer function variable, don't create local variable
        x=10000 # it will modify the x of outer function as it is # nonlocal x
        y=250 # local scope for my_nested_function
        print("Value of x, y within nested function:", x, y)
    my_nested_function() # can be called only within my_function()
    print("Value of x,y within my_function:", x, y)

#my_nested_function() - we cannot use this function outside my_function()
# will get NameError: name 'my_nested_function' is not defined
my_function()

#if we have to call nested function outside mu_function() we can use return my_nested_function()
print("#" * 40, end="\n\n")
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
    print("Changing value of y to java,  inside my_function:", y)

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
#   Non-Local and Global scope   are used purely in inside function
#########################
