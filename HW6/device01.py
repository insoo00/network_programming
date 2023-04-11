from socket import *
import random
import json

BUF_SIZE = 1024

sock = create_server(('', 5555), backlog= 3)

while True:
    client, addr = sock.accept()
    print('connection from ', addr)

    msg = client.recv(BUF_SIZE)
    if not msg:
        client.close()
        continue
    
    if  msg.decode() == 'Request':
        temp = random.randint(0, 40)
        hum = random.randint(0, 100)
        illum = random.randint(70, 150) 

        res = {}
        res['Temp'] = temp
        res['Humid'] = hum
        res['Illum'] = illum

        client.send(json.dumps(res).encode())

    elif msg.decode() == 'quit':
        client.close()
        break
