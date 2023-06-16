from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 8888

class http_handler(BaseHTTPRequestHandler): 
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'image/png') 
            self.end_headers()
            with open('iot.png', 'rb') as f:
                msg = f.read()
                self.wfile.write(msg)

httpd = HTTPServer(('localhost', PORT), http_handler) 
print('Serving HTTP on {}:{}'.format('localhost', PORT)) 
httpd.serve_forever()