"""
Conditional Statement IF Statement: Based on the condition, we can execute block of code
"""
print("Using only if-blocks")
print("-"*20)
# ----------------

x = 10
if x == 10:
    print("x is equal to 10 statement-1")
    print("x is equal to 10 statement-2")
    print("x is equal to 10 statement-3")
    print("x is equal to 10 statement-4")
    print("x is equal to 10 statement-5")

if x > 10:
    print("x is greater than 10 statement-1")
    print("x is greater than 10 statement-2")
    print("x is greater than 10 statement-3")
    print("x is greater than 10 statement-4")
    print("x is greater than 10 statement-5")

if x < 10:
    print("x is less than 10 statement-1")
    print("x is less than 10 statement-2")
    print("x is less than 10 statement-3")
    print("x is less than 10 statement-4")
    print("x is less than 10 statement-5")

print("#"*40, end="\n\n")
#########################

print("Using if-block and elif-block")
print("-"*20)
# ----------------

x = 10
if x == 10:
    print("x is equal to 10 statement-1")
    print("x is equal to 10 statement-2")
    print("x is equal to 10 statement-3")
    print("x is equal to 10 statement-4")
    print("x is equal to 10 statement-5")

elif x > 10:
    print("x is greater than 10 statement-1")
    print("x is greater than 10 statement-2")
    print("x is greater than 10 statement-3")
    print("x is greater than 10 statement-4")
    print("x is greater than 10 statement-5")

elif x < 10:
    print("x is less than 10 statement-1")
    print("x is less than 10 statement-2")
    print("x is less than 10 statement-3")
    print("x is less than 10 statement-4")
    print("x is less than 10 statement-5")

print("#"*40, end="\n\n")
#########################

print("Using if-block, elif-block and else-block")
print("-"*20)
# ----------------

x = 10
if x == 10:
    print("x is equal to 10 statement-1")
    print("x is equal to 10 statement-2")
    print("x is equal to 10 statement-3")
    print("x is equal to 10 statement-4")
    print("x is equal to 10 statement-5")

elif x > 10:
    print("x is greater than 10 statement-1")
    print("x is greater than 10 statement-2")
    print("x is greater than 10 statement-3")
    print("x is greater than 10 statement-4")
    print("x is greater than 10 statement-5")

else:
    print("x is less than 10 statement-1")
    print("x is less than 10 statement-2")
    print("x is less than 10 statement-3")
    print("x is less than 10 statement-4")
    print("x is less than 10 statement-5")

print("#"*40, end="\n\n")
#########################

print("if-block with strings")
print("-"*20)
# ----------------

my_string = "Python"
print("my_string", my_string, end="\n\n")

if (my_string == "Python") and ("th" in my_string):
    print("substring 'th' found")

print("#"*40, end="\n\n")
#########################

print("if-block with list/tuples/any-other-collection")
print("-"*20)
# ----------------

employees_list = ["emp-1", "emp-2", "emp-3", "emp-4", "emp-5"]
print("employees_list", employees_list, end="\n\n")

if "emp-3" in employees_list:
    print("Employee emp-3 present in list")

print("#"*40, end="\n\n")
#########################

print("if-block with dictionary")
print("-"*20)
# ----------------

my_dictionary = {"course": "python", "mode": "online"}
print("my_dictionary", my_dictionary, end="\n\n")

# >>> my_dictionary.keys()
# ['course', 'mode']
if "mode" in my_dictionary.keys():
    print("Key 'mode' found")

# >>> my_dictionary.values()
# ['python', 'online']
if "python" in my_dictionary.values():
    print("Value 'python' found")

# >>> my_dictionary.items()
# [('course', 'python'), ('mode', 'online')]
if ('course', 'python') in my_dictionary.items():
    print("Both key/value pairs found")

print("#"*40, end="\n\n")
#########################
