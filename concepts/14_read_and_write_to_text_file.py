"""
Read and write to text files with any extensions like .txt, .log, .mylog, etc
For testfiles ,any filetype we can give. not always .txt, we can use any file type and
it will stored as text file. we can create without extension also.
"""

"""
We need to follow 3 steps
Step-1: Connect to file
Step-2: Read/Write operations
Step-3: Disconnect from file
"""

"""
We have functions all 3 steps
Step-1: Connect to file
    - open() function
Step-2: Read/Write operations
    - For WRITING: 1) write 2) writelines 3) print-function
    - FOR READING: 1) read 2) readlines 3) readline
Step-3: Disconnect from file
    - close() function
"""

print("All write operations")
print("-"*20)
# ----------------

# Step-1: Connect to file
my_out_file_handle = open(file="my_out_file.txt", mode="w")

# mode 'w': Write only mode, This will create new file, This will erase existing file content
# mode 'r': Read only mode, This will NOT create new file, This will NOT erase existing file content
# mode 'a': Append only mode, This will create new file ONLY if file not present,
#               This will NOT erase existing file content

# mode 'w+': Read/Write mode, This will create new file, This will erase existing file content
# mode 'r+': Read/Write mode, This will NOT create new file, This will NOT erase existing file content
# mode 'a+': Read/Write mode, This will create new file ONLY if file not present,
#               This will NOT erase existing file content
# Read/Write mode means we can read also and write also. using same file handle
# say my_out_file_hand.read
# Read/Write mode means we can read also and write also. using same file handle
# say my_out_file_hand.write


# Step-2: Write operations

# our data
x = 10
y = "Python"

# 1) write() method: It takes one string of any length.
my_out_file_handle.write(str(x)+"\n") #Since text files have string only,we convert integer to string
my_out_file_handle.write(y+"\n")
#one variable only we can pass in my_out_file_handle.write.
# so we write separately in 2 lines

# 2) writelines() method: It takes any collections like list/tuple etc
#    Wherever we pass multiple value, we can use writelines
L = [str(x)+"\n", y+"\n"]
my_out_file_handle.writelines(L)

# 3) print-function:
print(x, y, 20, "Java", sep="\n" ,file=my_out_file_handle)

# Step-3: Disconnect from file
my_out_file_handle.close()

print("Created my_out_file.txt, Please check")

print("#"*40, end="\n\n")
#########################

print("Reading from my_out_file.txt using 1) read()")
print("-"*20)
# ----------------

# Step-1: Connect to file
my_out_file_handle = open(file="my_out_file.txt", mode="r")

# Step-2: Read operations
file_contents = my_out_file_handle.read()
# Returns entire file content in one string
print(file_contents)

print("file_contents in raw format:", repr(file_contents))

# Step-3: Disconnect from file
my_out_file_handle.close()

print("#"*40, end="\n\n")
#########################


print("Reading from my_out_file.txt using 2) readlines()")
print("-"*20)
# ----------------

# Step-1: Connect to file
my_out_file_handle = open(file="my_out_file.txt", mode="r")
#OR - Both same
# my_out_file_handle=open("my_out_file.txt","r")

# Step-2: Read operations
file_contents = my_out_file_handle.readlines()
# Returns entire file content in list. Program will not ignore even space also. so we see \n
print(file_contents)

# Step-3: Disconnect from file
my_out_file_handle.close()

print("#"*40, end="\n\n")
#########################

print("Reading from my_out_file.txt using 3) readline()")
# note it is readline() and not readlines(). so it retuns only one line at a time.
print("-"*20)
# ----------------

# Step-1: Connect to file
my_out_file_handle = open(file="my_out_file.txt", mode="r")

# Step-2: Read operations
file_contents = my_out_file_handle.readline()
# Returns one line
# note it is readline() and not readlines(). so it retuns only one line at a time.
print("1st line:", file_contents)

file_contents = my_out_file_handle.readline()
# Returns one line
print("2nd line:", file_contents)

file_contents = my_out_file_handle.readline()
# Returns one line
print("3rd line:", file_contents)

# Step-3: Disconnect from file
my_out_file_handle.close()

print("#"*40, end="\n\n")
#########################

print("Read line by line using for-loop")
print("-"*20)
# ----------------

# Step-1: Connect to file
my_out_file_handle = open(file="my_out_file.txt", mode="r")

# Step-2: Read operations
for each_line in my_out_file_handle: # Returns each in each iteration
    print(each_line)

# Step-3: Disconnect from file
my_out_file_handle.close()

print("#"*40, end="\n\n")
#########################
