import requests
import re

# url = '192.168.0.139:8080'
# rsp = requests.get(url)
# html = rsp.text

html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>가짜 이메일</h1>
  <p>이메일 주소: example123@gmail.com</p>
  <p>보낸 사람: examasdasd3@gmail.com</p>
  <p>받는 사람: ex12312afsd123@gmail.com</p>
  <p>제목: 중요한 안내사항</p>
  <p>내용: 안녕하세요, 중요한 안내사항이 있어서 이 이메일을 보냅니다. 자세한 내용은 첨부 파일을 확인해주세요. 감사합니다.</p>
</body>
</html>
'''

# email_lists = re.findall(r'(<p>)([\s\S]+?)(<\/p>)', html)

# for email in email_lists:
#     result = re.findall(r'[a-zA-Z0-9_.]+@.+\.[a-z]{2,3}', email[1])
#     if result:
#         print(result[0])

result = re.findall(r'[a-zA-Z0-9_.]+@.+\.[a-z]{2,3}', html)
for item in result:
    print(item)