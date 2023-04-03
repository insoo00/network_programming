import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)

msg = sock.recv(1024)
print(msg.decode())

name = "이인수"
sock.send(name.encode())

no = sock.recv(1024)
print(int.from_bytes(no, 'big'))

sock.close()