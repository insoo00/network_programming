import requests
rsp = requests.get('https://naver.com') 
print(rsp.status_code) # 응답 상태 코드 
print(rsp.encoding) # 응답 데이터의 인코딩 방식

url = 'https://search.naver.com/search.naver' 
payload = {'query': 'IoT'}
rsp = requests.get(url, params=payload) 
print(rsp.url) # 요청 URL 
print(rsp.headers) # 응답 헤더 
print(rsp.text[:1000]) # 응답 데이터

# 200

# UTF-8

# https://search.naver.com/search.naver?query=IoT

# {'Date': 'Mon, 12 Jun 2023 09:33:52 GMT', 'Content-Type': 'text/html; charset=UTF-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Set-Cookie': 'page_uid=i4kElsprvN8ssFlYnjNssssstLR-338108; path=/; domain=.naver.com, _naver_usersession_=Oksy9JHZySYn1D+TLSJHKA==; path=/; expires=Mon, 12-Jun-23 09:38:52 GMT; domain=.naver.com, nx_ssl=2; Domain=.naver.com; Path=/; Expires=Wed, 12-Jul-2023 09:33:52 GMT;', 'X-Frame-Options': 'SAMEORIGIN', 'X-XSS-Protection': '1; report=/p/er/post/xss', 'Cache-Control': 'no-cache, no-store, must-revalidate, max-age=0', 'Pragma': 'no-cache', 'Referrer-Policy': 'unsafe-url', 'Vary': 'Accept-Encoding', 'Content-Encoding': 'gzip', 'Server': 'nxg', 'Accept-CH': 'Sec-CH-UA, Sec-CH-UA-Arch, Sec-CH-UA-Bitness, Sec-CH-UA-Full-Version-List, Sec-CH-UA-Mobile, Sec-CH-UA-Model, Sec-CH-UA-Platform, Sec-CH-UA-Platform-Version, Sec-CH-UA-WoW64'}

# <!doctype html> <html lang="ko"><head> <meta charset="utf-8"> <meta name="referrer" content="always">  <meta name="format-detection" content="telephone=no,address=no,email=no"> <meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=2.0"> <meta property="og:title" content="IoT : 네이버 통합검색"/> <meta property="og:image" content="https://ssl.pstatic.net/sstatic/search/common/og_v3.png"> <meta property="og:description" content="'IoT'의 네이버 통합검색 결과입니다."> <meta name="description" lang="ko" content="'IoT'의 네이버 통합검색 결과입니다."> <title>IoT : 네이버 통합검색</title> <link rel="shortcut icon" href="https://ssl.pstatic.net/sstatic/search/favicon/favicon_191118_pc.ico">  <link rel="search" type="application/opensearchdescription+xml" href="https://ssl.pstatic.net/sstatic/search/opensearch-description.https.xml" title="Naver" /><script> if (top.frames.length!=0 || window!=top) window.open(location, "_top"); </script><link rel="stylesheet" type="text/css" href="https://ssl.pstatic.net/ss