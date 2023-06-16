import selectors
import socket
import random

sel = selectors.DefaultSelector()

def accept(sock, mask):
    conn, addr = sock.accept()
    print('connected from', addr)
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
    data = conn.recv(1024)
    if not data:
        sel.unregister(conn)
        conn.close()
        return

    if data == b'1':
        temp = random.randint(0, 40)
        res = 'Temp='+str(temp)
    elif data == b'2':
        hum = random.randint(0, 100)
        res = 'Humid='+str(hum)

    conn.send(res.encode())

sock = socket.socket()
sock.bind(('', 9999))
sock.listen(5)

sel.register(sock, selectors.EVENT_READ, accept)
while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)

