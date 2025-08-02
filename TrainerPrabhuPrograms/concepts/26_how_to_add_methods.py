"""
How to add methods?
"""
import json

"""
Requirement:
Create class for slack : MySlackClass

1. Add method to store slack channel name
2. Add method to get slack channel name
3. Add method to store slack message of each member
4. Add method to get slack message of each member
5. Get company information
"""

"""
Our Plan

Create class for slack : MySlackClass

* WE WANT TO STORE THIS IN CLASS OBJECT because it is common for all
* Here we need CLASS-OBJECT inside the method
--------------
1. Add method to store slack channel name
2. Add method to get slack channel name
--------------

* WE WANT TO STORE THIS IN separate cubicles so we need to store in INSTANCE OBJECTS
* Here we need INSTANCE-OBJECT inside the method
--------------
3. Add method to store slack message of each member
4. Add method to get slack message of each member
--------------

* We are reading from file/DB, We are not accessing in either INSTANCE/CLASS-OBJECT 
* Here we don't need any-object(INSTANCE/CLASS-OBJECT) inside the method
--------------
5. Get company information from json
--------------
"""

print("Defining the SlackClass")
print("-"*20)
# ----------------
# import json - it will import json for entire program which may not be needed for all methods.

class MySlackClass:
    # import json - it will import json for all functions in the class which may not be needed for all methods.
    # New requirement: Also store employee_name and email
    # self - object reference . we can use any other name instead of self also.standard naming convention self
    # constructer in python is __new__. __init__ is initializer and it is not constructor.
    # In summary: __new__ constructs the object and init initializes the object's attributes.
    # in python , when object is created, __new__ and __init__ will be executed internall.

    def __init__(self, name, email): # Overriding method which is coming from object class to initialize our objects
        self.name = name
        self.email = email

    # New requirement: Also add method to get employee_name and email
    def get_employee_name_and_email(self):
        return {"name": self.name, "email": self.email}

    # - @classmethod will take care of passing class-object only to cls(not e1,e2, e3,etc) even if we are
    #   calling this method using e1, e2 etc
    # this cls or self is not reserved keyword. we can use any name instead.

    # 1. Add method to store slack channel name
    @classmethod
    def store_channel_name(cls, channel_name):
        cls.channel_name = channel_name

    # 2. Add method to get slack channel name
    @classmethod
    def get_channel_name(cls):
        return cls.channel_name

    # 3. Add method to store slack message of each member
    def store_slack_message(self, message):
        self.message = message

    # 4. Add method to get slack message of each member
    def get_slack_message(self):
        return self.message

    # 5. Get company information from json
    @staticmethod
    def get_company_info():
        # create json file
        my_json_file_handle = open(file="my_company_info.json", mode="w")
        my_company_data = {"company_name": "XYZ", "company_email": "email@xyzabc.com"}
        import json   # here we are importing json only for the functions which need it. that much neat it is
        json.dump(my_company_data, my_json_file_handle)
        my_json_file_handle.close()

        # get data from same json file
        my_json_file_handle = open(file="my_company_info.json", mode="r")
        my_company_data = json.load(my_json_file_handle)
        my_json_file_handle.close()
        return my_company_data

print("#"*40, end="\n\n")
#########################

print("Creating 2 objects")
print("-"*20)
# ----------------

e1 = MySlackClass("emp-1", "emp-1@xyzabc.com")
# - It will call  __init__
# - cubicle-address/object-reference will be passed to self
# - So, so self will be having object e1

e2 = MySlackClass("emp-2", "emp-2@xyzabc.com")
# - It will call  __init__
# - cubicle-address/object-reference will be passed to self
# - So, so self will be having object e2

print("#"*40, end="\n\n")
#########################

print("Get employee name and email")
print("-"*20)
# ----------------

print("Employee - 1 Name and Email:", e1.get_employee_name_and_email())
# Here e1 will be passed to self
print("Employee - 2 Name and Email:", e2.get_employee_name_and_email())

print("#"*40, end="\n\n")
#########################

print("Store channel name and get channel name")
print("-"*20)
# ----------------

MySlackClass.store_channel_name("Python-concepts")
# - Cubicle-reference/object-reference 'MySlackClass' will be passed to 'cls'
# - @classmethod will take care of passing class-object only to cls(not e1,e2, e3,etc) even if we are
#   calling this method using e1, e2 etc

print("Channel Name:", MySlackClass.get_channel_name())
# - Cubicle-reference/object-reference 'MySlackClass' will be passed to 'cls'

print("#"*40, end="\n\n")
#########################

print("Store slack message and get slack message")
print("-"*20)
# ----------------

e1.store_slack_message("Hi This is e1")
e2.store_slack_message("Hi This is e2")
# e1, e2 will be passed to self

print("e1 slack message:", e1.get_slack_message())
print("e2 slack message:", e2.get_slack_message())
# e1, e2 will be passed to self

print("#"*40, end="\n\n")
#########################

print("Company Information")
print("-"*20)
# ----------------

# We can call static method using either instance or class objects
# Because we can write static method if we dont need to pass class object
# or instance object
print("Company Info Using Class-object MySlackClass:", MySlackClass.get_company_info(), end="\n\n")
print("Company Info Using Instance-object e1:",e1.get_company_info(), end="\n\n")
print("Company Info Using Instance-object e2:",e2.get_company_info(), end="\n\n")

print("#"*40, end="\n\n")
#########################

# ----------------
# POINT-1: To Make Private
# ----------------
# To make any variables, functions, classes and file
#   then prefix with _
# Example
#   _x=10
#
# def _f():
#   pass
#
# class _MyClass:
#       pass
#
# _my_file_name.py
#########################

# ----------------
# POINT-2: How to access INSTANCE Methods
# ----------------
# 1. Using instance objects i.e e1 & e2
#   Example:
#       e1.store_slack_message("Hi This is e1")
#       e2.store_slack_message("Hi This is e2")
#
# 2. Using class object i.e MySlackClass
#   Example:
#       MySlackClass.store_slack_message(e1, "Hi This is e1")
#       MySlackClass.store_slack_message(e2, "Hi This is e2")
#########################
# @classmethod or @staticmethod - we call them as decorators.
# ----------------
# POINT-3: How to access CLASS Methods
# ----------------
# 1. Using instance objects i.e, e1 & e2
#   Example:
#       e1.store_channel_name("Python-concepts")
#       print("Channel Name:", e1.get_channel_name())
#
#       e2.store_channel_name("Python-concepts")
#       print("Channel Name:", e2.get_channel_name())
#
#       IMPORTANT POINT: @classmethod will make sure to pass class object 'MySlackClass'
#           to 'cls' not e1 or not e2 eventhough we are calling with e1 & e2
#
# 2. Using class object i.e MySlackClass
#   Example:
#       MySlackClass.store_channel_name("Python-concepts")
#       print("Channel Name:", MySlackClass.get_channel_name())
#########################

# ----------------
# POINT-4: How to access STATIC Methods
# ----------------
# 1. Using instance objects i.e, e1 & e2
#   Example:
#       e1.get_company_info()
#       e2.get_company_info()
#
# 2. Using class object i.e MySlackClass
#   Example:
#       MySlackClass.get_company_info()
#########################
# IMPORTANT POINT: @staticmethod will not pass (any object) class object 'MySlackClass' or object instance e1,e2,etc
# eventhough we are calling with MySlackClass or e1 & e2. When We don't need to instance object reference
# or class object reference. we can write @static method.
# To write a logic like get_company_info or computeaveragesalary ie when we did not need to access
# class object or instance object, we can write staticmethod.


# Final summary is we can use any object we can access any method based on  POINT 2, 3, 4

"""
Wikipedia
The @staticmethod decorator in Python is used to define a static method within a class. Static methods are functions that belong to the class but do not operate on instances of the class or the class itself.
Here are the key characteristics and uses of @staticmethod:

    No self or cls parameter:
    Unlike instance methods (which receive self as the first argument) or class methods (which receive cls as the first argument), static methods do not implicitly receive an instance or class reference. They behave like regular functions but are encapsulated within the class's namespace for organizational purposes.

Independence from instance state:
Static methods cannot access or modify instance-specific attributes or methods because they don't have access to self.
Independence from class state:
Static methods also cannot access or modify class-specific attributes or methods using cls.
Calling static methods:
Static methods can be called directly on the class itself, without needing to create an instance of the class. They can also be called on an instance, but the instance is not passed to the method.
"""