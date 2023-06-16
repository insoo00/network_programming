import selectors
from socket import *

sel = selectors.DefaultSelector()

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 8080))
sock.listen(10)

def http_200_response(mimeType):
    return 'HTTP/1.1 200 OK \r\n' + 'Content-Type: ' + mimeType + '\r\n' + '\r\n'

def read(conn, mask):
    data = conn.recv(1024).decode()
    if not data:
        sel.unregister(conn)
        conn.close()
        return
    
    req = data.split('\r\n')[0]
    method, path, protocol = req.split(' ')
    filename = path[1:]

    if path == '/': 
        filename = 'index.html'
        f = open(filename, 'r', encoding='utf-8')
        data = f.read()
        f.close()
        mimeType = 'text/html'
        conn.send(http_200_response(mimeType).encode())
        conn.send(data.encode('euc-kr'))
    elif filename == 'iot.png': 
        f = open(filename, 'rb')
        data = f.read()
        f.close()
        mimeType = 'image/png'
        conn.send(http_200_response(mimeType).encode())
        conn.send(data)
    elif filename == 'favicon.ico':
        f = open(filename, 'rb')
        data = f.read()
        f.close()
        mimeType = 'image/x-icon'
        conn.send(http_200_response(mimeType).encode())
        conn.send(data)
    else:
        conn.send(b'HTTP/1.1 404 Not Found\r\n')
        conn.send(b'\r\n')
        conn.send(b'<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>')
        conn.send(b'<BODY>Not Found</BODY></HTML>')


def accept(sock, mask):
    conn, addr = sock.accept()
    print('connected from', addr)
    sel.register(conn, selectors.EVENT_READ, read)

sel.register(sock, selectors.EVENT_READ, accept)
while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)



