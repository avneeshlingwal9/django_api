import requests

endpoint = "https://httpbin.org/anything" ## The endpoint of the api. 

get_response = requests.get(endpoint , json={"data": "hello world"} )
 ## HTTP Request. with JSON data.



print(get_response.text) # Prints the code. 

get_response = requests.get(endpoint, data={"query" : "hello world"})
print(get_response.json())


