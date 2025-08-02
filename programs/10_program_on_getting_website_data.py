"""
Get data from website and print
When we access urls programmatically, it will get blocked. at server level it will be blocked.
if we run one or two times and it is permanent. For python.org also it will get blocked if we run 2 or 3 times in
a day, it will get blocked for that day. next day we can run. since it is public and we are using for learning
purpose then block is for one day only.
However the urls we can access from web browsers but not programmatically if it is blocked.
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