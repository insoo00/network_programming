import requests
import re

url = 'https://finance.naver.com/item/main.nhn?code=005930'
rsp = requests.get(url)
html = rsp.text

stock_results = re.findall(r'(<dl class="blind">)([\s\S]+?)(<\/dl>)', html) # <dl class>~</dl> 정보를 추출
# print('stock_results: ', stock_results)
samsung_stock = stock_results[0] # HTML 내에 2개의 <dl class>~</dl> 부분이 존재. 첫 번째 것을 선택 
# print('samsung_stock: ', samsung_stock)
samsung_index = samsung_stock[1] # <dl class>~</dl> 사이의 정보만 추출
# print('samsung_index: ', samsung_index)

# 주식 정보(<dd>~</dd>)를 추출
index_list = re.findall(r'(<dd>)([\s\S]+?)(<\/dd>)', samsung_index)

for index in index_list:
    print(index[1])

