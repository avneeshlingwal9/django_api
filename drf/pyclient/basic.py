import requests

endpoint = "https://httpbin.org/anything" ## The endpoint of the api. 

endpoint = "http://localhost:8000/api/" #http://locahost:8000/"


 ## HTTP Request. with JSON data.

get_response = requests.get(endpoint , params={"abc": 123}, json={"query": "What"})

print("Respose is: ", get_response.text)





