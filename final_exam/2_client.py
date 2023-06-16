import time
import random
import socket

PORT = 7777
BUF_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', PORT))

my_id = input('ID 를 입력하세요! : ')

while True:
    temp = random.randint(0, 40)
    sock.send((my_id + ' ' + str(temp)).encode())
    time.sleep(5)
