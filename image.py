import http.server
import socketserver

class ImageHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/image.jpg':
            self.send_response(200)
            self.send_header('Content-type', 'image/jpeg')
            self.end_headers()
            with open('image.jpg', 'rb') as image_file:
                self.wfile.write(image_file.read())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Image not found')

PORT = 8000

with socketserver.TCPServer(("", PORT), ImageHTTPRequestHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
