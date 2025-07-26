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

# Ge3 ways we can do python
# 1.without writing function also we can write a program
# 2.by creating our own function also we can write a program based on requirement
# 3.Creating our own classes also we can write a program
# 4. variables declared in function are in local scope. those variables cannot be
#    accessed outside the function directly.
# 5. However Including class block, if block, for , while block - variables declared inside
#    are global scope and can be accessed outside the block.

