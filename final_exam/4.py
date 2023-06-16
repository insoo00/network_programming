import requests
import re

url = 'https://en.wikipedia.org/wiki/Internet_of_things'
rsp = requests.get(url)
html = rsp.text
# print(html)

result = re.findall(r'[iI][oO][tT][\w]+[\b]?', html)
print(result)
