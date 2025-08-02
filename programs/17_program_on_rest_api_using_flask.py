"""
Python for web development
    3 things in web development
    1. website development
    2. REST-API development
    3. Microservices development
"""

"""
We have many web frameworks
example:
flask  # if we can manage front end code, backend code ,controller code everythin in one function block, then use flask
DJango # use this if the code is huge so we can not manage everything front end code, backend code, controller code.  
FastAPI
bottle
web2py
pyramid
many more

POPULAR:
flask # small framework  /synchronous. supporting web development , api development, microservices development, 
very old - so more community support. for developer , coding is same as FastAPI.but more efficient than FastAPI.

DJango (ModelViewTemplate) : # for big framework implementing modelviewtemplate architecture.
FastAPI # small framework 
"""

"""
Using flask framework, we can develop all 3
    1. website development
    2. REST-API development
    3. Microservices development
"""

"""
In our training, we are discussing on,
How to use flask framework for REST-API Development
"""
"""
Understanding REST-API
Example: Suppose we want to provide access to our mydb.sqlite3 with others/public
Then how we can provide access to our mydb.sqlite3 with others/public?

OPTION-1: We can create separate credentials like user/password etc with restricted permissions
and share to others.
    This OPTION is limited to internal use. NOT SUITABLE FOR PROVIDING ACCESS TO PUBLIC
"""

"""
We got 2 solutions
1. SOAP: Simple Object Access Protocol
2. REST: REpresentational State Transfer

Both are called architecture/designs/Style
Both tells how we can provide access to others

Both tells introduce MAIN-DOOR/INTERFACE to your application/db
it is like
our-application/DB  <--INTERFACE-->  others/public

Both tells how to write such INTERFACE

This INTERFACE is also called as APPLICATION PROGRAMMING INTERFACE (API)
We call: REST-API or SOAP-API 
"""

"""
REST came after SOAP
- REST is easy to implement and manage
- REST is popular
"""

"""
How to implement REST INTERFACE to provide access to our mydb.sqlite3?
- ANSWER: No need to implement REST architecture. BECAUSE flask-framework is already 
    implemented REST architecture.

WE JUST NEED TO KNOW, HOW TO USE FLASK-FRAMEWORK TO DEVELOP/IMPLEMENT REST-API
"""
"""
Assume We are planning to provide full-access/complete-access to our database

full-access/complete-access means
- provide access to add new records
- provide access to get records
- provide access to update records
- provide access to delete records
"""

"""
HTTP Standard methods : GET, POST, PUT, PATCH, DELETE

POST       - provide access to add new records
GET         - provide access to get records
PUT         - provide access to update entire row
PATCH     - provide access to update few cells like update only email, only phone-numbers
DELETE    - provide access to delete records
"""

"""
Web server: We need server to run any web application
flask-framework has builtin web-server, we can use for development purpose

FOR PRODUCTION: Few example production servers
https://wsgi.readthedocs.io/en/latest/servers.html 
"""

"""
flask-documentation: https://pypi.org/project/Flask/ 

Install: 
pip install Flask
"""
"""
To provide access for public or enduser to our database we will give an url. like
below url. user will use this url to access.
"""
# Sample url - https://demoqa.com/utilities/weather/city/bangalore

"""
In this release, we are planning to create REST-API
to provide access to get all records from our table

We finalized URL also called END POINT which
we are sharing with end user. End user will use that ENDPOINT/URL
to access our database

Finalized END POINT URL: http://127.0.0.1:5000/getdbdata
"""

# --------------
# Create App
# ---------------
import flask
my_rest_api_app = flask.Flask("MyAPIAPPName")
#########################

# --------------
# END POINT-1: URL http://127.0.0.1:5000/getdbdata mapped to route("/getdbdata")
# ---------------
@my_rest_api_app.route("/getdbdata", methods=["GET"])
def getdbdata():
    import sqlite3
    conn = sqlite3.connect("mydb.sqlite3")
    cur = conn.cursor()
    cur.execute("SELECT * FROM mytable")
    my_db_data = cur.fetchall()
    conn.close()
    return flask.jsonify(my_db_data)  # this will convert to json
# in case of API we need to communicate only using JSON only always
# URL Mapping : root url is http://127.0.0.1:5000/
# After root url we have getdbdata

# For url - https://demoqa.com/utilities/weather/city/bangalore
    # root url is utilities/weather/city/
    """
    @my_rest_api_app.route("/utilities/weather/city/<city_name", methods=["GET"])
    """
#########################

# --------------
# Run Builtin Server
# ---------------
my_rest_api_app.run() # Default host='127.0.0.1', port=5000. We can change ip address , port number if needed.
# my_rest_api_app.run(host="192.168.1.100", port=1234)
#########################
# RUN THE SERVER FIRST. THEN
# ACCESS THIS API USING END POINT : http://127.0.0.1:5000/getdbdata
# PANDIA IS ABLE TO ACCESS.
# Able to access below END POINT
# http://127.0.0.1:5000/getdbdata
# First run this server by running the program and then end user to can access the url to get the data in Json format.
# if this server is not running, then end user cannot access . he will get page not found error.

# Steps to create virtual environment and linking it to it.
# Go command program say c: python training folder.
#  C:\Python_training> python -m venv myvenv1
#  C:\Python_training> cd myvenv1
# C:\Python_training\myvenv1> cd scripts
# (myvenv1) PS C:\python_training\concepts> activate or ./activate
 # we will go back to Python training folder using cd ../..
# cd ..
# cd ..
#cd concepts
# (myvenv1) PS C:\Python_training\concepts> python  1_how_to_provide_description_and_comments.py
# Hello
# (myvenv1) PS C:\Python_training\concepts>
