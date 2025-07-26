"""
Write a function 'log_process_function' which takes log_file_path as an
argument, then that function should read log file,
extract IP, DATE, URL then return extracted information in dictionary
We can use sample.data.txt we can take and try.
Example:
    l1 = log_process_function("my_log_file_1.txt")
    print(l1) # = {0:(ip,dt, url), 1:(ip,dt, url) }

    l2 = log_process_function("my_log_file_2.txt")
    print(l2) # = {0:(ip,dt, url), 1:(ip,dt, url) }

    l3 = log_process_function("my_log_file_3.txt")
    print(l3) # = {0:(ip,dt, url), 1:(ip,dt, url) }
"""