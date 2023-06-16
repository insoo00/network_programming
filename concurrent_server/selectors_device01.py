from socket import *
import random
import json
import time

PORT = 2500
BUF_SIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', PORT))
sock.listen(5)

while True:
    client, addr = sock.accept()
    print('connection from ', addr)

    msg = client.recv(BUF_SIZE)
    if not msg:
        client.close()
        continue
    
    # if msg == b'Register':
    if  msg.decode() == 'Register': 
        while True:
            temp = random.randint(0, 40)
            hum = random.randint(0, 100)
            lilum = random.randint(70, 150) 

            res = {}
            res['Temp'] = temp
            res['Humid'] = hum
            res['LiLum'] = lilum

            client.send(json.dumps(res).encode())
            time.sleep(3)

    elif msg.decode() == 'quit':
        client.close()
        break
