from http.server import HTTPServer, BaseHTTPRequestHandler
import json

PORT = 8000  # Set up the server on port 8000

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """HTTP Server handling GET requests"""

    def do_GET(self):
        """Handles the GET requests"""
        if self.path == '/':
            self.send_response(200)  # OK status 200
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')  # text resp
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


if __name__ == "__main__":
    with HTTPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
