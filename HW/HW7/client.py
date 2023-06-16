import socket
import threading

PORT = 2501
BUF_SIZE = 1024


def client_th(sock):
    while True:
        data = sock.recv(BUF_SIZE)
        print(data.decode())

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', PORT))

my_id = input('ID 를 입력하세요! : ')
sock.send(('[' + my_id + ']').encode())

th = threading.Thread(target=client_th, args=(sock,))
th.daemon = True
th.start()

while True:
    msg = '[' + my_id + '] ' + input()
    sock.send(msg.encode())