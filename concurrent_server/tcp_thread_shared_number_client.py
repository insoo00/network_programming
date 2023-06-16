from socket import *

PORT = 2500
BUFSIZE = 1024

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', PORT))

print(int(s.recv(BUFSIZE).decode()))

s.close()