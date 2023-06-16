from socket import *

port = 9999
addr = ('localhost', port)

BUFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(addr)

while True:
    msg = input("Message to send: ")
    if msg != 'q':
        sock.send(msg.encode())
        data = sock.recv(BUFSIZE)
        print("Received message: %s" % data.decode())
    else:
        print("Quit")
        sock.close()
