"""
Generators: We can create/generate values on the fly without storing in any collection like list/tuple etc
- Basically to save memory
"""

print("WITHOUT Generator function")
print("-"*20)
# ----------------

def my_square_function(my_list):
    result = []
    for x in my_list:
        result.append(x * x)
    return result

L = [10, 20, 30, 40]
square_result = my_square_function(L)
print("square_result:", square_result)

for i in square_result:
    print("Each Squared Value:", i)

# Here, our final requirement is to
# print each squared value
# So, here even getting one squared value in each iteration also fine
#   instead of keeping all squared values in list i.e square_list

print("#"*40, end="\n\n")
#########################


print("Generator function")
print("-"*20)
# ----------------

def my_square_function(my_list):
    for x in my_list:
        yield x * x

L = [10, 20, 30, 40]
square_result = my_square_function(L)
print("square_result:", square_result)

for i in square_result:
    print("Each Squared Value:", i)


print("#"*40, end="\n\n")
#########################