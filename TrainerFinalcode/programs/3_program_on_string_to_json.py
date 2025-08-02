"""
From the given string,

Extract

IP
DATE
URL

Expected Output in dictionary
------------------
my_dictionary =
{
    0: ('123.123.123.123', '26/Apr/2000', 'http://www.jafsoft.com/asctortf/'),
    1: ('123.123.123.123', '26/Apr/2000', 'http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF'),
    2: ('123.123.123.123', '26/Apr/2000', 'http://www.jafsoft.com/asctortf/'),
    3: ('123.123.123.123', '26/Apr/2000', 'http://www.jafsoft.com/asctortf/'),
    4: ('123.123.123.123', '26/Apr/2000', 'http://www.jafsoft.com/asctortf/'),
    5: ('123.123.123.123', '26/Apr/2000', 'http://www.jafsoft.com/asctortf/')
}
------------------
"""
print("Input Data:")
print("-"*20)
# ----------------

input_data = """
First lets look at a fragment of log file....

fcrawler.looksmart.com - - [26/Apr/2000:00:00:12 -0400] "GET /contacts.html HTTP/1.0" 200 4595 "-" "FAST-WebCrawler/2.1-pre2 (ashen@looksmart.net)"
fcrawler.looksmart.com - - [26/Apr/2000:00:17:19 -0400] "GET /news/news.html HTTP/1.0" 200 16716 "-" "FAST-WebCrawler/2.1-pre2 (ashen@looksmart.net)"

ppp931.on.bellglobal.com - - [26/Apr/2000:00:16:12 -0400] "GET /download/windows/asctab31.zip HTTP/1.0" 200 1540096 "http://www.htmlgoodies.com/downloads/freeware/webdevelopment/15.html" "Mozilla/4.7 [en]C-SYMPA  (Win95; U)"

123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:47 -0400] "GET /asctortf/ HTTP/1.0" 200 8130 "http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/5star2000.gif HTTP/1.0" 200 4005 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:50 -0400] "GET /pics/5star.gif HTTP/1.0" 200 1031 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:51 -0400] "GET /pics/a2hlogo.jpg HTTP/1.0" 200 4282 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:51 -0400] "GET /cgi-bin/newcount?jafsof3&width=4&font=digital&noshow HTTP/1.0" 200 36 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"

(Note, I've added some space for clarity, and changed the IP number to 123.123.123.123 to protect the privacy of the actual visitor)

The fragment shown represents three visitors to my web site
"""

print(input_data)

print("#"*40, end="\n\n")
#########################

print("Making list of lines")
print("-"*20)
# ----------------

list_of_lines = input_data.splitlines()
# OR
# list_of_lines = input_data.split("\n")
print(list_of_lines)

print("#"*40, end="\n\n")
#########################

print("Extract Information and print")
print("-"*20)
# ----------------

for each_line in list_of_lines:
    if each_line.startswith("123"):
        # print("IP Address Line:", each_line)
        sp = each_line.split(" ")
        # print("Splitted line:", sp, end="\n\n")
        ip = sp[0]

        raw_date = sp[3] # '[26/Apr/2000:00:23:48'
        start_index = 1
        end_index = raw_date.find(":")
        dt = raw_date[start_index:end_index]

        raw_url = sp[10] # '"http://www.jafsoft.com/asctortf/"'
        start_index = 1
        end_index = -1
        url = raw_url[start_index:end_index]
        print(ip, dt, url, sep='\t')

print("#"*40, end="\n\n")
#########################

print("Create dictionary")
print("-"*20)
# ----------------
my_dictionary = {}
key = 0
for each_line in list_of_lines:
    if each_line.startswith("123"):
        # print("IP Address Line:", each_line)
        sp = each_line.split(" ")
        # print("Splitted line:", sp, end="\n\n")
        ip = sp[0]

        raw_date = sp[3] # '[26/Apr/2000:00:23:48'
        start_index = 1
        end_index = raw_date.find(":")
        dt = raw_date[start_index:end_index]

        raw_url = sp[10] # '"http://www.jafsoft.com/asctortf/"'
        start_index = 1
        end_index = -1
        url = raw_url[start_index:end_index]
        each_line_tuple = (ip, dt, url)
        # print("each_line_tuple:", each_line_tuple)
        my_dictionary[key] = each_line_tuple
        key = key + 1

print(my_dictionary)

print("#"*40, end="\n\n")
#########################

print("Write to json file log_report.json")
print("-"*20)
# ----------------

my_json_file_handle = open(file="log_report.json", mode="w")

import json
json.dump(my_dictionary, my_json_file_handle) # This write function

my_json_file_handle.close()

print("Created log_report.json file")

print("#"*40, end="\n\n")
#########################

# ----------------
# How to write data to json file
# ----------------
# - We can pass int, float, string, list, tuple, dictionary to dump function
# - Other types like set, frozenset etc: convert to list/tuple/dictionary
#   then pass to dump function
#########################

print("Read json file log_report.json")
print("-"*20)
# ----------------

my_json_file_handle = open(file="log_report.json", mode="r")

import json
json_file_content = json.load(my_json_file_handle) # This is read function

my_json_file_handle.close()

print("json_file_content:", json_file_content, end="\n\n")
print("type of json_file_content:", type(json_file_content), end="\n\n")

print("#"*40, end="\n\n")
#########################
