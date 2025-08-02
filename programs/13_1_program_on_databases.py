"""
Program on databases
SQLITE3 Documentation: https://docs.python.org/3/library/sqlite3.html

for sql connector documentation - pypi.org/project/mysql-connector-python/
library found in Big repository-

first run the database server for mysql connector. then connect to it.

Sample Code for mysql connector

import mysql.connector

# Connect to server
cnx = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="mike",
    password="s3cre3t!")

# Get a cursor
cur = cnx.cursor()

# Execute a query
cur.execute("SELECT CURDATE()")

# Fetch one result
row = cur.fetchone()
print("Current date is: {0}".format(row[0]))

# Close connection
cnx.close()


Sample Code

import mysql.connector

# Connect to server
cnx = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="mike",
    password="s3cre3t!")

# Get a cursor
cur = cnx.cursor()

# Execute a query
cur.execute("SELECT CURDATE()")

# Fetch one result
row = cur.fetchone()
print("Current date is: {0}".format(row[0]))

# Close connection
cnx.close()

Problem Statement:
Get data from sample_data.txt
then
Extract Info
then
send extracted information to database


How to communicate with database in python?

We have libraries for each databases(SQL/No-SQL)

Example:
    python-program  <--communicate using library cx_oracle -->  Oracle Database
    python-program  <--communicate using library mysqlconnector -->  mysql Database
    python-program  <--communicate using library sqlite3 -->  sqlite3 Database


We need one database.
- We can use SQLite database
- lightweight database
- This database will not run any database server
- It will just create one database file, That file is database.
    - we can run sql-query on that file



How to install/create-and-communicate with SQLite database?

2 WAYS

1-WAY: Install SQLite database software
       https://sqlitebrowser.org/dl/
       # select DB Browser for SQLite - .zip (no installer) for 64-bit Windows
       # zip all will get stored in downloads. extract it.
       # to run software,database server , execute DB Browser for SQLite.exe to connect to file

2-WAY: WITHOUT Installing SQLite database software,
            Using python-library, Sqlite3, we can create database and execute query
our notes we will create one database and 1 table. we will extract the data from browser and print. and send it to
database. we need 3 columns in the table to store ip, date, url. data type of column could be varchar

"""

print("Create database 'mydb.sqlite3' and table 'mytable'")
print("-" * 20)
# ------- ---------

import sqlite3

"""
 Below step 1 it will create db file - mydb.sqllite3 in local directory programs
# C:\python_training\programs folder
# we can change the directory path to store some other path if needed
"""
my_db_connection = sqlite3.connect('mydb.sqlite3')  # step1
my_cursor = my_db_connection.cursor()  # step 2 followed by step3
my_sql_query = """
               CREATE TABLE IF NOT EXISTS mytable \
               ( \
                   IP \
                   VARCHAR \
               ( \
                   100 \
               ),
                   DATE VARCHAR \
               ( \
                   100 \
               ),
                   URL VARCHAR \
               ( \
                   100 \
               )) \
               """
my_cursor.execute(my_sql_query)  # step4

my_file_handle = open(file="sample_data.txt", mode="r")
file_contents = my_file_handle.readlines()
my_file_handle.close()

print(file_contents)

print("Extract IP, DATE, URL and print")
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

print("#" * 40, end="\n\n")
#########################

print("Extract IP, DATE, URL and Send It Database")
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
        my_sql_query = f"INSERT INTO MYTABLE VALUES('{ip}', '{dt}', '{url}')"
        print("Executing SQL Query:", my_sql_query)
        my_cursor.execute(my_sql_query)
        print("One Record Inserted\n")

my_db_connection.commit()
print("All records inserted. Please check database")

print("#" * 40, end="\n\n")
#########################

print("Get data from database and print")
print("-" * 20)
# ----------------

my_sql_query = "SELECT * FROM mytable"
my_cursor.execute(my_sql_query)
my_db_result = my_cursor.fetchall()
print(my_db_result)

my_db_connection.close()

print("#" * 40, end="\n\n")
#########################
