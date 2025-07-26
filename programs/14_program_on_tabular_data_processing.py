"""
Program on using pandas library for tabular data processing

Problem Statement:'

    Get data from 3 different sources

    1. mydb.sqlite3
    2. log_report.json
    3. web_scrape_report.json

    Then produce single consolidated report
    final_report.csv
    final_report.xlsx
    final_report.json
    final_report.xml

Expected Columns In Final Report:
IP      DATE        URL     ALL_URLS        ALL_PARAGRAPHS
"""

print("Get data from mydb.sqlite3")
print("-"*20)
# ----------------

import sqlite3
my_db_connection = sqlite3.connect("mydb.sqlite3")

import pandas as pd
my_db_data_df = pd.read_sql("SELECT * FROM mytable", my_db_connection)
print(my_db_data_df)

print("#"*40, end="\n\n")
#########################

print("Get data from log_report.json")
print("-"*20)
# ----------------

import pandas as pd
my_log_report_df = pd.read_json("log_report.json")
print(my_log_report_df)

print("#"*40, end="\n\n")
#########################

print("ROTATE: Making rows to columns")
print("-"*20)
# ----------------

my_log_report_df = my_log_report_df.transpose()
print(my_log_report_df)

print("#"*40, end="\n\n")
#########################

print("Get list of columns")
print("-"*20)
# ----------------

print(my_log_report_df.columns)

print("#"*40, end="\n\n")
#########################


print("Renaming columns")
print("-"*20)
# ----------------

my_log_report_df.columns = ["IP", "DATE", "URL"]
print(my_log_report_df.columns)

print("#"*40, end="\n\n")
#########################

print("my_log_report_df after Renaming columns")
print("-"*20)
# ----------------

print(my_log_report_df)

print("#"*40, end="\n\n")
#########################

print("Get data from web_scrape_report.json")
print("-"*20)
# ----------------

my_json_file_handle =open(file="web_scrape_report.json", mode="r")

import json
my_json_data = json.load(my_json_file_handle)

my_json_file_handle.close()

print(my_json_data)

print("#"*40, end="\n\n")
#########################


print("Make website_title also list")
print("-"*20)
# ----------------

my_json_data["website_title"] = [my_json_data["website_title"]]
# keeping title string in list,
# inside list only one value
print(my_json_data)

print("#"*40, end="\n\n")
#########################

print("Create DataFrame with my_json_data")
print("-"*20)
# ----------------

import pandas as pd
my_json_data_df = pd.DataFrame(my_json_data.values(), index=my_json_data.keys())
print(my_json_data_df)

print("#"*40, end="\n\n")
#########################

print("Rotate DataFrame my_json_data_df")
print("-"*20)
# ----------------

my_json_data_df = my_json_data_df.transpose()
print(my_json_data_df)

print("#"*40, end="\n\n")
#########################

# Merge all 3
# 1. my_db_data_df
# 2. my_log_report_df
# 3. my_json_data_df
# 1 & 2, we need append one below the other
# 3rd one, we need to merge as new column

print("VERTICAL: my_db_data_df and my_log_report_df")
print("-"*20)
# ----------------

all_in_one_df = pd.concat([my_db_data_df, my_log_report_df], axis=0)
# axis=0 : VERTICAL MERGINING
print(all_in_one_df)

print("#"*40, end="\n\n")
#########################

print("RESET index number")
print("-"*20)
# ----------------

all_in_one_df = all_in_one_df.reset_index(drop=True)
# drop=True "Remove existing index column
print(all_in_one_df)

print("#"*40, end="\n\n")
#########################

print("HORIZONTAL: all_in_one_df and my_json_data_df ")
print("-"*20)
# ----------------

all_in_one_df = pd.concat([all_in_one_df, my_json_data_df], axis=1)
# axis=1 : HORIZONTAL MERGINING
print(all_in_one_df)

print("#"*40, end="\n\n")
#########################


print("Empty cells in entire dataframe")
print("-"*20)
# ----------------

print(all_in_one_df.isnull())

print("#"*40, end="\n\n")
#########################

print("TOTAL Empty cells in entire dataframe")
print("-"*20)
# ----------------

print(all_in_one_df.isnull().sum())

print("#"*40, end="\n\n")
#########################

print("Fill EMPTY Cells")
print("-"*20)
# ----------------

all_in_one_df["IP"] = all_in_one_df["IP"].fillna("127.0.0.1")
all_in_one_df["DATE"] = all_in_one_df["DATE"].fillna("1970-01-01")
all_in_one_df["URL"] = all_in_one_df["URL"].fillna("www.xyzabc.com")
all_in_one_df["all_urls"] = all_in_one_df["all_urls"].fillna("www.somewesite.com")
all_in_one_df["website_title"] = all_in_one_df["website_title"].fillna("New Title")

print("#"*40, end="\n\n")
#########################

print("TOTAL Empty cells in entire dataframe")
print("-"*20)
# ----------------

print(all_in_one_df.isnull().sum())

print("#"*40, end="\n\n")
#########################

print("Create Final Reports")
print("-"*20)
# ----------------

all_in_one_df.to_csv("final_report.csv", index=False)
all_in_one_df.to_excel("final_report.xlsx", index=False)
all_in_one_df.to_json("final_report.json")
all_in_one_df.to_xml("final_report.xml")

print("""
Created Below Files, 
final_report.csv and 
final_report.xlsx
and final_report.json
and final_report.xml
Please check""")

print("#"*40, end="\n\n")
#########################