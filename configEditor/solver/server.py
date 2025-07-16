from http.server import BaseHTTPRequestHandler, HTTPServer
class server(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        exploit_file = open('exp.yml', 'rb')
        self.wfile.write(exploit_file.read())
        self.end_headers()

ip,port = 'localhost', 8000
s = HTTPServer((ip,port), server)
print(f'Server running on {ip}:{port}')
s.serve_forever()