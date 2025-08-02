"""
Exceptions Handling
"""

# print("WITHOUT handling exceptions")
# print("-"*20)
# # ----------------
#
# a = 10
# b = 0
# result = a/b # Program will terminate abruptly here.
# print(result)
#
# print("#"*40, end="\n\n")
# #########################

print("Exception Handling using 'try-except' blocks")
print("-"*20)
# ----------------

try:
    a = 10
    b = 0
    result = a/b # Program will NOT terminate here. Instead control will be passed to 'except-block'
    print(result)
except:
    print("Reached Except Block")
    print("Here we are writing logic to solve problem happened in try-block")

print("#"*40, end="\n\n")
#########################


# ----------------
# About 'Exception' classes
# ----------------
# - We need to have class for each type of exception if we want to handle using
#   try-except blocks.
#   Other way to say,
#   if we don't have class for each exception type, then we CAN'T handle using
#   try-except blocks.
#   If we are not handling using try-except blocks then program will terminate abruptly
#
# - We have few exception classes are defined as part of builtins
#   print(dir(__builtins__))
#
# - For remaining type of error, we need to write exception class so that
#   we can handle using try-except blocks
#
# - Whenerver we are using some libraries, that time most of the libraries
#   also provide exception classes for the type of error occurs while using the libraries
#
# In above 'except-block', we didn't mention type of error to handle?
#  -- by default, default 'except-block' will be able to handle all builtin exceptions
#  -- for any other type of exceptions, we need to mention class name in except block
#
# 'Exception' class is super class for all the exception classes
#
# If we want to write user defined exception class then we need to write
#   subclass of 'Exception' class. then only 'except-block' will understand
#########################


print("We can Specify class name in 'except' blocks")
print("-"*20)
# ----------------

try:
    L = [10, 20]
    print(L[100]) # index 100 is not present so IndexError
except ZeroDivisionError: # 1-way to specify class name in except
    print("Reached Except Block")
    print("This is ZDE")
except NameError as ne: # 2-way to specify class name in except, where we are storing error message
    print("Reached Except Block")
    print("This is NE and value of ne is :", ne)
except Exception as e: # Remaining type of error will come here
    print("Reached Except Block")
    print("This is default except with class name 'Exception' so that we can store error messages:")
    print("Message is :", e)
    #exit()

print("#"*40, end="\n\n")
#########################

print("Total 4 blocks in exceptions handling in python")
print("1. try 2. except 3. else 4. finally")
print("-"*20)
# ----------------

try:
    print("Reached try block")
    print("Opening file..")
    my_file_handle = open(file=r"D:\some\wrong\file.txt", mode="w")
except Exception as e:
    print("Reached Except Block")
    print("This exception block is written to handle all file open() function error")
    print("Error occurred and message is :", e)

else:
    print("Reached else Block")
    print("If try-block success then we need to write to file")
    my_file_handle.write("Hi")
    my_file_handle.write("Hello")
finally:
    print("Reached Finally Block")
    try:
        print("Closing file handle..")
        my_file_handle.close()
    except Exception as e:
        print("Not able to close file handle")
        print("Error message:", e)


# about 'else-block':
# - If try-block success then 'else-block' will execute and skip 'except-block'
# - If try-block failed then 'except-block' will execute and skip 'else-block'

# about 'finally-block'
# - 'finally-block' will execute always
# - 'always' means, if try-block/except-block/else-block SUCCESS/FAILED
#   in both the cases it will execute
# - So, use this block for mandatory task, cleanup, logout, closing connections
#   which we want to doit in both success/failed cases

print("#"*40, end="\n\n")
#########################

# ----------------
# 'os' library
# ----------------
# Use this library for directory operations
#########################

print("User defined exception class Example-1")
print("-"*20)
# ----------------

# Mandatory Step: our class should be subclass of 'Exception' class

# Minimal things are in MyError Exception class
class MyError(Exception):
    pass

# - Above Exception class is empty class
# - Above Exception class is valid class
# - Above Exception class is empty class, which means we can specify in 'except-block'
#   and except-block will understand MyError class

try:
    x = 10
    if x == 10:
        raise MyError("MyError: Here value is equal to 10")
    if x > 10:
        raise MyError("MyError: Here value is greater than 10")
    if x < 10:
        raise MyError("MyError: Here value is less than 10")

except MyError as e:
    print("Reached MyError Except Block")
    print("Error message:", e)

print("#"*40, end="\n\n")
#########################

print("User defined exception class Example-2")
print("-"*20)
# ----------------

# Mandatory Step: our class should be subclass of 'Exception' class

# Minimal things are in MyError Exception class
class MyError(Exception):
    def how_to_debug(self):
        return "Steps to debug"

    def some_help_function(self):
        return "Some help function"

# - Above Exception class is empty class
# - Above Exception class is valid class
# - Above Exception class is empty class, which means we can specify in 'except-block'
#   and except-block will understand MyError class

try:
    x = 10
    if x == 10:
        raise MyError("MyError: Here value is equal to 10")
    if x > 10:
        raise MyError("MyError: Here value is greater than 10")
    if x < 10:
        raise MyError("MyError: Here value is less than 10")

except MyError as e:
    print("Reached MyError Except Block")
    print("Error message:", e)
    print("How to debug:", e.how_to_debug())
    print("Some help:", e.some_help_function())

print("#"*40, end="\n\n")
#########################

# ----------------
# We can write except-block anywhere
# ----------------
# Example-1 : outside of function & class
try:
    pass
except:
    pass

# Example-2 : inside function
def f():
    try:
        pass
    except:
        pass

# Example-3: Inside class
class MyClass:
    def my_method_1(self):
        try:
            pass
        except:
            pass
#########################


