"""
multithreading:

When we run the program, it will create one process and execute the program
- We can check this process in task manager

One program, we can split into smaller pieces and run parallelly. Each piece is called
thread: This is called multi threading
- To increase the performance
- To utilize the resources RAM, processor etc

2nd Option is:
That one program can also split into smaller pieces and run parallelly.
For each piece of code we can create one process and execute.
This is called multiprocessing
"""

"""
In python, multithreading is NOT PARALLEL EXECUTION
BUT
In python, multiprocessing is PARALLEL  EXECUTION
"""

"""
If multithreading is NOT PARALLEL EXECUTION
then what is the use of it?
"""

"""
Still multithreading is useful.

If one thread is waiting for some resource then
during that waiting time, it will execute another thread
SO, we are making use of WAITING TIME of one thread to
execute ANOTHER thread

IF want completely parallel execute then we need use multiprocessing
"""

print("WITHOUT using multithreading")
print("-"*20)
# ----------------

import time

start_time = time.time()

def my_square_function(my_list):
    for i in my_list:
        print("Square:", i*i)

def my_cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)


L = [10, 20, 30, 40]
my_square_function(L)
my_cube_function(L)

end_time = time.time()
print("Time Taken:", end_time - start_time)

print("#"*40, end="\n\n")
#########################


print("USING multithreading")
print("-"*20)
# ----------------

import time

start_time = time.time()

def my_square_function(my_list):
    for i in my_list:
        print("Square:", i*i)

def my_cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)


L = [10, 20, 30, 40]


from threading import Thread

my_square_thread = Thread(target=my_square_function, args=(L,))
my_cube_thread = Thread(target=my_cube_function, args=(L,))

my_square_thread.start()
# It will just start the thread and goto next line
# start() will NOT wait for that thread to complete
my_cube_thread.start()

my_square_thread.join() # wait here till my_square_thread completes
my_cube_thread.join() # wait here till my_cube_thread completes

end_time = time.time()
print("Time Taken:", end_time - start_time)

print("#"*40, end="\n\n")
#########################

print("WITH DELAY: WITHOUT using multithreading")
print("-"*20)
# ----------------

import time

start_time = time.time()

def my_square_function(my_list):
    for i in my_list:
        print("Square:", i*i)
        time.sleep(0.1)

def my_cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)
        time.sleep(0.1)


L = [10, 20, 30, 40]
my_square_function(L)
my_cube_function(L)

end_time = time.time()
print("Time Taken:", end_time - start_time)

print("#"*40, end="\n\n")
#########################


print("WITH DELAY: USING multithreading")
print("-"*20)
# ----------------

import time

start_time = time.time()

def my_square_function(my_list):
    for i in my_list:
        print("Square:", i*i)
        time.sleep(0.1)

def my_cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)
        time.sleep(0.1)


L = [10, 20, 30, 40]


from threading import Thread

my_square_thread = Thread(target=my_square_function, args=(L,))
my_cube_thread = Thread(target=my_cube_function, args=(L,))

my_square_thread.start()
# It will just start the thread and goto next line
# start() will NOT wait for that thread to complete
my_cube_thread.start()

my_square_thread.join() # wait here till my_square_thread completes
my_cube_thread.join() # wait here till my_cube_thread completes

end_time = time.time()
print("Time Taken:", end_time - start_time)

print("#"*40, end="\n\n")
#########################