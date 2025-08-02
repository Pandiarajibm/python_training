"""
Strings:
        - We have option to store text data like name, email-id, words, sentence, paragraph
        - Automatically, index number will be assigned to each character
"""

print("Strings PART-1")
print("Store text data")
print("-"*20)
# ----------------

a = 'PERSON'
b = "PERSON'S"
c = """PERSON'S HEIGHT IS XYZ" (" represents inch)"""
d = '''PERSON'S HEIGHT IS XYZ" (" represents inch)'''
e = 'PERSON\'S'

print(a, b, c, d, e, sep='\n')

print("#"*40, end="\n\n")
#########################

print("Strings PART-2")
print("Store text data")
print("-"*20)
# ----------------

my_file_path_1 = "D:\newfolder\test.py"
# \n -> replace with new line
# \t -> replace with tab space
print("my_file_path_1=", my_file_path_1, sep='\n', end="\n\n")


my_file_path_2 = r"D:\newfolder\test.py"
# r -> Raw String
# r -> no special meaning for characters with \
print("my_file_path_2=", my_file_path_2, sep='\n', end="\n\n")

# Convert existing string from non-raw-format to raw-format
my_file_path_3 = repr(my_file_path_1)
print("my_file_path_3=", my_file_path_3, sep='\n', end="\n\n")

print("#"*40, end="\n\n")
#########################

print("Strings PART-3")
print("Store text data")
print("-"*20)
# ----------------

x = 10
y = 20

my_string = f"Value of x is {x} and value of y is {y}"
# f -> format
# f -> Replaces, {variable_name} with value
print("my_string=", my_string, sep='\n', end="\n\n")

print("#"*40, end="\n\n")
#########################

print("Strings PART-4")
print("4 things we can do using index number")
print("1st thing: we can access individual character using index number")
print("-"*20)
# ----------------

my_string = "WEL COME"
print("my_string=", my_string, end="\n\n")

# Refer examples in 5_strings.xlsx
print("Accessing character at 0th index using positive index number:", my_string[0])
print("Accessing character at 0th index using negative index number:", my_string[-8])

print("#"*40, end="\n\n")
#########################

print("Strings PART-5")
print("4 things we can do using index number")
print("2nd thing: we can get sub string using index number")
print("-"*20)
# ----------------

my_string = "WEL COME"
print("my_string=", my_string, end="\n\n")

# Refer examples in 5_strings.xlsx
print("substring from index 1 to 6 using positive index number:", my_string[1:6])
print("substring from index 1 to 6 using negative index number:", my_string[-7:-2])
# IMPORTANT NOTE:
# Always, character at START-INDEX will be included in the substring here index-1
# Always, character at END-INDEX will be excluded. i.e character at index-6 will not come
#   if we want 6 then provide 7 as end index


print("#"*40, end="\n\n")
#########################

print("Strings PART-5")
print("4 things we can do using index number")
print("3rd thing: we can skip characters in between")
print("-"*20)
# ----------------

my_string = "WEL COME"
print("my_string=", my_string, end="\n\n")

# Refer examples in 5_strings.xlsx
print("substring from index 1 to 6 using positive index number with default step value=1:", my_string[1:6])
print("substring from index 1 to 6 using negative index number with default step value=1:", my_string[-7:-2], end="\n\n")
# step value=1: which means, from index-1 to 6, give me every character

print("substring from index 1 to 6 using positive index number with step value=1:", my_string[1:6:1])
print("substring from index 1 to 6 using negative index number with step value=1:", my_string[-7:-2:1], end="\n\n")
# step value=1: which means, from index-1 to 6, give me every character

print("substring from index 1 to 6 using positive index number with step value=2:", my_string[1:6:2])
print("substring from index 1 to 6 using negative index number with step value=2:", my_string[-7:-2:2], end="\n\n")
# step value=2: which means, from index-1 to 6, give me every 2nd character

print("#"*40, end="\n\n")
#########################

print("Strings PART-6")
print("4 things we can do using index number")
print("4th thing: we can traverse in reverse order")
print("-"*20)
# ----------------

my_string = "WEL COME"
print("my_string=", my_string, end="\n\n")

# Example: 6 to 1 in reverse direction
# We need to follow below 3 steps:
# Step-1: start index should be 6
# Step-2: end index should be 1
# Step-3: step value should be negative, here -1
# IMPORTANT: If we miss any step, we will get empty string

# Refer examples in 5_strings.xlsx
print("substring from index-6 to 1 using positive index number with step value -1:", my_string[6:1:-1])
print("substring from index-6 to 1 using negative index number with step value -1:", my_string[-2:-7:-1], end="\n\n")

print("substring from index-6 to 1 using positive index number with step value -2:", my_string[6:1:-2])
print("substring from index-6 to 1 using negative index number with step value -2:", my_string[-2:-7:-2], end="\n\n")

print("substring from index-6 to 1 using positive index number with step value -3:", my_string[6:1:-3])
print("substring from index-6 to 1 using negative index number with step value -3:", my_string[-2:-7:-3], end="\n\n")

print("#"*40, end="\n\n")
#########################

print("Strings PART-7")
print("Methods present inside 'str' class")
print("-"*20)
# ----------------

my_string = "WEL COME"
print("my_string=", my_string, end="\n\n")

print(dir(my_string))
# OR
print(dir(str))

print("#"*40, end="\n\n")
#########################

print("cubicle-1, that is object-1")
print("DATA inside cubicle-1, that is object-1:")
print("-"*20)
# ----------------

cubicle_1 = "Hi"
print(cubicle_1)

print("#"*40, end="\n\n")
#########################


print("cubicle-1, that is object-1")
print("FUNCTIONS/METHODS inside cubicle-1, that is object-1:")
print("-"*20)
# ----------------

print(dir(cubicle_1))

print("#"*40, end="\n\n")
#########################

print("cubicle-2, that is object-2")
print("DATA inside cubicle-2, that is object-2:")
print("-"*20)
# ----------------

cubicle_2 = "Hello"
print(cubicle_2)

print("#"*40, end="\n\n")
#########################


print("cubicle-2, that is object-2")
print("FUNCTIONS/METHODS inside cubicle-2, that is object-2:")
print("-"*20)
# ----------------

print(dir(cubicle_2))

print("#"*40, end="\n\n")
#########################

# ----------------
# >>> # Why function names are starting with __ ?
# ----------------
# >>> # THese names are system defined
# >>> # Directly we are not calling these methods
# >>> # These methods are called by either some operators or some functions
# >>> # complete list of these type of methods:
# https://docs.python.org/3/reference/datamodel.html#special-method-names
#########################

# ----------------
#  Example-1
# ----------------
# >>> s1 = "Hi"
# >>> s2 = "Hello"
# >>> s3 = s1 + s2
# >>> s3
# 'HiHello'
# >>>
# >>> # Internally + will execute __add__
# >>> # We can call directly using __ names
# >>> s4 = s1.__add__(s2)
# >>> s4
# 'HiHello'
#########################

# ----------------
# Example-2
# ----------------
# >>> s1="Hi"
# >>> len(s1)
# 2
# >>> # Internally builtin len() calls __len__ present inside str class
# >>> s1.__len__()
# 2
# >>>
#########################

# ----------------
# Example-3
# ----------------
# >>> s1="Hi"
# >>> my_string = "Hello"
# >>> my_string[0]
# 'H'
# >>> # Internally it calls __getitem__
# >>> my_string.__getitem__(0)
# 'H'
#########################


print("Convert to lowercase")
print("-"*20)
# ----------------

my_string = "WEL COME"
print("my_string=", my_string, end="\n\n")

my_string_lowercase = my_string.lower()
print("my_string_lowercase=", my_string_lowercase, end="\n\n")

print("#"*40, end="\n\n")
#########################

