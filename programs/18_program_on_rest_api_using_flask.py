"""
In this release, we are supporting 2 endpoints
one end point for getting records
i.e
http://127.0.0.1:5000/getdbdata

another end point for adding new record
http://127.0.0.1:5000/adddbdata
"""

# --------------
# Create App
# ------- --------
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
# END POINT-2: URL http://127.0.0.1:5000/adddbdata mapped to route("/adddbdata")
# ---------------
@my_rest_api_app.route("/adddbdata", methods=["POST"])
def adddbdata():
    """
    Our Plan: User should send record in this format.
    Task-1: Receive new record details sent by end user
            Example: {"IP": "192.168.127.12", DATE:"20/Jun/2022", URL:"www.example.com"}
    Task-2: Check whether record exists
    Task-3: Add to database
    """

    # Task-1: Receive new record details sent by end user
    #             Example: {"IP": "192.168.127.12", DATE:"20/Jun/2022", URL:"www.example.com"}
    # ---------------
    received_data = flask.request.get_json()
    # received_data = {"IP": "192.168.127.12", DATE:"20/Jun/2022", URL:"www.example.com"}
    ip = received_data.get("IP")
    date = received_data.get("DATE")
    url = received_data.get("URL")

    # Task-2: Check whether record exists
    # ---------------
    import sqlite3
    conn = sqlite3.connect("mydb.sqlite3")
    cur = conn.cursor()
    my_sql_query = f"SELECT * FROM mytable WHERE IP = '{ip}'"
    cur.execute(my_sql_query)
    my_db_data = cur.fetchone() # Returns None if no record present
    print("PANDIA WANTS TO SEE", my_db_data)
    if my_db_data is None:
        my_sql_query = f"INSERT INTO MYTABLE VALUES('{ip}', '{date}', '{url}')"
        cur.execute(my_sql_query)
        conn.commit()
        conn.close()
        return flask.jsonify("Record added successfully")
    else:
        return flask.jsonify("Record already exists")
#########################

# --------------
# Run Builtin Server
# ---------------
my_rest_api_app.run() # Default host='127.0.0.1', port=5000
# my_rest_api_app.run(host="192.168.1.100", port=1234)
#########################

# ACCESS THIS API USING END POINT : http://127.0.0.1:5000/getdbdata
# For those who wants to get info from db, we give END POINT-1
# Use can access this url thro browser or thro post man or thro any rest client

# END POINT-2: URL http://127.0.0.1:5000/adddbdata mapped to route("/adddbdata")
# to run this we can use postman or any rest api.
# For those who wants to add info to db , we give END POINT-2
# Use can access this url thro browser with installing some extensions or thro post man or thro any rest client
# or thro any programming language.



