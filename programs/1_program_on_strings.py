"""
Referred https://jafsoft.com/searchengines/log_sample.html to get the given string.
From the given string,

Extract

IP
DATE
PICS
URL

Expected Output
------------------
123.123.123.123
26/Apr/2000
wpaper.gif
http://www.jafsoft.com/asctortf/
------------------
"""

print("Input Data:")
print("-"*20)
# ----------------
# input data below is formatted data ie there is a clear structure in data
# since it is formatted , we use String

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(input_data)

print("#"*40, end="\n\n")
#########################

print("Type of Input Data:")
print("-"*20)
# ----------------

print(type(input_data))

print("#"*40, end="\n\n")
#########################

print("Extract IP: NOT WORKING")
print("-"*20)
# ----------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
ip = input_data[0:15]
print(ip)

print("#"*40, end="\n\n")
#########################

print("Extract IP: 1-way")
print("-"*20)
# ----------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

index_of_1st_space = input_data.find(' ')
ip = input_data[0:index_of_1st_space]
print(ip)

# >>> # Explore find() method
# >>> # Feature-1
# >>> my_string = "WEL COME"
# >>> my_string.find('E') # return index of 1st occurance of 'E'
# 1
# >>> # Feature-2
# >>> my_string = "WEL COME"
# >>> my_string.find('E', 3) # return index of 'E' which is coming after 3rd index
# 7
# >>> # Feature-3
# >>> my_string = "WEL COME"
# >>> my_string.find('COME') # returns index of 'C'
# 4
# >>> # Feature-4
# >>> my_string.find('XYZ') # returns -1 if not found
# -1

print("#"*40, end="\n\n")
#########################

print("Extract IP: 2-way")
print("-"*20)
# ----------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

sp = input_data.split()
print("splitted data:", sp)

ip = sp[0]
print("IP Address is :", ip)
date1=sp[3]
print("date is :", date1)
print("date is :", sp[3])
print("Image Name :", sp[6])
print("URL", sp[10])
i=input_data.find('"http://')
print("Start Index of URL :", i)
i=i+1
e=input_data.find('"',i)
print("End Index of URL :", e)
print (len(sp))
print("URL is :",input_data [i:e]) # this will give url from unformatted data also
# Example:
# >>> # Exploring split() method
# >>> # Feature-1
# >>> my_string = "WEL COME"
# >>> my_string.split() # split be space
# ['WEL', 'COME']
# >>>
# >>> # Feature-2
# >>> my_string = "WEL COME"
# >>> my_string.split("CO") # Split by CO''
# ['WEL ', 'ME']

print("#"*40, end="\n\n")
#########################

