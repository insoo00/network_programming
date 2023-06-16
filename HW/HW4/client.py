from socket import *

s = socket(AF_INET, SOCK_STREAM)
addr = ('localhost', 9001)
s.connect(addr)

while True:
    expression = input("Enter an expression (e.g. 20 + 17) or 'q' to quit: ")

    if expression == 'q':
        break
    
    s.send(expression.encode())

    try:
        result = s.recv(1024)
        if not result:
            break
    except:
        break

    print("Result: ", result.decode())

s.close()