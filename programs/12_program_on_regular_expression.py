"""
Get data from sample_data.txt

then
extract
IP
DATE
URL

using regular expression
"""
print("Get data from sample_data.txt")
print("-"*20)
# ----------------

my_file_handle = open(file="sample_data.txt", mode="r")
file_contents = my_file_handle.readlines()
my_file_handle.close()

print(file_contents)

print("#"*40, end="\n\n")
#########################

print("print only IP address lines: WITHOUT writing pattern")
print("-"*20)
# ----------------

import re
for each_line in file_contents:
    match_result = re.match(r'123.123.123.123', each_line)
    print("Each Line:", each_line)
    print("Match Result:", match_result, end="\n\n")

print("#"*40, end="\n\n")
#########################

print("print only IP address lines: USING pattern")
print("-"*20)
# ----------------

import re
for each_line in file_contents:
    # 1-WAY
    # match_result = re.match(r'\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d', each_line)
    # 2-WAY
    match_result = re.match(r'\d{3}.\d{3}\.\d{3}\.\d{3}', each_line)
    # 3-WAY
    match_result = re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', each_line)
    print("Each Line:", each_line)
    print("Match Result:", match_result, end="\n\n")

# ---------------
# COMMENT
# ---------------
r"""
In Regular Expression,

IDENTIFIERS
------
\d -> use \d to tell one digit b/n 0 to 9
\D -> use \D to tell one non-digit. Any character expect digits between 0 to 9
. -> Use . (DOT) to say some-character/any-character
\. -> This represents striclty DOT
------

QUANTIFIERS
------
\d{3} -> It makes \d 3 times
\d{1,3} -> It can be one digit or two digits are 3 digits
------

"""

print("#"*40, end="\n\n")
#########################

print("Extract IP")
print("-"*20)
# ----------------

import re
for each_line in file_contents:
    match_result = re.match(r'(\d{3}.\d{3}\.\d{3}\.\d{3})', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        print("IP:", ip)

# ---------------
# COMMENT
# ---------------
r"""
To capture IP Address, put () to IP address pattern
- This is called grouping
- Each group has index numbers starting from 1

"""

print("#"*40, end="\n\n")
#########################

print("Extract IP: Example-2")
print("-"*20)
# ----------------

import re
for each_line in file_contents:
    match_result = re.match(r'((\d{3}.\d{3})\.(\d{3}\.\d{3}))', each_line)
    if match_result is not None:
        full_ip = match_result.group(1)
        print("Full IP:", full_ip)
        first_half_ip = match_result.group(2)
        print("1st half:", first_half_ip)
        second_half_ip = match_result.group(3)
        print("Second Half:", second_half_ip)
        all_match = match_result.group(0)
        print("all_match:", all_match)
        all_match_in_tuple = match_result.group(1, 2, 3)
        print("all_match_in_tuple:", all_match_in_tuple, end="\n\n")

# ---------------
# COMMENT
# ---------------
r"""
To capture IP Address, put () to IP address pattern
- This is called grouping
- Each group has index numbers starting from 1

"""

print("#"*40, end="\n\n")
#########################

print("Extract IP, DATE")
print("-"*20)
# ----------------

import re
for each_line in file_contents:
    # 1-way
    # match_result = re.match(r'(\d{3}.\d{3}\.\d{3}\.\d{3}) - - \[(\d{2}/[A-Za-z]{3}/\d{4})', each_line)
    # 2-way
    match_result = re.match(r'(\d{3}.\d{3}\.\d{3}\.\d{3}).*(\d{2}/[A-Za-z]{3}/\d{4})', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        print(ip, dt, sep="\t\t")

# ---------------
# COMMENT-1
# ---------------
"""
MODIFIERS:
* -> to make 0 or more times
+ -> to make 1 or more times
? -> to make 0 or 1 time
"""

# ---------------
# COMMENT-1
# ---------------
r"""
26/Apr/2000

pattern for  26
----
\d\d # Strictly 2 digits
\d{2} # Strictly 2 digits
[0-9][0-9] # Strictly 2 digits
[0-9]{2} # Strictly 2 digits
\d[0-9] # Strictly 2 digits
[0-9]\d # Strictly 2 digits

\d{1,2} # minimum 1 digit, maximum 2 digits
[0-9]{1,2} # minimum 1 digit, maximum 2 digits
\d?\d # minimum 1 digit, maximum 2 digits
[0-9]?[0-9] # minimum 1 digit, maximum 2 digits
\d?[0-9] # minimum 1 digit, maximum 2 digits
[0-9]?\d # minimum 1 digit, maximum 2 digits
----

pattern for 'Apr'
----
# 1-way
[A-Z][a-z][a-z]

# 2-way
[A-Z][a-z]{2}

# 3-way
[A-Za-z]{3}

# 4-way
(Jan|Feb|Mar|Apr)
----
"""

print("#"*40, end="\n\n")
#########################

print("Extract IP, DATE, URL")
print("-" * 20)
# ----------------

import re

for each_line in file_contents:
    match_result = re.match(r'(\d{3}.\d{3}\.\d{3}\.\d{3}).*(\d{2}/[A-Za-z]{3}/\d{4}).*(http[s]?://[a-z./A-Z_0-9]+)',
                            each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        url = match_result.group(3)
        print(ip, dt, url, sep="\t\t")

# ---------------
# COMMENT-1
# ---------------
r"""

http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF

http[s]?://[a-z./A-Z_]+

# SOME EXAMPLE

http[s]? -> 's' is optional

https? -> here also 's' is optional

[https]? -> 0 occurance OR one occurance of 
            any one of the character present in group characters mentioned in square bracket

(https)? -> extact word 'https' 1 occurance or 0 occurance

abc* -> ab followded by 0 or more occurance of 'c'
        Example:
            ab # MATCH
            abc # MATCH
            abcccccc # MATCH

(abc)* -> Exact 'abc', 0 or more times
        Example:
            abc # MATCH
            abcabc # MATCH
            abcabcabcabc # MATCH
            abcccccc # NOT MATCH

r[ea]d -> r followed by any one character either e or a followed by 'd'
            Example:
                rd # NOT MATCH

                red  # MATCH
                rad  # MATCH

                read  # NOT MATCH
                raed  # NOT MATCH
                reeeaaad  # NOT MATCH
                raaeed # NOT MATCH

r(ea)d -> r followed by extact word 'ea' followed by d
            Example:
                rd # NOT MATCH        
                red  # NOT MATCH
                rad  # NOT MATCH

                read  # MATCH

                raed  # NOT MATCH
                reeeaaad  # NOT MATCH
                raaeed # NOT MATCH


r[ea]?d -> r followed by any one character either e or a or 0 occurance and followed by 'd'
            Example:
                rd # MATCH
                red  # MATCH
                rad  # MATCH

                read  # NOT MATCH
                raed  # NOT MATCH
                reeeaaad  # NOT MATCH
                raaeed # NOT MATCH

r[ea]+d -> r followed by any one or more either 'e' or 'a' followed by 'd'
            Example:
                rd # NOT MATCH
                red  # MATCH
                rad  # MATCH

                read  # MATCH
                raed  # MATCH
                reeeaaad  # MATCH
                raaeed # MATCH

r[ea]*d -> r followed by any ZERO or more either 'e' or 'a' followed by 'd'
            Example:
                rd # MATCH
                red  # MATCH
                rad  # MATCH

                read  # MATCH
                raed  # MATCH
                reeeaaad  # MATCH
                raaeed # MATCH

"""

print("#" * 40, end="\n\n")
#########################
