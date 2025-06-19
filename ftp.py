import http.server
import socketserver

PORT = 8080  # You can change to any open port
DIRECTORY = "/home/kali/Desktop"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"🚀 Serving files from {DIRECTORY} at http://{httpd.server_address[0]}:{PORT}")
    httpd.serve_forever()
