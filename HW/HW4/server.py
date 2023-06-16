from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('',9001))
s.listen(2)

def calculator(expression):
    val1, operator, val2 = expression.split(' ')
    val1 = int(val1)
    val2 = int(val2)
    
    if(operator == '+'):
        return val1 + val2
    elif(operator == '-'):
        return val1 - val2
    elif(operator == '*'):
        return val1 * val2
    elif(operator == '/'):
        return round(val1 / val2, 1)
    else:
        return "Error: Invalid expression"

while True:
    client, addr = s.accept()
    while True:
        try:
            expression = client.recv(1024).decode()
            client.send(str(calculator(expression)).encode())
        except:
            break

    client.close()
