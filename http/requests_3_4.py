import requests
url = 'https://httpbin.org/put' 
data = {'IoT': '2017'}
rsp = requests.put(url, data=data) 
print('PUT data', rsp.text)

rsp = requests.put(url, json=data) 
print('PUT json', rsp.text)

files = {'file': open('iot.png', 'rb')} 
rsp = requests.post(url, files=files) 
print('PUT file', rsp.text)

rsp = requests.delete('https://httpbin.org/delete') 
print('DELETE', rsp.text)

rsp = requests.head('https://httpbin.org/get') 
print('HEAD header', rsp.headers)
print('HEAD text', rsp.text)
