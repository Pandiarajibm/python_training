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
square_result = my_square_function(L)   # square_list: [100,400,900,1600]
print("square_result:", square_result)

for i in square_result:
    print("Each Squared Value:", i)

# Here, our final requirement is to
# print each squared value
# So, here even getting one squared value in each iteration also fine
#   instead of keeping all squared values in list i.e square_list
# in this example, we dont want to store square_result as a list.

print("#"*40, end="\n\n")
#########################


print("Generator function")
print("-"*20)
# ----------------

def my_square_function(my_list):
    for x in my_list:
        yield x * x         # on the fly yield will create the result and return. it will not store any value.
                            # yield will store only one value at time and perform a function and then that
        #                   # value is not needed. we do not need to store in a list or tuple like in previous block.
                            # saves memory.

square_result = my_square_function(L)
print("square_result:", square_result)

for i in square_result:
    print("Each Squared Value:", i)

# yield is the generator.
print("#"*40, end="\n\n")
#########################