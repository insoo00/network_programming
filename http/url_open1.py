from urllib import request

rsp = request.urlopen('https://home.sch.ac.kr/iot')

print('HTTP Response:', rsp) 
print('URL:', rsp.geturl()) 
print('Status:', rsp.getcode())
headers = rsp.info() 
print('Date:', headers['date']) 
print('Headers') 
print('-------------') 
print(headers)
data = rsp.read().decode() 
print('Length:', len(data)) 
# print('Data') 
# print('-------------') 
# print(data)



# HTTP Response: <http.client.HTTPResponse object at 0x103bbdab0>
# URL: https://home.sch.ac.kr/iot/
# Status: 200
# Date: Mon, 12 Jun 2023 09:02:08 GMT
# Headers
# -------------
# Date: Mon, 12 Jun 2023 09:02:08 GMT
# Server: Apache
# Cache-Control: no-cache, no-store, must-revalidate
# Pragma: no-cache
# Content-Length: 33910
# Expires: Thu, 01 Jan 1970 00:00:00 GMT
# Set-Cookie: SCHHOMEID=bkOu11ozG1pPb-FOKpOsAj4l9wMGhcXIVBy-teeGRjIYzvn_nHgj!1890782685; path=/; HttpOnly
# Set-Cookie: SSCSID=62HME0&&bkOu11ozG1pPb-FOKpOsAj4l9wMGhcXIVBy-teeGRjIYzvn_nHgj!1890782685!1686560528947; path=/
# Set-Cookie: iot_visited=Y; expires=Mon, 12-Jun-2023 15:00:32 GMT; path=/
# Set-Cookie: iot_visited=20230612180208949011; expires=Mon, 12-Jun-2023 15:00:32 GMT; path=/
# Connection: close
# Content-Type: text/html; charset=UTF-8
# Set-Cookie: cpFmxRbQpF6rdH0_=v1XW9rVQ__Tog; Path=/


# Length: 30423