import json
import requests

url = 'https://httpbin.org/post' 
payload = {
    'ID': '20191524',
    'Name': 'Insoo Lee',
    'Department': 'IoT'
    }

rsp = requests.post(url, json=payload) 
print(rsp.text) 

json_data = json.loads(rsp.text)
print(json_data['json'])