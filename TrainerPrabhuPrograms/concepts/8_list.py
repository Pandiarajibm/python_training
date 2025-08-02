"""
lists:
        - We have option to store multiple values like list of employee names
        - We can keep DUPLICATE values
        - Automatically, index number will be assigned to each values
"""
print("list PART-1")
print("Store multiple values like list of employee names")
print("-"*20)
# ----------------

my_list = [10, 12.5, "python", (100, 200)]
print(my_list)

print("#"*40, end="\n\n")
#########################

print("list PART-2")
print("Indexing is similar to strings")
print("-"*20)
# ----------------

print("1st Value:", my_list[0])
print("2nd Value:", my_list[1])
print("3rd Value:", my_list[2])
print("4th Value:", my_list[3])

print("#"*40, end="\n\n")
#########################


print("list PART-3")
print("Methods present in 'list' class")
print("-"*20)
# ----------------

print(dir(my_list))

print("#"*40, end="\n\n")
#########################

print("list PART-4")
print("count and index method")
print("-"*20)
# ----------------

my_list = ["emp-1", "emp-2", "emp-3", "emp-3", "emp-3"]
print("my_list:", my_list)

count_of_emp3 = my_list.count("emp-3")
print("count_of_emp3:", count_of_emp3)

index_of_emp3 = my_list.index("emp-3")
print("index_of_emp3:", index_of_emp3)

print("#"*40, end="\n\n")
#########################

print("list PART-5")
print("ADD/REMOVE/UPDATE")
print("-"*20)
# ----------------

my_list = ["emp-1", "emp-2", "emp-3", "emp-3", "emp-3"]
print("my_list:", my_list)

# ADD
my_list.append("emp-4")
my_list.insert(2, "emp-5")
print("my_list after adding emp-4 and 5:", my_list)
# ['emp-1', 'emp-2', 'emp-5', 'emp-3', 'emp-3', 'emp-3', 'emp-4']

# UPDATE
my_list[1] = "emp-20"
print("my_list after updating 2nd value to emp-20:", my_list)
# ['emp-1', 'emp-20', 'emp-5', 'emp-3', 'emp-3', 'emp-3', 'emp-4']

# REMOVE
my_list.remove("emp-3") # from left, 1st occurance
# ['emp-1', 'emp-20', 'emp-5', 'emp-3', 'emp-3', 'emp-4']
my_list.pop(3)
print("my_list after removing emp-3 and emp-20:", my_list)
# ['emp-1', 'emp-20', 'emp-5',  'emp-3', 'emp-4']

print("#"*40, end="\n\n")
#########################
