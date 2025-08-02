"""
set:
        - We have option to store multiple values like list of employee names
        - We can keep only UNIQUE values
        - NO, Index number will be assigned to each values
"""

"""
How to create object in python
- Using class

Example:
a = int(10)
    OR
    SHORTCUT: a =10

b = str("Hello")
    OR
    SHORTCUT: b = "Hello"
    
c = tuple((10, 20, 30))
    OR
    SHORTCUT: c = (10, 20, 30)

d = frozenset([10, 20, 30])
    SHORTCUT: NO SHORTCUT, So we need to use class name only

e = list([10, 20, 30])
    OR
    SHORTCUT: [10, 20, 30]
        
f = set([10, 20, 30])
    OR
    SHORTCUT: {10, 20, 30}

g = dict({"A": 10, "B": 20, "C": 30})
    OR
    SHORTCUT: {"A": [10, 200], "B": 20, "C": 30}
"""

print("set PART-1")
print("Store multiple values")
print("-"*20)
# ----------------


my_set_1 = {"emp-1", "emp-2", "emp-3", "emp-3", "emp-3"}
print("my_set_1:", my_set_1)

# OR

my_set_2 = set(["emp-1", "emp-2", "emp-3", "emp-3", "emp-3"])
print("my_set_2:", my_set_2)

# It will keep unique values
# It will not maintain the order, It is unordered

# Since we don't have index number, we can't access individual values
# OPTION-1: We can convert to other typle like list/tuple etc to get index number
# OPTION-2: We can iterate using loops like for-loop, while-loop

print("#"*40, end="\n\n")
#########################

print("set PART-2")
print("METHODS present inside set class")
print("-"*20)
# ----------------

# print(dir(my_set))
# OR
print(dir(set))

print("#"*40, end="\n\n")
#########################

print("set PART-3")
print("union, intersection, difference methods")
print("-"*20)
# ----------------

sb_account_customers = set(["emp-1", "emp-2", "emp-3", "emp-4"])
print("sb_account_customers: ", sb_account_customers, end="\n\n")
loan_account_customers = set(["emp-3", "emp-4", "emp-5", "emp-6"])
print("loan_account_customers: ", loan_account_customers, end="\n\n")

all_customers = sb_account_customers.union(loan_account_customers)
print("all_customers: ", all_customers, end="\n\n")

customers_having_both_sb_and_loan = sb_account_customers.intersection(loan_account_customers)
print("customers_having_both_sb_and_loan:", customers_having_both_sb_and_loan, end="\n\n")

customers_not_having_loan = sb_account_customers.difference(loan_account_customers)
print("customers_not_having_loan:", customers_not_having_loan)

print("#"*40, end="\n\n")
#########################

print("set PART-4")
print("ADD/REMOVE/UPDATE")
print("-"*20)
# ----------------

sb_account_customers = set(["emp-1", "emp-2", "emp-3", "emp-4"])
print("sb_account_customers: ", sb_account_customers, end="\n\n")

# ADD
sb_account_customers.add("emp-4")
sb_account_customers.add("emp-5")
sb_account_customers.add("emp-6")
print("sb_account_customers after adding emp-4,5,6: ", sb_account_customers, end="\n\n")

# Update
another_set = {"emp-10", "emp-11", "emp-12", "emp-13", "emp-14", "emp-15"}
print("another_set: ", another_set, end="\n\n")
sb_account_customers.update(another_set)
print("sb_account_customers after updating with another_set: ", sb_account_customers, end="\n\n")

# Remove
sb_account_customers.remove("emp-13")
sb_account_customers.remove("emp-14")
popped_value = sb_account_customers.pop() # Random value will be removed
print("sb_account_customers after removing emp-13, 14 and pop(): ", sb_account_customers, end="\n\n")
print("popped_value:", popped_value)

print("#"*40, end="\n\n")
#########################
