#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# gestionnaire de requêtes HTTP


class SimpleAPIHandler(BaseHTTPRequestHandler):

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

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            status = {
                "version": "1.0",
                "description": "A simple API built with http.server"
                }
            self.wfile.write(json.dumps(status).encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


# Launch the server on the port 8000
def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print("Server running on http://localhost:8000")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
