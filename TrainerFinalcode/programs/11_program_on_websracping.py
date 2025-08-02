"""
Program on webscraping using beautifulsoup4 library

Documentation:
    https://pypi.org/project/beautifulsoup4/
    https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    https://docs.python.org/3/library/urllib.request.html
"""

print("Get data from website and print")
print("-"*20)
# ----------------

try:
    import urllib.request as mylib
    my_website_handle = mylib.urlopen("https://www.crummy.com/software/BeautifulSoup/bs4/doc/")
    my_website_data = my_website_handle.read()
    print(my_website_data)
    my_website_handle.close()
except Exception as e:
    print("Not able to get data from website")
    print("Reason: ", e, end="\n\n")

print("#"*40, end="\n\n")
#########################

print("Create object of BeautifulSoup class with website data")
print("-"*20)
# ----------------

from bs4 import BeautifulSoup
soup = BeautifulSoup(my_website_data, "html.parser")
print(soup)

print("#"*40, end="\n\n")
#########################

print("Neatly display the html content")
print("-"*20)
# ----------------

print(soup.prettify())

print("#"*40, end="\n\n")
#########################

print("Only head tag")
print("-"*20)
# ----------------

head_tag = soup.head
print(head_tag)

print("#"*40, end="\n\n")
#########################

print("Only Body tag")
print("-"*20)
# ----------------

head_tag = soup.body
print(head_tag)

print("#"*40, end="\n\n")
#########################

print("1st title tag in entire website content")
print("-"*20)
# ----------------

title_tag = soup.title
print("title_tag:", title_tag) # <title>Welcome to Python.org</title>

print("#"*40, end="\n\n")
#########################

print("1st title tag inside head-tag")
print("-"*20)
# ----------------

title_tag = soup.head.title
print("title_tag:", title_tag) # <title>Welcome to Python.org</title>

print("#"*40, end="\n\n")
#########################

print("Content of title tag")
print("-"*20)
# ----------------

title_tag_content = soup.head.title.text
print("title_tag_content:", title_tag_content) # Welcome to Python.org
print("type of title_tag_content:", type(title_tag_content))

print("#"*40, end="\n\n")
#########################


print("1st link tag in entire website content")
print("-"*20)
# ----------------

print(soup.link) # <link rel="prefetch" href="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js">

print("#"*40, end="\n\n")
#########################

print("1st link tag inside head tag")
print("-"*20)
# ----------------

print(soup.head.link) # <link rel="prefetch" href="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js">

print("#"*40, end="\n\n")
#########################

print("1st link tag and its attributes")
print("-"*20)
# ----------------

print("1st link tag:", soup.head.link) # <link rel="prefetch" href="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js">

rel_value = soup.head.link.get("rel") # "prefetch"
print("Attribute 'rel': ", rel_value)
print("type of Attribute 'rel' value: ", type(rel_value))

href_value = soup.head.link.get("href")
print("Attribute 'href': ", href_value)
print("type of Attribute 'href' value: ", type(href_value))

print("#"*40, end="\n\n")
#########################

print("All link tags present inside head-tag")
print("-"*20)
# ----------------

all_link_tags = soup.head.find_all(href=True) # Where href attribute should be present
print(all_link_tags)

print("#"*40, end="\n\n")
#########################

print("All href tags present inside each link-tag")
print("-"*20)
# ----------------

for each_link_tag in all_link_tags:
    print("Tag:", each_link_tag)
    print("URL:", each_link_tag.get("href"))

print("#"*40, end="\n\n")
#########################

print("All paragraph tags")
print("-"*20)
# ----------------

all_paragraph_tags = soup.find_all("p")
print(all_paragraph_tags)
# Ex: [<p>some text</p>,    <p>some text</p>,   <p>some text</p>,  etc ]

print("#"*40, end="\n\n")
#########################


print("all paragraphs content")
print("-"*20)
# ----------------

L = [10, 20, 30, 40, 50]
M = [i*i    for i in L] # Oneliner : Called Comprehensions

# Ex: [<p>some text</p>,    <p>some text</p>,   <p>some text</p>,  etc ]
all_paragraph_contents = [each_paragraph_tag.text       for each_paragraph_tag in all_paragraph_tags]
print(all_paragraph_contents)
# ["pargraph-1 content", "pargraph-2 content", "pargraph-3 content", ]

print("#"*40, end="\n\n")
#########################

print("All anchor(<a>) tag")
print("-"*20)
# ----------------

all_anchor_tags = soup.find_all("a")
print(all_anchor_tags)
# [<a href=''> </a>, <a href=''> </a>, <a href=''> </a>, <a href=''> </a>, ]

print("#"*40, end="\n\n")
#########################

print("All URLS")
print("-"*20)
# ----------------

# [<a href=''> </a>, <a href=''> </a>, <a href=''> </a>, <a href=''> </a>, ]
all_urls = [each_anchor_tag.get("href")     for each_anchor_tag in all_anchor_tags]
# This oneliner is called comprehension
print(all_urls)
# ["url-1", "url-2", "url3"]

print("#"*40, end="\n\n")
#########################

print("Cleanup All URLS")
print("-"*20)
# ----------------

cleaned_urls = [each_url   for each_url in all_urls  if each_url.startswith("http")]
print(cleaned_urls)

print("#"*40, end="\n\n")
#########################

print("Create dictionary with all urls and paragraphs")
print("-"*20)
# ----------------

my_webscrape_dictionary = {
    "website_title": title_tag_content,
    "all_urls": cleaned_urls,
    "all_paragraphs": all_paragraph_contents}
print(my_webscrape_dictionary)

print("#"*40, end="\n\n")
#########################

print("Write to web_scrape_report.json file")
print("-"*20)
# ----------------

my_json_file_handle = open(file="web_scrape_report.json", mode="w")

import json
json.dump(my_webscrape_dictionary, my_json_file_handle)

my_json_file_handle.close()

print("Created web_scrape_report.json file")

print("#"*40, end="\n\n")
#########################
