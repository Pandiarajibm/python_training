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
flask
DJango
FastAPI
bottle
web2py
pyramid
many more

POPULAR:
flask # small framework
DJango (ModelViewTemplate) :
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

WE JUST NEED TO KNOW, HOW TO USE FLASK-FRAMEWORK TO DEVELOP REST-API
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

# https://demoqa.com/utilities/weather/city/bangalore

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
    return flask.jsonify(my_db_data)
#########################

# --------------
# Run Builtin Server
# ---------------
my_rest_api_app.run() # Defau
# lt host='127.0.0.1', port=5000
# my_rest_api_app.run(host="192.168.1.100", port=1234)
#########################

# ACCESS THIS API USING END POINT : http://127.0.0.1:5000/getdbdata

# Able to access below END POINT
# http://127.0.0.1:5000/getdbdata
