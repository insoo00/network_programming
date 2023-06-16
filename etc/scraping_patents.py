from urllib import request
import requests
import re

url = 'https://bulkdata.uspto.gov/data/patent/officialgazette/2022/' 
rsp = requests.get(url)
html = rsp.text

file_list = re.findall(r'e-.+zip"', html) 
file_url = ''
for name in file_list:
    file_url = url + name[:-1] # 마지막 " 제거
    print(file_url)

request.urlretrieve(file_url, 'patent.zip')