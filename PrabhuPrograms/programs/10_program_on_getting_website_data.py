"""
Get data from website and print
"""

print("Get data from website and print")
print("-"*20)
# ----------------

try:
    import urllib.request as mylib
    my_website_handle = mylib.urlopen("https://www.python.org")
    my_website_data = my_website_handle.read()
    print(my_website_data)
    my_website_handle.close()
except Exception as e:
    print("Not able to get data from website")
    print("Reason: ", e, end="\n\n")

print("#"*40, end="\n\n")
#########################
