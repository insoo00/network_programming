import socket
import threading

class HTTPHandler:
    def __init__(self, client_socket, client_address):
        self.client_socket = client_socket
        self.client_address = client_address

    def handle_request(self):
        request_data = self.client_socket.recv(1024).decode()
        if request_data.startswith('GET'):
            self.send_response()

        self.client_socket.close()

    def send_response(self):
        status_line = 'HTTP/1.1 200 OK\r\n'
        content_type = 'Content-Type: image/png\r\n\r\n'

        with open('iot.png', 'rb') as f:
            image_data = f.read()

        response = status_line.encode() + content_type.encode() + image_data
        self.client_socket.sendall(response)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 8888)
    server_socket.bind(server_address)
    server_socket.listen(5)
    print('Serving HTTP on {}:{}'.format(*server_address))

    while True:
        client_socket, client_address = server_socket.accept()
        handler = HTTPHandler(client_socket, client_address)
        thread = threading.Thread(target=handler.handle_request)
        thread.start()

start_server()
