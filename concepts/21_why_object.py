"""
Why Object or why object oriented programming language?

Why cubicle to each employee??? cubicle=object
- Idea is to
    Employee, privacy and to keep related items like bag, phone, lunchbox etc

Why Object: To keep values and related methods,related functionalities

In this section, 2 words
1. Encapsulation: Keeping values/data and related methods together
2. Abstraction: And also we are providing abstraction through methods where
                END USER of the class needs to know what and all methods are present
                and how to use each method. NO NEED TO KNOW HOW INTERNALLY
                IT IS IMPLEMENTED ex:mobile phone , we need to know how to use. no need to know how
                mobile works.

In Python -
Function - without using any object i am calling. can be called without reference
           to an object. ex:print, open . independent to any object.

method - can only be called with reference to an object. ex.write,writelines is a method. close
         is a method. through object only we can call
"""

print("Inside str class")
print("-"*20)
# ----------------

print(dir(str))

print("#"*40, end="\n\n")
#########################

print("DATA Inside str class object-a")
print("-"*20)
# ----------------

object_a = "Java"
print(object_a)

print("#"*40, end="\n\n")
#########################

print("METHODS Inside str class object-a")
print("-"*20)
# ----------------

print(dir(object_a))

print("#"*40, end="\n\n")
#########################


print("DATA Inside str class object-b")
print("-"*20)
# ----------------

object_b = "Python"
print(object_b)

print("#"*40, end="\n\n")
#########################

print("METHODS Inside str class object-b")
print("-"*20)
# ----------------

print(dir(object_b))

print("#"*40, end="\n\n")
#########################