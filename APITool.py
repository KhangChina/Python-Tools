import requests
import json

headers =  {"Content-Type":"application/json"}

api_url = "https://jsonplaceholder.typicode.com/todos/1"

#Get api
response = requests.get(api_url,headers=headers)
data = response.json()
#get status
print(response.status_code) 
#get data
print(data)

#Post API
api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
response = requests.post(api_url, json=todo,headers=headers)
response.json()

#get status
print(response.status_code) 
#get data
print(data)