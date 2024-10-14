from http.server import HTTPServer, BaseHTTPRequestHandler
import json


# Define a class for handle requests
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)  # OK status 200
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b'"Hello, this is a simple API!"')  # text resp
        elif self.path == '/data':  # Implement /data endpoint
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(bytes(json.dumps(response), "utf-8"))  # JSONresp
        elif self.path == '/status':  # Implement /status endpoint
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {"status": "OK"}
            self.wfile.write(bytes(json.dumps(response), "utf-8"))
        elif self.path == '/info':  # Implement /info endpoint
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(bytes(json.dumps(response), "utf-8"))
        else:
            self.send_error(404, "Endpoint not found")


# Set up the server on port 8000 : voir module ("TCPServer")
PORT = 8000

if __name__ == "__main__":
    with HTTPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
