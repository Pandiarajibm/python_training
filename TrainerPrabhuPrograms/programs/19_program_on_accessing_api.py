"""
requests library: to access APIs
https://pypi.org/project/requests/
"""

print("Accessing Weather API")
print("-"*20)
# ----------------

import requests

response = requests.get("https://demoqa.com/utilities/weather/city/bangalore")
weather_data = response.json()

print("weather_data:", weather_data, end="\n\n")

print("Type of weather_data:", type(weather_data), end="\n\n")

print("#"*40, end="\n\n")
#########################

print("GET: get db data ")
print("-"*20)
# ----------------


try:
    import requests
    response = requests.get("http://127.0.0.1:5000/getdbdata")
    db_data = response.json()
    print("db_data:", db_data, end="\n\n")
except Exception as e:
    print("Error Details:", e, end="\n\n")
    print("Not able to access API, Please check 18_program_on_rest_api.py is running")
    exit(1)

print("#"*40, end="\n\n")
#########################

print("POST: Add new record to database ")
print("-"*20)
# ----------------


try:
    import requests
    response = requests.post("http://127.0.0.1:5000/adddbdata",
                             json={"IP": "192.168.127.12", "DATE": "20/Jun/2022", "URL": "www.example.com"}
                                   )
    db_data = response.json()
    print("db_data:", db_data, end="\n\n")
except Exception as e:
    print("Error Details:", e, end="\n\n")
    print("Not able to access API, Please check 18_program_on_rest_api.py is running")
    exit(1)

print("#"*40, end="\n\n")
#########################
