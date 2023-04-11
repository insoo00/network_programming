from socket import *
import random
import json

BUF_SIZE = 1024

sock = create_server(('', 6666), backlog=3)

while True:
    client, addr = sock.accept()
    print('connection from ', addr)

    msg = client.recv(BUF_SIZE)
    if not msg:
        client.close()
        continue
    
    if  msg.decode() == 'Request':
        heart_rate = random.randint(40, 140)
        step_count = random.randint(2000, 6000)
        calorie_consumed = random.randint(1000, 4000) 

        res = {}
        res['Heartbeat'] = heart_rate
        res['Steps'] = step_count
        res['Cal'] = calorie_consumed

        client.send(json.dumps(res).encode())

    elif msg.decode() == 'quit':
        client.close()
        break
