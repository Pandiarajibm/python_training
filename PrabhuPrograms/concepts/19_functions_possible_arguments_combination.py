"""
Possible function arguments combination
- We can combine all type of arguments in one function
"""
import sys

"""
To combine all type of arguments in one function, 
we need to follow below order

1st put all positional arguments IF ANY
then
2nd put variable positional argument IF ANY
then
3rd put all keyword arguments IF ANY
then
4th put variable keyword argument IF ANY 
"""

print("All type of arguments in one function")
print("-"*20)
# ----------------

# Before * argument, all are considered as POSITIONAL arguments
# After * argument, all are considered as keyword argument
# Always, last argument will be variable keyword argument

def my_function(a, b, *c, d, e, **f):
    print("Value of a is:", a)
    print("Value of b:", b)
    print("Value of c:", c)
    print("Value of d:", d)
    print("Value of e:", e)
    print("Value of f:", f)


my_function(10, 20, d=30, e=40) # With minimal values
my_function(10, 20, 30, 40, 50, d=60, e=70, x=100, y=200, z=300)

print("#"*40, end="\n\n")
#########################

print("2 arguments we need positional arguments")
print("another 2 arguments we need positional/keyword arguments")
print("-"*20)
# ----------------

# a, b: We can pass only values
# c,d: We can pass either values or we can pass in the form of argument_name=value
def my_function(a, b, /, c, d):
    print("Value of a is:", a)
    print("Value of b:", b)
    print("Value of c:", c)
    print("Value of d:", d, end="\n\n")

my_function(10, 20, 30, 40)
my_function(10, 20, c=30, d=40)

print("#"*40, end="\n\n")
#########################

print("2 arguments we need STRICTLY positional arguments")
print("another 2 arguments we need STRICTLY keyword arguments")
print("-"*20)
# ----------------

# before *, all positional
# After *, all keyword

# a, b: We can pass only values
# c,d: We can pass in the form of argument_name=value
def my_function(a, b, /, *, c, d):
    print("Value of a is:", a)
    print("Value of b:", b)
    print("Value of c:", c)
    print("Value of d:", d, end="\n\n")

my_function(10, 20, c=30, d=40)
my_function(10, 20, c=30, d=40)

print("#"*40, end="\n\n")
#########################

print("my_print function")
print("-"*20)
# ----------------

def my_own_print_function(*values, sep="|", end="\n"):
    # print(values[0], values[1], values[2]) #
    print(*values, sep=sep, end=end)
    # *values, each value will be passed individually: UNPACKING

my_own_print_function()
my_own_print_function(10, 20, 30, "HEllo", "Python", "Java")
my_own_print_function(10, 20, 30, "HEllo", "Python", "Java", sep="\t\t\t", end="\n")

print("#"*40, end="\n\n")
#########################

