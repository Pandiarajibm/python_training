"""
logging library: To capture message in file instead of printing on the console
https://docs.python.org/3/library/logging.html
"""

print("Configuring logger")
print("-"*20)
# ----------------

import logging
my_logger = logging.getLogger("my_logger")

logging.basicConfig(filename="my_own_log_file.log",
                    filemode="w",
                    level=logging.DEBUG,
                    format="%(levelname)s : %(filename)s : %(asctime)s : %(message)s"
                    )

print("Logger configured. Please use in your program to capture logs")

print("#"*40, end="\n\n")
#########################

print("Testing my_logger")
print("-"*20)
# ----------------

my_logger.info("This is test INFO message")
my_logger.debug("This is test DEBUG message")
my_logger.warning("This is test WARNING message")
my_logger.error("This is test ERROR message")
my_logger.critical("This is test CRITICAL message")

print("Log captured in my_own_log_file.log, Please check")

print("#"*40, end="\n\n")
#########################


print("Using my_logger in actual programs")
print("-"*20)
# ----------------

try:
    my_logger.info("Reached try block")
    my_logger.info("Opening file..")
    my_file_handle = open(file=r"D:\some\wrong\file.txt", mode="w")
except Exception as e:
    my_logger.info("Reached Except Block")
    my_logger.info("This exception block is written to handle all file open() function error")
    my_logger.error(f"Error occurred and message is :{e}")

else:
    my_logger.info("Reached else Block")
    my_logger.info("If try-block success then we need to write to file")
    my_file_handle.write("Hi")
    my_file_handle.write("Hello")
finally:
    my_logger.info("Reached Finally Block")
    try:
        my_logger.info("Closing file handle..")
        my_file_handle.close()
    except Exception as e:
        my_logger.info("Not able to close file handle")
        my_logger.error(f"Error message:{e}")

print("Program output captured in my_own_log_file.log. Please check")

print("#"*40, end="\n\n")
#########################