#!/usr/bin/python3
"""
    Set up a basic web server using the http.server module.
    Handle different types of HTTP requests (GET, POST, etc.).
    Serve JSON data in response to specific endpoints.
"""
#import http.server
#import socketserver

from http.server import HTTPServer, BaseHTTPRequestHandler
import json


"""basic webserver"""
def webserver_basic():
    
    PORT = 8000

    Handler = http.server.SimpleHTTPRequestHandler
    # Handler = BaseHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()


class simpleHTTPServer(BaseHTTPRequestHandler):
    """class SimpleHTTPServer inherited from BaseHTTPRequestHandler
        duplicate the function of http.server.SimpleHTTPRequestHandler
    """
    def do_GET(self):
        """Handle HTTP GET request"""
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, this is a simple API!')

httpd = HTTPServer(('', 8000), simpleHTTPServer)
httpd.serve_forever()

# def main():
# webserver_basic()   

