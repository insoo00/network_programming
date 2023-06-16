import selectors
from socket import *
import json
import time

BUF_SIZE = 1024

sel = selectors.DefaultSelector()

def conn_device1(conn, mask):
    res = conn.recv(BUF_SIZE)
    if not res:
        sel.unregister(conn)
        conn.close()
        return  

    data = json.loads(res.decode())
    data_string = ', '.join([f"{key} = {value}" for key, value in data.items()])
    date = time.asctime()
    
    f = open('data.txt', 'a')
    print(data_string)
    f.write(date + ': '+ 'Device1: ' + data_string + '\n')

def conn_device2(conn, mask):
    res = conn.recv(BUF_SIZE)
    if not res:
        sel.unregister(conn)
        conn.close()
        return  
    
    data = json.loads(res.decode())
    data_string = ', '.join([f"{key} = {value}" for key, value in data.items()])
    date = time.asctime()
    
    f = open('data.txt', 'a')
    print(data_string)
    f.write(date + ': '+ 'Device2: ' + data_string + '\n')

device1_sock = socket(AF_INET, SOCK_STREAM)
device1_sock.connect(('localhost', 2500))

device2_sock = socket(AF_INET, SOCK_STREAM)
device2_sock.connect(('localhost', 3500))

device1_sock.send('Register'.encode())
device2_sock.send('Register'.encode())

sel.register(device1_sock, selectors.EVENT_READ, conn_device1)
sel.register(device2_sock, selectors.EVENT_READ, conn_device2)

while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)
