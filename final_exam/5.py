from urllib import parse
import requests

url = 'https://search.naver.com/search.naver?query=iot'

parsed_url = parse.urlparse(url)
print(parsed_url)

# parsed_url_except_query =  + parsed_url.path + parsed_url.params + parsed_url.fragment
parsed_url_except_query = parse.urljoin(parsed_url.scheme + '://' + parsed_url.netloc, parsed_url.path + parsed_url.params + parsed_url.fragment) 
print(parsed_url_except_query)

payload = parsed_url.query
rsp = requests.get(parsed_url_except_query, params=payload) 
print(rsp.headers) # 응답 헤더 
