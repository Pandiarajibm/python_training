"""
2 things here
1. list of directories where import will search
2. how to add new location to 'import'
"""
print("1. list of directories where import will search")
print("-"*20)
# ----------------

import sys
print(sys.path)

print("#"*40, end="\n\n")
#########################

print("2. Adding new location to sys.path so that 'import' will check in that location as well")
print("-"*20)
# ----------------

import sys
sys.path.append(r"D:\mylib1")
sys.path.append(r"D:\mylib2")
sys.path.append(r"E:\mymount\directory")
print(sys.path)

# So, 1st we need to add new location to sys.path
# then
# write 'import' so that 'import' will look in that
# directory as well

print("#"*40, end="\n\n")
#########################
