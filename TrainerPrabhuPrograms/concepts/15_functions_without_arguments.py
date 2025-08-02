"""
Functions: If we want to rewrite/copy-paste same code more than
one time then instead of rewrite/copy-paste, keep that code in a block and
execute that block of code whenever we want.
"""
print("WITHOUT using function")
print("-"*20)
# ----------------

a = 10
b = 20
c = a + b
print("Value of c is:", c)

a = 10
b = 20
c = a + b
print("Value of c is:", c)

a = 10
b = 20
c = a + b
print("Value of c is:", c)

a = 10
b = 20
c = a + b
print("Value of c is:", c)

a = 10
b = 20
c = a + b
print("Value of c is:", c)

print("#"*40, end="\n\n")
#########################

print("USING function")
print("-"*20)
# ----------------

# Function Definition
def my_function():
    a = 10
    b = 20
    c = a + b
    print("Value of c is:", c)


# Function call
my_function()
my_function()
my_function()
my_function()
my_function()

print("#"*40, end="\n\n")
#########################
