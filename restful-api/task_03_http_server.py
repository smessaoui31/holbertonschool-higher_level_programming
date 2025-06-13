#!/usr/bin/python3
"""
All module containing class for my first server
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# gestionnaire de requêtes HTTP


class MyServer(BaseHTTPRequestHandler):
    """
    Class to define my first server
    """

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)  # = OK
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")  # Type JSON
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            # Transformer le dictionnaire en texte JSON
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            message = "OK"

        else:
            self.send_response(404, message="Not Found")
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            message = "Endpoint not found"

        self.wfile.write(bytes(message, "utf8"))


# Launch the server on the port 8000
def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyServer)
    print("Server running on http://localhost:8000")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
