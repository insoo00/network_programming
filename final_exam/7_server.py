from socket import *
import select
import time

socks = [] # 소켓 리스트
PORT = 2500
BUF_SIZE = 1024

s_sock = socket()
s_sock.bind(('', PORT))
s_sock.listen(10)

socks.append(s_sock)
print(str(PORT) + '에서 접속 대기 중')

while True:
    r_sock, w_sock, e_sock = select.select(socks, [], [])

    for s in r_sock:
        if s == s_sock:
            c_sock, addr = s_sock.accept()
            socks.append(c_sock)
            print('Client ({}) connected'.format(addr))
        else:
            data = s.recv(BUF_SIZE)
            if 'quit' in data.decode():
                if s in socks:
                    print(addr, 'exited')
                    socks.remove(s)
                    continue

            print(time.asctime() + str(addr) + ':' + data.decode())

            for s_in_socks in socks:
                if s_in_socks == s_sock:
                    continue
                if s_in_socks != s:
                    s_in_socks.send(data)
