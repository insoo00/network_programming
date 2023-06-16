from socket import *
import json
import time

BUF_SIZE = 1024

while True:
    sock1 = create_connection(('localhost', 5555))
    sock2 = create_connection(('localhost', 6666))

    msg = input("Input: ")
    if not msg:
        break

    if msg == '1':
        sock1.send('Request'.encode())
        res = sock1.recv(BUF_SIZE)
        if not res:
            break
        data = json.loads(res.decode())
        data_string = ', '.join([f"{key} = {value}" for key, value in data.items()])
        date = time.asctime()


        f = open('data.txt', 'a')
        print(data_string)
        f.write(date + ': '+ 'Device1: ' + data_string + '\n')
    
    elif msg == '2':
        sock2.send('Request'.encode())
        res = sock2.recv(BUF_SIZE)
        if not res:
            break
        data = json.loads(res.decode())
        data_string = ', '.join([f"{key} = {value}" for key, value in data.items()])
        date = time.asctime()

        f = open('data.txt', 'a')
        print(data_string)
        f.write(date + ': '+ 'Device2: ' + data_string + '\n')

    elif msg == 'quit':
        sock1.send('quit'.encode()) 
        sock2.send('quit'.encode()) 
        break

    sock1.close()
    sock2.close()
    f.close()
