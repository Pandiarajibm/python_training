"""
Decorators:
function to keep code/functionalities which is common for all other functions

https://en.wikipedia.org/wiki/Decorator_pattern

Used Decorator Design Pattern
"""
"""
Below 2 lines are repeated but it is not in sequence, in add,subtract,mul functions 
print("Result is:")
print("End of the result")

To reuse , we define functions to avoid copy paste but reuse the same code everytime needed. But in 
this the repeated lines are not in sequence which is a challenge.
We can handle this by using decorators. it is common to all programming language. not just python.
"""

print("WITHOUT Decorators")
print("-"*20)
# ----------------

def f():
    print("Result is:")
    print("End of the result")


def add(a, b):
    print("Result is:")
    print(a + b)
    print("End of the result")

def subtract(a, b):
    print("Result is:")
    print(a - b)
    print("End of the result")

add(10, 20)
subtract(10, 20)

# Here common functionality/code is
#     print("Result is:")
#     print("End of the result")

# This we are planning to reuse. So we need to keep this in another function-block


print("#"*40, end="\n\n")
#########################


print("USING Decorators")
print("-"*20)
# ----------------

def my_decorator(my_func):# my_func = add
    def decorated_function(x, y): # x=10, y=20
        print("Result is:")
        my_func(x, y) # add(10,20)
        print("End of the result")
    return decorated_function


def add(a, b):
    print(a + b)

inner_function_reference = my_decorator(add)
# inner_function_reference will be having reference to 'decorated_function'
inner_function_reference(10, 20)

def sub(a, b):
    print(a - b)

inner_function_reference = my_decorator(sub)
# inner_function_reference will be having reference to 'decorated_function'
inner_function_reference(10, 20)

def mul(a, b):
    print(a * b)

inner_function_reference = my_decorator(mul)
# inner_function_reference will be having reference to 'decorated_function'
inner_function_reference(10, 20)

print("#"*40, end="\n\n")
#########################

print("FINAL IMPLEMENTATION: USING Decorators")
print("-"*20)
# ----------------

def my_decorator(my_func):# my_func = add
    def decorated_function(x, y): # x=10, y=20
        print("Result is:")
        my_func(x, y) # add(10,20)
        print("End of the result")
    return decorated_function

@my_decorator
def add(a, b):
    print(a + b)

add(10, 20)

# @my_decorator will execute below 2 steps
# inner_function_reference = my_decorator(add)
# inner_function_reference(10, 20)

@my_decorator
def sub(a, b):
    print(a - b)

sub(10, 20)

# @my_decorator will execute below 2 steps
# inner_function_reference = my_decorator(sub)
# inner_function_reference(10, 20)

@my_decorator
def mul(a, b):
    print(a * b)
# @my_decorator will execute below 2 steps
#inner_function_reference = my_decorator(mul)
#inner_function_reference(10, 20)

print("#"*40, end="\n\n")
#########################
