from socket import *
import random
import json
import time

PORT = 3500
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
            heart_rate = random.randint(40, 140)
            step_count = random.randint(2000, 6000)
            calorie_consumed = random.randint(1000, 4000) 

            res = {}
            res['Heartbeat'] = heart_rate
            res['Steps'] = step_count
            res['Cal'] = calorie_consumed

            client.send(json.dumps(res).encode())
            time.sleep(5)

    elif msg.decode() == 'quit':
        client.close()
        break
