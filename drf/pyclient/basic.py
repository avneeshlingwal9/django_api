import requests

endpoint = "https://httpbin.org/anything" ## The endpoint of the api. 

endpoint = "http://localhost:8000/api/" #http://locahost:8000/"


 ## HTTP Request. with JSON data.

get_response = requests.get(endpoint)

print(get_response.text) # Prints the code. 

print(get_response.status_code)

print(get_response.json()['message'])



