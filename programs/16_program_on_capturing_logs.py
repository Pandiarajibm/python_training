"""
intead of printing the output in console, if we save it in file, later we can refer to understand the output.

logging library: To capture message in file instead of printing on the console
Documentation - https://docs.python.org/3/library/logging.html
logging library is standard library. no need to install the library.

What is the advantage of using logging library instead of printing? we get a lot of options,levels while capturing the logs.
ie logging current timestop, created timestop, function name etc. we can capture all the standard logging variables
we can capture and use that. all standard items we can capture using the variables.

Benefit
1. we can capture all the standard logging options,variables etc. There are predefined variables which we can use
for logging are readily available.

go thro standard library for clear details of it
https://docs.python.org/3/library/logging.html

2. we can capture and categorise each and every step output,info,warning, error message in log file.
   it will be helpful in debugging.We can categorise the message easily.
   info means we can capture as info.warning, debug, we catogorize in debug. warning, error message.
In below try block, instead of printing , we can capture each information while logging.
In one log, whatever details which we may need to capture , for all there are variables available which we can use.

try:
    print("Reached try block")
    print("Opening file..")
except Exception as e:
    print("Reached Except Block")
    print("This exception block is written to handle all file open() function error")
else:
    print("Reached else Block")
    print("If try-block success then we need to write to file")

1 logging.debug to help debug, we are printing message in the log.
2. loging.info - for informational purpose.
3. logging.warning - for warning purpose.
4. logging.error - for capturing error message
5. logging.critical
above 5 of some of levels used for logging the messages

if we want to print all info say debug , warning, error message etc in logging.info . python,logging functions
will not retrict. it is developer decision at what level it has to be logged but if they don't follow
the catogorisation then user will confuse. if all info is put in log.info, then user reading log file
will assume there is no error message and all are working good which may be wrong at times.

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
                    # refer this while seeing my_own_log_file.log to understand the messages in my_own_log_file.log.
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
        #my_logger.error("Error message:",e)")
        my_logger.error(f"Error message:{e}")
        #my_file_handle is not defined.so we use{e} with f- (f"Error message:{e}")

print("Program output captured in my_own_log_file.log. Please check")

print("#"*40, end="\n\n")
#########################