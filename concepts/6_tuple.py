"""
Tuples:
        - We have option to store multiple values like list of employee names
        - We can keep DUPLICATE values
        - Automatically, index number will be assigned to each values
"""
print("Tuple PART-1")
print("Store multiple values like list of employee names")
print("-"*20)
# ----------------

my_tuple = (10, 12.5, "python", (100, 200))
print(my_tuple)

print("#"*40, end="\n\n")
#########################

print("Tuple PART-2")
print("Indexing is similar to strings")
print("-"*20)
# ----------------

print("1st Value:", my_tuple[0])
print("2nd Value:", my_tuple[1])
print("3rd Value:", my_tuple[2])
print("4th Value:", my_tuple[3])

print("#"*40, end="\n\n")
#########################


print("Tuple PART-3")
print("Methods present in 'tuple' class")
print("-"*20)
# ----------------

print(dir(my_tuple))

print("#"*40, end="\n\n")
#########################

print("Tuple PART-4")
print("count and index method")
print("-"*20)
# ----------------

my_tuple = ("emp-1", "emp-2", "emp-3", "emp-3", "emp-3")
print("my_tuple:", my_tuple)

count_of_emp3 = my_tuple.count("emp-3")
print("count_of_emp3:", count_of_emp3)

index_of_emp3 = my_tuple.index("emp-3")
print("index_of_emp3:", index_of_emp3)

print("#"*40, end="\n\n")
#########################