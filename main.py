import http.server
import socketserver
import os

PORT = int(os.environ.get("PORT", 10000))

class CustomHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"<h1>Free Claude Code Proxy is running successfully!</h1>")

    def do_POST(self):
        self.do_GET()

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
