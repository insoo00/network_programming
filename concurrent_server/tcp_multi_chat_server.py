import socket
import threading
import time

clients = []
PORT = 2500
BUF_SIZE = 1024

def server_th(client, addr):
    while True:
        data = client.recv(BUF_SIZE)
        if 'quit' in data.decode():
            if client in clients:
                print(addr, 'exited')
                clients.remove(client)
                continue

        print(time.asctime() + str(addr) + ':' + data.decode())

        for client_in_clients in clients:
            if client_in_clients != client:
                client_in_clients.send(data)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', PORT))
s.listen(50)

print('Server Started')

while True:
    client, addr = s.accept()
    clients.append(client)
    print('new clients', addr)

    threading.Thread(target=server_th, args=(client, addr)).start()