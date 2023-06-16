from socket import *
import threading

PORT = 7777
BUFSIZE = 1024

sharedData = {
    '1': [],
    '2': []
}

def thread_handler(sock):
    global sharedData, lock

    while True:
        data = sock.recv(BUFSIZE).decode()
        if data.startswith('1'):
            temp_data = data.split(' ')[1]
            lock.acquire()
            sharedData['1'].append(temp_data)
            lock.release()
        elif data.startswith('2'):
            temp_data = data.split(' ')[1]
            lock.acquire()
            sharedData['2'].append(temp_data)
            lock.release()

        print(sharedData)
        
s = socket(AF_INET, SOCK_STREAM)
s.bind(('', PORT))
s.listen(5)

lock = threading.Lock()

while True:
    client, addr = s.accept()
    print('connected by ', addr)
    th = threading.Thread(target=thread_handler, args=(client,))
    th.start()
    
