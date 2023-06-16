from socket import *

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 8080))
sock.listen(2)

def http_200_response(mimeType):
    return 'HTTP/1.1 200 OK \r\n' + 'Content-Type: ' + mimeType + '\r\n' + '\r\n'

while True:
    client, addr = sock.accept()
    print('connection from ', addr)
    

    data = client.recv(1024).decode()
    req = data.split('\r\n')[0]
    method, path, protocol = req.split(' ')
    filename = path[1:]

    print('filename: ', filename)

    if filename == 'index.html': 
        f = open(filename, 'r', encoding='utf-8')
        data = f.read()
        f.close()
        mimeType = 'text/html'
        client.send(http_200_response(mimeType).encode())
        client.send(data.encode('euc-kr'))
    elif filename == 'iot.png': 
        f = open(filename, 'rb')
        data = f.read()
        f.close()
        mimeType = 'image/png'
        client.send(http_200_response(mimeType).encode())
        client.send(data)
    elif filename == 'favicon.ico':
        f = open(filename, 'rb')
        data = f.read()
        f.close()
        mimeType = 'image/x-icon'
        client.send(http_200_response(mimeType).encode())
        client.send(data)
    else:
        client.send(b'HTTP/1.1 404 Not Found\r\n')
        client.send(b'\r\n')
        client.send(b'<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>')
        client.send(b'<BODY>Not Found</BODY></HTML>')

    client.close()
    
