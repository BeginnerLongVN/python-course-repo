import requests

# get requests
# respone = requests.get("https://jsonplaceholder.typicode.com/todos/1")
# print(respone.status_code)
# print(respone.json())

# filter data
param = {"userId": 2}
respone = requests.get("https://jsonplaceholder.typicode.com/posts", param)
print(respone.json())
